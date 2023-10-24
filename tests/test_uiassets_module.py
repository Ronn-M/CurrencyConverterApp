import sys

wd = '/home/sr-ronn-m/Documents/Python Projects/CurrencyConverterApp/'

sys.path.insert(0, wd)

import UIAssets

def test_get_currencies_default() -> None:
    
    result = UIAssets.get_currencies()
    
    assert type(result) is dict

def test_convert_default() -> None:
    
    req_format_0 = 'USD'
    req_format_1 = 'AUD'
    req_format_2 = 1000
    
    result = UIAssets.convert(req_format_0, req_format_1, req_format_2)
    
    assert type(result) is float or result == 'Connection Error!'

def test_convert_default_str() -> None:
    
    req_format_0 = 'USD'
    req_format_1 = 'AUD'
    req_format_2 = '1000'
    
    result = UIAssets.convert(req_format_0, req_format_1, req_format_2) 
    
    assert type(result) is float or result == 'Connection Error!'
    
def test_convert_unknown_str() -> None:
    
    req_format_0 = 'USD'
    req_format_1 = 'AUD'
    req_format_2 = 'ABC'
    
    result = UIAssets.convert(req_format_0, req_format_1, req_format_2)    
    
    print('true')
    
    assert result == 'Database Error!' or result == 'Connection Error!'
    