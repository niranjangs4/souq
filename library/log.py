def writer(file_name, line):
    with open(file_name, 'a+') as data:
        data.write("{}\n".format(line))
