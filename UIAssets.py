import json
import requests  

def get_currencies():

    currencies_list = {
        
        'Australia Dollar': 'AUD', 'Great Britain Pound': 'GBP', 'Euro': 'EUR', 'Japan Yen': 'JPY', 'Switzerland Franc': 'CHF', 'USA Dollar': 'USD', 
        'Afghanistan Afghani': 'AFN', 'Albania Lek': 'ALL', 'Algeria Dinar': 'DZD', 'Angola Kwanza': 'AOA', 'Argentina Peso': 'ARS', 
        'Armenia Dram': 'AMD', 'Aruba Florin': 'AWG', 'Austria Schilling': 'ATS (EURO)', 'Belgium Franc': 'BEF (EURO)', 'Azerbaijan New Manat': 'AZN', 
        'Bahamas Dollar': 'BSD', 'Bahrain Dinar': 'BHD', 'Bangladesh Taka': 'BDT', 'Barbados Dollar': 'BBD', 'Belarus Ruble': 'BYR', 
        'Belize Dollar': 'BZD', 'Bermuda Dollar': 'BMD', 'Bhutan Ngultrum': 'BTN', 'Bolivia Boliviano': 'BOB', 'Bosnia Mark': 'BAM', 
        'Botswana Pula': 'BWP', 'Brazil Real': 'BRL', 'Brunei Dollar': 'BND', 'Bulgaria Lev': 'BGN', 'Burundi Franc': 'BIF', 'CFA Franc BCEAO': 'XOF', 
        'CFA Franc BEAC': 'XAF', 'CFP Franc': 'XPF', 'Cambodia Riel': 'KHR', 'Canada Dollar': 'CAD', 'Cape Verde Escudo': 'CVE', 
        'Cayman Islands Dollar': 'KYD', 'Chili Peso': 'CLP', 'China Yuan/Renminbi': 'CNY', 'Colombia Peso': 'COP', 'Comoros Franc': 'KMF', 
        'Congo Franc': 'CDF', 'Costa Rica Colon': 'CRC', 'Croatia Kuna': 'HRK', 'Cuba Convertible Peso': 'CUC', 'Cuba Peso': 'CUP', 
        'Cyprus Pound': 'CYP (EURO)', 'Czech Koruna': 'CZK', 'Denmark Krone': 'DKK', 'Djibouti Franc': 'DJF', 'Dominican Republich Peso': 'DOP', 
        'East Caribbean Dollar': 'XCD', 'Egypt Pound': 'EGP', 'El Salvador Colon': 'SVC', 'Estonia Kroon': 'EEK (EURO)', 'Ethiopia Birr': 'ETB', 
        'Falkland Islands Pound': 'FKP', 'Finland Markka': 'FIM (EURO)', 'Fiji Dollar': 'FJD', 'Gambia Dalasi': 'GMD', 'Georgia Lari': 'GEL', 
        'Germany Mark': 'DMK (EURO)', 'Ghana New Cedi': 'GHS', 'Gibraltar Pound': 'GIP', 'Greece Drachma': 'GRD (EURO)', 'Guatemala Quetzal': 'GTQ', 
        'Guinea Franc': 'GNF', 'Guyana Dollar': 'GYD', 'Haiti Gourde': 'HTG', 'Honduras Lempira': 'HNL', 'Hong Kong Dollar': 'HKD', 
        'Hungary Forint': 'HUF', 'Iceland Krona': 'ISK', 'India Rupee': 'INR', 'Indonesia Rupiah': 'IDR', 'Iran Rial': 'IRR', 'Iraq Dinar': 'IQD', 
        'Ireland Pound': 'IED (EURO)', 'Israel New Shekel': 'ILS', 'Italy Lira': 'ITL (EURO)', 'Jamaica Dollar': 'JMD', 'Jordan Dinar': 'JOD', 
        'Kazakhstan Tenge': 'KZT', 'Kenya Shilling': 'KES', 'Kuwait Dinar': 'KWD', 'Kyrgyzstan Som': 'KGS', 'Laos Kip': 'LAK', 'Latvia Lats': 'LVL (EURO)', 
        'Lebanon Pound': 'LBP', 'Lesotho Loti': 'LSL', 'Liberia Dollar': 'LRD', 'Libya Dinar': 'LYD', 'Lithuania Litas': 'LTL (EURO)', 
        'Luxembourg Franc': 'LUF (EURO)', 'Macau Pataca': 'MOP', 'Macedonia Denar': 'MKD', 'Malagasy Ariary': 'MGA', 'Malawi Kwacha': 'MWK', 
        'Malaysia Ringgit': 'MYR', 'Maldives Rufiyaa': 'MVR', 'Malta Lira': 'MTL (EURO)', 'Mauritania Ouguiya': 'MRO', 'Mauritius Rupee': 'MUR', 'Mexico Peso': 'MXN',
        'Moldova Leu': 'MDL', 'Mongolia Tugrik': 'MNT', 'Morocco Dirham': 'MAD', 'Mozambique New Metical': 'MZN', 'Myanmar Kyat': 'MMK', 'NL Antilles Guilder': 'ANG',
        'Namibia Dollar': 'NAD', 'Nepal Rupee': 'NPR', 'Netherlands Guilder': 'NLG (EURO)', 'New Zealand Dollar': 'NZD', 'Nicaragua Cordoba Oro': 'NIO', 
        'Nigeria Naira': 'NGN', 'North Korea Won': 'KPW', 'Norway Kroner': 'NOK', 'Oman Rial': 'OMR', 'Pakistan Rupee': 'PKR', 'Panama Balboa': 'PAB', 
        'Papua New Guinea Kina': 'PGK', 'Paraguay Guarani': 'PYG', 'Peru Nuevo Sol': 'PEN', 'Philippines Peso': 'PHP', 'Poland Zloty': 'PLN', 
        'Portugal Escudo': 'PTE (EURO)', 'Qatar Rial': 'QAR', 'Romania New Lei': 'RON', 'Russia Rouble': 'RUB', 'Rwanda Franc': 'RWF', 'Samoa Tala': 'WST', 
        'Sao Tome/Principe Dobra': 'STD', 'Saudi Arabia Riyal': 'SAR', 'Serbia Dinar': 'RSD', 'Seychelles Rupee': 'SCR', 'Sierra Leone Leone': 'SLL', 
        'Singapore Dollar': 'SGD', 'Slovakia Koruna': 'SKK (EURO)', 'Slovenia Tolar': 'SIT (EURO)', 'Solomon Islands Dollar': 'SBD', 'Somali Shilling': 'SOS', 
        'South Africa Rand': 'ZAR', 'South Korea Won': 'KRW', 'Spain Peseta': 'ESP (EURO)', 'Sri Lanka Rupee': 'LKR', 'St Helena Pound': 'SHP', 
        'Sudan Pound': 'SDG', 'Suriname Dollar': 'SRD', 'Swaziland Lilangeni': 'SZL', 'Sweden Krona': 'SEK', 'Syria Pound': 'SYP', 'Taiwan Dollar': 'TWD', 
        'Tanzania Shilling': 'TZS', 'Thailand Baht': 'THB', "Tonga Pa'anga": 'TOP', 'Trinidad/Tobago Dollar': 'TTD', 'Tunisia Dinar': 'TND', 
        'Turkish New Lira': 'TRY', 'Turkmenistan Manat': 'TMM', 'Uganda Shilling': 'UGX', 'Ukraine Hryvnia': 'UAH', 'Uruguay Peso': 'UYU', 
        'United Arab Emirates Dirham': 'AED', 'Vanuatu Vatu': 'VUV', 'Venezuela Bolivar': 'VEB', 'Vietnam Dong': 'VND', 'Yemen Rial': 'YER', 
        'Zambia Kwacha': 'ZMK', 'Zimbabwe Dollar': 'ZWD'}

    return currencies_list

