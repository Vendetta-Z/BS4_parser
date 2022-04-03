from bs4 import BeautifulSoup
import requests
import requests

x = 0
while True:
    if x == 0:
        Url = 'https://news.ycombinator.com/news?p=1'
    else:
        Url = 'https://news.ycombinator.com/news?p=' + str(x)
    request = requests.get(Url)

    soup = BeautifulSoup(request.text, 'html.parser')
    title_links = soup.find_all('td', class_='title')

    all_links = []
    for link in title_links:
        link = link.find('a', {'class': 'titlelink'})
        if link != None:
            all_links.append(link)
            print('======')
            print(link)

    nex = soup.find(class_='morelink')
    nexlink = nex.get('href')
    nexx = nexlink[6:]
    x += 1



#
# if __name__ == '__main__':
#     print(soup)
