from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    chars = {}

    url = input("Input website you want analyzed: ")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.get_text())
    for i in soup.get_text():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    print("Website chosen:", r.url)
    print("Characters: ", chars)

