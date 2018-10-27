# encoding=utf8

"""
link : input is product page link
"""
from resources.configs import *
from resources.results import output_config


@advance('Collection product features...')
def start(link):
    item = {}
    global session
    with requests.Session() as session:
        response = session.get(link)
        if response:
            soup = BeautifulSoup(response.content, "html.parser")
            for i in soup.select("div.hide"):
                if i.findAll('dt'):
                    for k, v in zip(i.findAll('dt'), i.findAll('dd')):
                        item[k.text] = v.text
            try:
                item.update({"sell price": soup.find('h3', attrs={'class': 'price is sk-clr1'}).text.split()[0]})
            except Exception as e:
                item.update({"sell price": "not present"})
            try:
                item.update({"original": soup.find('span', attrs={'class': 'was'}).text.split()[0]})
            except Exception as e:
                item.update({"original": "not present"})
            try:
                item.update({"save": soup.find('span', attrs={'class': 'noWrap'}).text.split()[0]})
            except Exception as e:
                item.update({"save": "not present"})
            try:
                item.update(
                    {"quantity": soup.find('div', attrs={'class': 'tabs-panel is-active'}).text.strip().split()})
            except Exception as e:
                item.update({"quantity": "not present"})
            try:
                condition = soup.find('dl', attrs={'class': 'stats clearfix'}).text
                a = [i.strip().strip(':') for i in condition.splitlines() if i.strip()]
                item.update({item_1: a[index + 1] for index, item_1 in enumerate(a) if index % 2 == 0})
                item.update({"Product name": soup.find('h1').text})
            except Exception as e:
                item.update({"Product name": "not present"})
            try:
                item.update({"Product rating": rating.strip() for rating in
                             soup.find('div', attrs={'class': 'large-4 small-12 columns'}).text.splitlines() if
                             'out' in rating})

            except Exception as e:
                item.update({"Product rating": "not present"})
            try:
                item.update({"users rating": rat_usr.strip().split()[0] for rat_usr in
                             soup.find('div', attrs={'class': 'large-4 small-12 columns'}).text.splitlines() if
                             'ratings' in rat_usr})
            except Exception as e:
                item.update({"users rating": "not present"})
            try:
                item.update({"product review":
                                 [product.text.split() for product in
                                  soup.findAll('a', attrs={'class': 'linkToReviewsTab'})][-1][
                                     0]})
            except Exception as e:
                item.update({"product review": "not present"})
            try:
                item.update({"recommends": soup.find('span', attrs={'class': 'messaging'}).text.strip()})
            except Exception as e:
                item.update({"recommends": "not present"})
            try:
                item.update(
                    {'shipping': ship.split('\n') for ship in
                     soup.find('li', attrs={'class': 'region'}).text.split('\n\n')
                     if
                     'Shipping' in ship})
            except Exception as e:
                item.update({'shipping': "not present"})
            finally:
                return item


def stop():
    session.close()


if __name__ == "__main__":
    product_page_link = output_config.get('product_link')
    print(start(product_page_link))
