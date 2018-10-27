from resources.configs import *
from library.log import writer
from page_objects.launch import visit_url
from library.SessionMap import manager
from resources.results import output_config
import threading


class NextVariables:
    next_filename = output_config.get('pages')
    product_filename = output_config.get('product')


def navigator(page):
    try:
        driver.get(page)
        writer(NextVariables.next_filename, page)  # writing next page links
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
        sleep(interval)
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
        element = WebDriverWait(driver, 100)
        element.until(EC.visibility_of_element_located((By.CLASS_NAME, 'pagination-next')))
        element.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'pagination-next'), 'Next'))
        grid_list = driver.find_element_by_class_name('grid-list')
        for i in grid_list.find_elements_by_class_name('itemLink'):
            product = i.get_attribute('href')
            print(product)
            employes = threading.Thread(target=manager, args={product}).start()
            """multi thread"""
            #print(employes)
            writer(NextVariables.product_filename, product)  # writing product page links
    except Exception as e:
        driver.refresh()
        navigator(page)
    try:
        global nex_page
        nex_page = driver.find_element_by_link_text('Next').get_attribute('href')
    except Exception as e:
        print('Completed !')
        driver.close()
    return navigator(nex_page)


if __name__ == "__main__":
    navigator(visit_url())
