from page_objects.launch import visit_url
from page_objects.next import navigator
from resources.results import output_config
from resources.configs import *
from library.csv_report import first_modify, jsontocsv, rewrite
import os

def delete_old_results():
    results_folder = output_config.get('results')
    for file_old in os.listdir(results_folder):
        files = os.path.join(results_folder, file_old)
        print("Deleted:{}".format(files))
        os.remove(files)


@advance('deleted old results')
@advance('scrapping started')
def main():
    try:
        delete_old_results()
    except Exception as e:
        print("error:", e)
    try:
        launch = visit_url()
        if navigator(launch):
            print("Completed !")
    except Exception as e:
        print("error:", e)
    print('started generate report...')
    sleep(60)
    try:
        first_modify(output_config.get('json_file'))
    except Exception as e:
        print("error:", e)
    try:
        rewrite(output_config.get('json_file'))
    except Exception as e:
        print("error:", e)
    try:
        jsontocsv(output_config.get('jsonreport'))
    except Exception as e:
        print("error:", e)


if __name__ == "__main__":
    main()
