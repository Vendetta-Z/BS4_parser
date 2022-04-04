from bs4 import BeautifulSoup
import requests
import requests


def soup():
    x = 0
    all_links = []
    while True:
        Url = 'https://news.ycombinator.com/news?p=' + str(x)
        request = requests.get(Url)

        soup = BeautifulSoup(request.text, 'html.parser')
        title_links = soup.find_all('td', class_='title')

        for link in title_links:
            link = link.find('a', {'class': 'titlelink'})
            if link is not None:
                all_links.append(link)

        nex = soup.find(class_='morelink')
        try:
            nexlink = nex.get('href')
            x += 1
            nexx = nexlink[6:]
        except Exception:
            print('Succesfull!!')
            with open('result.txt', 'w', encoding="utf-8") as f:
                for link in all_links:
                    f.write(str(link.text + '\n' + link['href'] + '\n ================================ \n'))
            return all_links

if __name__ == '__main__':
    soup()
