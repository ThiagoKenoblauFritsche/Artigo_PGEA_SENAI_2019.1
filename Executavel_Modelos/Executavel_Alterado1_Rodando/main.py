from kivymd.app import MDApp  
from kivy.lang.builder import Builder
from mainwidget import MainWidget

class MainApp(MDApp):
    def build(self):
        self._widget = MainWidget()
        return self._widget

if __name__ == "__main__":
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True)
    MainApp().run()

