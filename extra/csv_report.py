import pandas as pd
import os, time

json_report = 'final_json_file.json'

def first_modify(file_json):
    with open(file_json, 'a+') as file_writer:
        file_writer.seek(0, os.SEEK_END)  # seek to end of file; f.seek(0, 2) is legal
        file_writer.seek(file_writer.tell() - 3, os.SEEK_SET)  # go backwards 3 bytes
        file_writer.truncate()
        file_writer.write("]")


def rewrite(json_file):
    with open(json_file,encoding="utf8") as read_json:
        with open(json_report,'w+',encoding="utf8") as json_writer:
            json_writer.write("[\n")
            for line in read_json.readlines():
                json_writer.write(line)


def jsontocsv(json_report):
    try:
        df = pd.read_json(json_report, orient='columns')
        df.to_csv('json_file.csv')
    except ValueError as ve:
        print("Error: Json file not proper.\nplease check in reports folder")


if __name__ == "__main__":
    first_modify('file_json.json')
    time.sleep(2)
    rewrite('file_json.json')
    jsontocsv(json_report)
