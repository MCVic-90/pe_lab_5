import requests
from bs4 import BeautifulSoup


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
            active_word = el.replace('.', ' ').replace(',', ' ').split()
            if len(active_word[0]) >= 2:
                first_wrd = active_word[0]
                active_list.append(first_wrd)

    #for wrd in enumerate(active_list):
    #   print(str(wrd[0]) + " -- " + str(wrd[1]))

    print(str(len(active_list)-1) + " words in dictionary")


if __name__ == '__main__':
    main()
