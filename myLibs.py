from selenium.webdriver import Firefox


def writeListToFile(lst, filename):
    f = open(filename, "w")
    for row in lst:
        f.write(row.text + "\n")
    f.close()


def findCommons(file1, file2):
    with open(file1) as f1:
        list1 = f1.read().splitlines()
    with open(file2) as f2:
        list2 = f2.read().splitlines()
    commons = list(set(list1).intersection(list2))

    return commons

