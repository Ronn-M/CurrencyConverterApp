from dataclasses import dataclass

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from kivymd.app import MDApp

from UIAssets import convert, get_currencies

screenmanager = ScreenManager()

class CurrencyConverter( MDApp ):

    args: str
    field_name: str
    currency_name: str
    
    def build( self )  -> object:

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.material_style = 'M3'
        
        converterui  = Builder.load_file( 'kv_data/CurrencyConverterPage.kv' )
        currencylist = Builder.load_file( 'kv_data/CurrencyList.kv' )
        
        screenmanager.add_widget( converterui )
        screenmanager.add_widget( currencylist )

        return screenmanager

    def currencylist(self, field_name: str ) -> None:

        screenmanager.current = 'currencylist'   
        screen = screenmanager.current_screen
        
        screen.ids.scrollview.name = field_name
        
        Window.release_all_keyboards()

    def set_currency( self, currency_name: str, field_name: str ) -> None:
        
        screenmanager.current = 'converterui' 
        screen = screenmanager.current_screen

        if field_name == 'convertto': screen.ids.convertto.text = currency_name
        if field_name == 'convertfrom': screen.ids.convertfrom.text = currency_name

    def converterui( self, *args: str ) -> None:

        screenmanager.current = 'converterui'   
        screen = screenmanager.current_screen

        amount = args[2].text
        convertto = args[1].text
        convertfrom = args[0].text
        
        if convertfrom != '' and convertto != '' and amount != '':

            currencies_list = get_currencies()

            converted_amount = str( convert( currencies_list[ convertfrom ], 
                                        currencies_list[ convertto ], 
                                        amount ) )

            screen.ids.amount.text = ''
            
            if converted_amount != 'Connection Error!' and converted_amount != 'Database Error!':
                
                screen.ids.result.text = f'{ converted_amount } { currencies_list[ convertto ] }'
            
            else: screen.ids.result.text = converted_amount 

        else: 

            screen.ids.result.text = ''
                               
if __name__ == '__main__':

    CurrencyConverter().run()
