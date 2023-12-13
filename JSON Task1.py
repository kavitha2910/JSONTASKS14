import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = None
    
    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Failed to fetch data")

    def display_country_info(self):
        if not self.data:
            self.fetch_data()
        
        if self.data:
            for country in self.data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                if currencies:
                    currency_names = ', '.join(currencies.keys())
                    currency_symbols = ', '.join([c.get('symbol', 'N/A') for c in currencies.values()])
                    print(f"Country: {name}")
                    print(f"Currencies: {currency_names}")
                    print(f"Currency Symbols: {currency_symbols}")
                    print("=" * 30)

    def countries_with_currency(self, currency):
        if not self.data:
            self.fetch_data()
        
        if self.data:
            for country in self.data:
                name = country.get('name', {}).get('common', 'N/A')
                currencies = country.get('currencies', {})
                if currencies and currency in currencies:
                    print(f"Country with {currency} as currency: {name}")

    def display_dollar_countries(self):
        self.countries_with_currency('USD')

    def display_euro_countries(self):
        self.countries_with_currency('EUR')


url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
country_data.display_country_info()
country_data.display_dollar_countries()
country_data.display_euro_countries()
