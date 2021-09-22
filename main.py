from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, CardTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem


class ScreenManagement(ScreenManager):
    pass

class MainScreen(MDScreen):
    pass

class QRScreen(MDScreen):
   
    def on_pre_enter(self):
        print("Entering...")
        self.ids.zbarcam.start()

    def on_pre_leave(self):
        print("Closing camera...")
        self.ids.zbarcam.stop()

        print("Camera closed")




class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.root.transition= CardTransition()

    def get_qrcode(self):
        self.root.current = 'qrscreen'

    def return_to_main(self):
        self.root.current = 'mainscreen'

    def get_code_data(self, data_lst):
        print(data_lst)
        for i in data_lst:
            if i not in [i.text for i in self.root.screens[0].ids.qrlist.children]:
                list_item = OneLineListItem(text=i)
                self.root.screens[0].ids.qrlist.add_widget(list_item)
        return ', '.join(data_lst)

    


if __name__ == '__main__':
    app = MainApp()
    app.run()