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
        '''Start the camera'''
        print("Starting Camera...")
        self.ids.zbarcam.start()

    def on_pre_leave(self):
        '''Pause the camera'''
        print("Pausing camera...")
        self.ids.zbarcam.stop()




class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.root.transition= CardTransition()

    def get_qrcode(self):
        self.root.current = 'qrscreen'

    def return_to_main(self):
        self.root.current = 'mainscreen'

    def get_code_data(self, data_lst):
        '''Get the qr code data, create list item and add it to the main window'''
        for i in data_lst:
            # check to see if list item with same text already exists
            if i not in [i.text for i in self.root.screens[0].ids.qrlist.children]:
                list_item = OneLineListItem(text=i)
                self.root.screens[0].ids.qrlist.add_widget(list_item)
        return ', '.join(data_lst)

    


if __name__ == '__main__':
    app = MainApp()
    app.run()