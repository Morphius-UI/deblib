import pandas as pd
def parsinfo(filepath):
    file = pd.read_excel(filepath) 	#считывает таблицу
    dtb = file.values.tolist()		#форматирует таблицу в матрицу
    return dtb


def cheaklogin(text):
    a = []
    b = []
    for i in parsinfo('D:\PyCharm Community Edition 2024.2\LDOD\Project\проект.xlsx'):
        a.append(i[0])
    if a.count(text) == 1:
        return True
    else:
        return False

def cheakfio(text):
    a = []
    for i in parsinfo('D:\PyCharm Community Edition 2024.2\LDOD\Project\проект.xlsx'):
        a.append(i[0])
        a.append(i[1])

    if a.count(text) == 1:
        return a[a.index(text)+1]

def cheaklog(text):
    a = []
    for i in parsinfo('D:\PyCharm Community Edition 2024.2\LDOD\Project\проект.xlsx'):
        a.append(i[0])
        a.append(i[1])

    if a.count(text) == 1:
        return a[a.index(text)]

def cheakklass(text):
    a = []
    for i in parsinfo('D:\PyCharm Community Edition 2024.2\LDOD\Project\проект.xlsx'):
        a.append(i[0])
        a.append(i[2])


    if a.count(text) == 1:
        return a[a.index(text)+1]


def istina(list):
    x = []
    for i in parsinfo('D:\PyCharm Community Edition 2024.2\LDOD\Project\Истинная инфа.xlsx'):
        x.append(i[1:4])
        print(list)
        print(x)
        if x.count(list) == 1:
            return True
    else:
        return False

def numberlogin(text):
    a = []
    b = []
    for i in parsinfo('D:\PyCharm Community Edition 2024.2\LDOD\Project\проект.xlsx'):
        a.append(i[0])
    if a.count(text) == 1:
        b = a.index(text)
        return b

