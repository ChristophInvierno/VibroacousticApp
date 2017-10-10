from bokeh.plotting import figure, show, output_file

output_file('image.html')

p = figure(x_range=(0,550), y_range=(0,550))
p.image_url(url=['scheme.png'], x=0, y=550, w=550, h=550)
show(p)