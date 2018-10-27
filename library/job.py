import sys
import threading
import time


flag = False
output = []


def get_job():
    line = file_operation.readline().strip()
    if 'stop' in line:
        global flag
        flag = True
        return False
    elif line:
        print("release job:{}".format(line))
        return line


def write_job(line):
    with open(file_1, 'a+') as file_wr:
        file_wr.write("{}\n".format(line))
    return True


def assign_job():
    if flag:
        sys.exit(1)
    else:
        job = get_job()
        task(job)


def get_employes(count):
    threading.Thread(target=assign_job).start()


def task(job):
    if not job:
        sys.exit(1)
    print("running task:{}".format(job))
    time.sleep(1)
    assign_job()


if __name__ == "__main__":
    get_employes(50)
