import json
import io
from resources.results import output_config

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

json_filename = output_config.get('json_file')

class JsonWriter:
    def __init__(self):
        self.file_json = json_filename
        # self.first_line()

    def first_line(self):
        with open(self.file_json, 'a+') as file_writer:
            file_writer.write('[')

    def json_writer(self, dict_value):
        with io.open(self.file_json, 'a+', encoding='utf8') as outfile:
            str_ = json.dumps(dict_value,
                              indent=4, sort_keys=True,
                              separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))
            outfile.write(",\n")
        return True


if __name__ == "__main__":

    data = {'Brand': 'Calvin Klein', 'Size': '200ml',
            'Targeted Group': 'Unisex',
            'EAN-13': '0088300104437',
            'UPC-A': '88300104437',
            'Perfume Name ': 'CK Be', 'Expirable': '',
            'Item EAN': '2724274285489',
            'Fragrance Type': 'Eau de Toilette',
            'Fragrance Family': 'Floral Woody Musk',
            'Fragrance Notes': 'Top Notes: Lavender, Green Notes, Mint, Mandarin Orange, Juniper, Bergamot\nMiddle Notes: Green Grass, Magnolia, Orchid, Freesia, Peach, Jasmine\nBase NTop Notes: Lavender, Green Notes, Mint, Mandarin Orange, Juniper, Bergamot\nMiddle Notes: Green Grass, Magnolia, Orchid, Freesia, Peach, Jasmine\nBase Notes: Sandalwood, Amber, Opoponax, Musk, Cedar, Vanilla\xa0Read more',
            'Alternative EANs': '2724267190196',
            'sell price': '74.99', 'original': '289.00',
            'save': '214.01',
            'quantity': ['200ml', '100ml'],
            'Condition': 'New', 'Sold by': 'dod_uae',
            'Seller Note': '100% Authenticity Guaranteed by Souq',
            'Product name': 'CK Be by Calvin Klein for Unisex - Eau de Toilette, 200ml',
            'Product rating': '4 out of 5',
            'users rating': '801',
            'product review': '174', 'recommends': '81.1',
            'shipping': ['UAE', 'Egypt', 'Saudi',
                         'Kuwait',
                         '-- International Shipping Countries --',
                         'Bahrain', 'Oman', 'Qatar']}
    obj = JsonWriter()
    obj.json_writer(data)
    obj.json_writer(data)
