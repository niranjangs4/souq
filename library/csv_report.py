import pandas as pd
from resources.results import output_config
import os


json_report = output_config.get('jsonreport')

def first_modify(file_json):
    with open(file_json, 'a+') as file_writer:
        file_writer.seek(0, os.SEEK_END)  # seek to end of file; f.seek(0, 2) is legal
        file_writer.seek(file_writer.tell() - 3, os.SEEK_SET)  # go backwards 3 bytes
        file_writer.truncate()
        file_writer.write("]")


def rewrite(json_file):
    with open(json_file,errors='ignore',encoding="utf8") as read_json:
        with open(json_report,'a+',errors='ignore',encoding="utf8") as json_writer:
            json_writer.write("[\n")
            for line in read_json.readlines():
                json_writer.write(line)


def jsontocsv(json_report):
    try:
        df = pd.read_json(json_report, orient='columns')
        df.to_csv(output_config.get('csv_file'))
    except ValueError as ve:
        print("Error: Json file not proper.\nplease check in reports folder")


if __name__ == "__main__":
    first_modify(output_config.get('json_file'))
    rewrite(output_config.get('json_file'))
    jsontocsv(json_report)
