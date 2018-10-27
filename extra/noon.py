import requests
from bs4 import BeautifulSoup
import io
import json
import os

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def delete_old_results():
    for old_file in ["file_json.json","final_json_file.json","json_file.json","json_file.csv"]:
        try:
            os.remove(old_file)
        except Exception as e:
            print(e)


def json_writer(dict_value):
    with io.open("file_json.json", 'a+', encoding='utf8') as outfile:
        str_ = json.dumps(dict_value,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
        outfile.write(",\n")


link = r"https://www.noon.com/en-sa/beauty-and-health/beauty/fragrance?page="
item = []
count = 0
product_info = {}
with requests.Session() as session:
    def extract():

        global count
        count += 1
        page = link + str(count)
        print(page)
        response = session.get(page)
        if response:
            product_labal = {}
            soup = BeautifulSoup(response.content, "html.parser")
            for no, i in enumerate(soup.select("div.jsx-3611441087.productContainer")):
                try:
                    product_labal.update(brand=i.find('p', attrs={'class': 'jsx-1505126516 brand'}).text)
                except Exception as e:
                    product_labal.update(brand="not avalible")
                try:
                    product_labal.update(name=i.find('div', attrs={'class': 'jsx-1505126516 name'}).text)
                except Exception as e:
                    product_labal.update(name="not avalible")
                try:
                    product_labal.update(
                        original=i.find('span', attrs={'class': 'jsx-996473556 preReductionPrice'}).text.split()[-1])
                except Exception as e:
                    product_labal.update(original="not avalible")
                try:
                    product_labal.update(
                        sell=i.find('span', attrs={'class': 'jsx-996473556 sellingPrice'}).text.split()[-1])
                except Exception as e:
                    product_labal.update(sell="not avalible")
                print(product_labal)
                if not product_labal:
                    break
                try:
                    json_writer(product_labal)
                except Exception as e:
                    print(e)
        return extract()
if __name__ == "__main__":
    delete_old_results()
    extract()
