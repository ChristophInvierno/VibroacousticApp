from bokeh.models import Div


class Message:

    def __init__(self, Color = "red",
                 Size = 4,
                 MessageHeader = 'Message: ',
                 Width = 500,
                 Hight = 20 ):


        self.Header = MessageHeader
        self.Color = Color
        self.Size = Size


        self.Widget = Div( text = "",
                           render_as_text = False,
                           width = Width,
                           height = Hight )

    def clean(self):
        self.Text = ''
        self._updateObject( );


    def printMessage(self, Text = 'none'):
        self.Text = self.Header + Text
        self._updateObject();


    def _updateObject(self):
        self.Widget.text = """
        <p><b><font size="{}" color="{}">
        {}
        </font></b></p>""".format( self.Size, self.Color,self.Text )