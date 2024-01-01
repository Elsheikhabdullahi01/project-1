from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string('''
<Example>:
    id: my_id
    BoxLayout:
        orientation: 'vertical'
        size: root.width, root.height
        spacing: 40
        padding: 50
        
        Image:
            id: im
            source: ' '
        FileChooserListView:
            id: chose
            on_selection: root.I(chose.selection)
        Label:
            id: la
            text: 'Choose Image'
            size_hint: (1,0.2)
            font_size: 35

''')
class Example(Widget):
    def I(self, file):
        try:
            self.ids.im.source = file[0]
            self.ids.la.text ='You Choose: \n '+ str(file)
        except:
            pass
class MyApp(App):
    def build(self):
        return Example()
      
MyApp().run()