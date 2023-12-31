from kivymd.app import MDApp
from kivy.lang import Builder



  
class MyApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Brown'
        return Builder.load_string('''
<My@MDSwiperItem>:
    #id: my
MDScreen:
#    id: my

    MDTopAppBar:
      #  id: my
        left_action_items: [['menu']]
        id: my
        title: 'Galary'.upper()
        pos_hint: {'top':1}
        
    MDSwiper:  
      #  id: my  
        size_hint_y: None
        height: root.height - my.height - dp(30)
        y:root.height - self.height - my.height - dp(20)
        
        My:
       #     
            BoxLayout:
                #id: my
                size: self.width, self.height
                spacing: 10
                padding: 20
                orientation: 'vertical'
                
                Image:
                    id: im
                    source: ' '
                    
                FileChooserIconView:
                    id: c
                    on_selection: app.Se(c.selection)
                
        My:
            FitImage:
                source: 'IMG-20230727-WA0033.jpg'
                radius: [60]
               
        My:
            FitImage:
                source: 'FB_IMG_16775863970187907.jpg'
                radius: [60]
                
        My:
            FitImage:
                source: 'logo.png'
                radius: [60]
        My:
            FitImage:
                source: 'status_me_status_IMG-20230416-WA0027.jpg'
                radius: [60]
           
     
''')  
    def Se(self, file):
      #  print(file)
        self.root.ids.im.source = file[0]

        
        
MyApp().run()