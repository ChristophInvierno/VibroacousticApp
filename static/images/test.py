from bokeh.plotting import figure, show, output_file
from bokeh.models.glyphs import ImageURL
from bokeh.models import ColumnDataSource


output_file('image.html')

p = figure(x_range=(0,550), y_range=(0,550))
#p.image_url(url=['scheme.png'], x=0, y=550, w=550, h=550)


source = ColumnDataSource(dict(
    url = ["scheme.png"],
    x1  = [ 0 ],
    y1  = [ 550 ],
    w1  = [ 550 ],
    h1  = [ 550 ],
))


image1 = ImageURL(url="url", x="x1", y="y1", w="w1", h="h1", anchor="center")
p.add_glyph(source, image1)
show(p)