import requests
from bs4 import BeautifulSoup
import nltk
import pickle

path = 'C:\\Users\\MC_VIC\\Dropbox\\1 семестр\\ПИ\\лр4\\dictionary.pkl'


def main():
    url = 'http://www.yomaker.ru/yoslovar.htm'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, features="html.parser")

    headers = soup.find_all('p')

    word_list = []

    for wrd in headers[38:]:
        word_list.append(wrd.text)

    active_list = []
    for el in word_list:
        if len(el) >= 2:
            el.replace('.', '').replace(',', '')
            active_list.append(el[0:])

    active_list[2] = active_list[2].replace('n', ' ').split().pop(0)

    alone_wrds = nltk.word_tokenize(str(active_list), "russian")

    goal_wrds = [x for x in alone_wrds if list(x).__contains__('ё')]

    only_wrds = []

    for i in goal_wrds:
        if not i[0].isalpha():
            only_wrds.append(i[1:])
        elif i[0].isalpha():
            only_wrds.append(i)

    pickle_create_file(only_wrds)


def pickle_create_file(list):
    f = open(path, 'wb')
    pickle.dump(list, f)
    print("Словарь в файле PICKLE и сохранен в " + path + "!")


if __name__ == '__main__':
    main()