# BS4_parser
Это парсер сайта Hackernews, наш скрипт парсит ссылки на статьи из ленты сайта , и записывает их в txt файл.
Для работы данного скрипта понадобиться скачать пару библиотек :
    BueautifulSoup4
    Requests

pip install beautifulsoup4
    
pip install Requests 


Url = Переменная с адресом страницы в которой находятся необходимые спарсить объекты 
title_links = В этой переменной находяться все нужные нам элементы , которые отбирались по названию тэга, и названию класса

Первым циклом проходимся по всем объектам из title_links , находим в каждом из них ссылку и добавляем в список all_links 
В блоке Try\except пытаемся нащупать кнопку more , если кнопка есть , цикл продолжает свою работу дальше ,
Если кнопки нет , все ссылки и названия этих ссылок записываються , в txt файл , с кодировкой UTF-8
