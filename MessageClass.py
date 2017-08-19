from bokeh.models import Div

class Message:

    def __init__(self, MessageHeader = 'Message: '):
        self.Header = MessageHeader;

        self.Widget = Div( text = "",
                           render_as_text = False,
                           width = 500,
                           height = 20 )

    def clean(self):
        self.Text = ''
        self._updateObject( );


    def printMessage(self, Text = 'none'):
        self.Text = self.Header + Text
        self._updateObject();


    def _updateObject(self):
        self.Widget.text = """
        <p><b><font size="4"> <font color="red">
        {}
        </font></font></b></p>""".format( self.Text )