def create_currencylist():

    currencies_list = get_currencies()
    
    with open('kv_data/CurrencyList.kv', 'wt') as file:

        spacer_i    = '\n\n\t'
        spacer_ii   = '\n\n\t\t'
        spacer_iii  = '\n\n\t\t\t'
        spacer_iv   = '\n\n\t\t\t\t'

        file.write( f"MDScreen: { spacer_i }name: 'currencylist' { spacer_i }ScrollView:" )
        file.write( f" {spacer_ii}id: scrollview {spacer_ii}name: '' { spacer_ii }MDBoxLayout: { spacer_iii }orientation: 'vertical' " )
        file.write( f" { spacer_iii }" + "pos_hint: { 'center_x': 0.5, 'center_y': 0.5 }" + f" { spacer_iii }" + "size_hint: 1, 10.38" )
        
        for currency_name in currencies_list.keys(): 
			
            widget = f' { spacer_iii }OneLineListItem: { spacer_iv }text: "{ currency_name }" ' + \
                     f' { spacer_iv }text_color: "#FFFFFF" { spacer_iv }on_release: app.set_currency( self.text, root.ids.scrollview.name ) \n'
            
            file.write( widget )

        file.close()

    return 

def convert( convert_from, convert_to, amount ):

    try:

        if amount != '':
            
            # api source - https://api-ninjas.com/api/convertcurrency
            api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={ convert_to }&have={ convert_from }&amount={ amount }'

	        # create key from api-source above
            key = 'place key here'

            response = requests.get( api_url, 
                                     headers={ 'X-Api-Key': key } )

            if response.status_code == requests.codes.ok:

                new_amount = json.loads( response.text )
                new_amount = new_amount[ 'new_amount' ]
                
                return str( new_amount )

            else:
                
                text = json.loads( response.text ) 

                return 'Database Error!'
    
    except BaseException as e:
        
        return 'Connection Error!'
    
