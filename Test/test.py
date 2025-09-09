from kivymd.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        return BoxLayout(
            md_bg_color=self.theme_cls.primary_color
        )

MyApp().run()