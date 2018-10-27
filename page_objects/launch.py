from resources.configs import *



class LaunchVariables:
    url = launch_config.get('souq')
    wait = launch_config.get('implicit')
    menu_button = launch_config.get('menu')
    categories_id = launch_config.get('categories_id')
    perfume = launch_config.get('Perfumes_Fragrances')


@advance('launch browser')
def visit_url():
    driver.get(LaunchVariables.url)
    driver.maximize_window()
    driver.implicitly_wait(LaunchVariables.wait)
    driver.find_element_by_class_name(LaunchVariables.menu_button).click()
    driver.find_element_by_id(LaunchVariables.categories_id).click()
    driver.find_element_by_id(LaunchVariables.categories_id).send_keys(Keys.PAGE_DOWN)
    return driver.find_element_by_link_text(LaunchVariables.perfume).get_attribute('href')


if __name__ == "__main__":
    print(visit_url())
