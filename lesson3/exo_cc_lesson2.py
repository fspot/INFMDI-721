import unittest
import requests
from bs4 import BeautifulSoup

URL_PAGE2 = "https://kim.fspot.org/cours/page2.html"
URL_PAGE3 = "https://kim.fspot.org/cours/page3.html"


# Write a function which extract some infos from the pages above.
# Example:
#     get_prices_from_url(URL_PAGE2) should return something like this:
#
#     {
#         'Personal': {
#             'price': '$5',
#             'storage': '1GB',
#             'databases': 1
#         },
#         'Small Business': {
#             'price': '$25',
#             'storage': '10GB',
#             'databases': 5
#         },
#         'Enterprise': {
#             'price': '$45',
#             'storage': '100GB',
#             'databases': 25
#         }
#     }
def get_prices_from_url(url):
    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
URL_BEERLIST_AUTRICHE = "https://www.beerwulf.com/fr-FR/api/search/searchProducts?country=Autriche&container=Bouteille"


def get_soup_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


def extract_beer_infos(url):
    # Example url: https://www.beerwulf.com/fr-fr/p/bieres/brouwerij-t-verzet-super-noah.33
    soup = get_soup_from_url(url)

    # Extract name:
    name = soup.find("h1").text

    # Extract price:
    price = soup.select('span.price')[0].text
    price = float(price[2:].replace(',', '.'))  # "€ 2,29" => 2.29

    # Extract volume:
    volume = soup.find('dt', text='Contenu').find_next_sibling()
    volume = int(volume.text[:-2])  # "33cl" => 33

    # Extract evaluation:
    note = soup.find('div', class_='stars')
    note = int(note.attrs['data-percent'])

    # Extract EBC:
    ebc = soup.find('div', class_='ebc')
    children = ebc.find_all('div')
    active_tag = ebc.find('div', class_='active')
    position = children.index(active_tag)
    ebc_pct = position / len(children) * 100

    infos = {
        'name': name,
        'price': price,
        'volume': volume,
        'note': note,
        'ebc': ebc_pct,
    }
    return infos


# This function takes a parameter "url" which (as its name suggests) is a url
# pointing to a page of beerwulf API which contains a list of beers.
# This function should return a list of beer informations, by using
# the function extract_beer_infos that we wrote previously.
# Example:
#     extract_beer_list_infos(URL_BEERLIST_AUTRICHE) should return a list like this:
#
#     [{'name': 'Brew Age Affenkönig', 'price': 3.49, 'volume': 33, 'note': 70, 'ebc': 30.7},
#      {'name': 'Stiegl Goldbraü', 'price': 2.49, 'volume': 33, 'note': 70, 'ebc': 38.4},
#      {'name': 'Bevog Rudeen Black IPA', 'price': 3.39, 'volume': 33, 'note': 80, 'ebc': 84.6},
#      {'name': 'Stiegl Columbus 1492', 'price': 1.99, 'volume': 33, 'note': 70, 'ebc': 7.6},
#      {'name': 'Engelszell Benno', 'price': 4.99, 'volume': 33, 'note': 70, 'ebc': 46.1},
#      {'name': 'Engelszell Gregorius', 'price': 5.49, 'volume': 33, 'note': 70, 'ebc': 53.8},
#      {'name': 'Bevog Tak Pale Ale', 'price': 2.79, 'volume': 33, 'note': 70, 'ebc': 23.1},
#      {'name': 'Brew Age Hopfenauflauf', 'price': 2.99, 'volume': 33, 'note': 70, 'ebc': 7.6}]
def extract_beer_list_infos(url):
    return


class Lesson2Tests(unittest.TestCase):
    def test_01_get_prices_from_url_page2(self):
        prices = get_prices_from_url(URL_PAGE2)
        # We should have found 3 products:
        self.assertIsInstance(prices, dict)
        self.assertEqual(len(prices), 3)
        self.assertIn('Personal', prices)
        self.assertIn('Small Business', prices)
        self.assertIn('Enterprise', prices)

        personal = prices['Personal']
        self.assertIn('price', personal)
        self.assertIn('storage', personal)
        self.assertIn('databases', personal)
        self.assertEqual(personal['price'], '$5')
        self.assertEqual(personal['storage'], '1GB')
        self.assertEqual(personal['databases'], 1)

    def test_02_get_prices_from_url_page3(self):
        prices = get_prices_from_url(URL_PAGE3)
        self.assertIsInstance(prices, dict)
        self.assertEqual(len(prices), 4)
        self.assertEqual(
            prices['Privilege'],
            {'databases': 100, 'price': '$99', 'storage': '1TB'}
        )

    def test_03_extract_beer_list_infos(self):
        infos = extract_beer_list_infos(URL_BEERLIST_AUTRICHE)
        # We should have 8 austrian beers:
        self.assertIsInstance(infos, list)
        self.assertEqual(len(infos), 8)
        # All of them are 33cl:
        for beer in infos:
            self.assertEqual(beer['volume'], 33)


def run_tests():
    test_suite = unittest.makeSuite(Lesson2Tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)


if __name__ == '__main__':
    run_tests()
