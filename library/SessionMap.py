from resources.configs import *
from resources.results import *
from library.features import start
from library.wr_Json import JsonWriter


@advance('mapping')
def manager(product_page_link):
    product_info = start(product_page_link)
    obj = JsonWriter()
    obj.json_writer(product_info)
    print(product_info)


if __name__ == "__main__":
    product_link = output_config.get('product_link')
    manager(product_link)
    # stop()
