from kivy.clock import Clock
from kivy.core.window import Window

from kivy.lang import Builder

from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

from UIAssets import convert, create_currencylist, get_currencies

create_currencylist()
screenmanager = ScreenManager()

class CurrencyConverter( MDApp ):

    def build( self ):

        self.theme_cls.material_style = 'M3'
        self.theme_cls.theme_style = 'Dark'
        
        converterui = Builder.load_file('kv_data/CurrencyConverterPage.kv')
        currencylist = Builder.load_file('kv_data/CurrencyList.kv')

        screenmanager.add_widget( converterui )
        screenmanager.add_widget( currencylist )

        return screenmanager

    def currencylist(self, field_name ):

        screenmanager.current = 'currencylist'   
        screen = screenmanager.current_screen

        Window.release_all_keyboards()

        screen.ids.scrollview.name = field_name

    def set_currency( self, currency_name, field_name ):
        
        screenmanager.current = 'converterui' 
        screen = screenmanager.current_screen

        if field_name == 'convertfrom':
            screen.ids.convertfrom.text = currency_name

        if field_name == 'convertto':
            screen.ids.convertto.text = currency_name

    def converterui( self, *args ):

        screenmanager.current = 'converterui'   
        screen = screenmanager.current_screen

        currencies_list = get_currencies()

        if args[0]:

            if type(args[0]) is not float and args[0].text != '' and args[1].text != '' and args[2].text != '':

                converted_amount = convert( currencies_list[args[0].text], currencies_list[args[1].text], args[2].text )

                screen.ids.result.text = str(converted_amount)

                screen.ids.amount.text = ''
            
            else: 

                screen.ids.result.text = ''
                               
if __name__ == '__main__':

    CurrencyConverter().run()
