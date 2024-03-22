# v1
def get_links(tags: list) -> list:
    res = []
    for el in tags:
        if el['name'] == 'img':
            res.append(el['src'])
        elif el['name'] in ('a', 'link'):
            res.append(el['href'])
    return res


# v2
tag_dict = {
    'a': 'href',
    'link': 'href',
    'img': 'src'
}


def get_links(tags: list) -> list:  # noqa E811
    res = []
    for tag in tags:
        tag_name = tag['name']
        if tag_name in tag_dict:
            res.append(tag[tag_dict[tag_name]])
    return res


""" Реализуйте функцию get_links(), которая принимает на вход список тегов,
находит среди них теги a, link и img, а затем извлекает ссылки и возвращает
список ссылок. Теги подаются на вход в виде списка, где каждый элемент это тег.
Тег имеет следующую структуру:

name — имя тега.
href или src — атрибуты. Атрибуты зависят от тега: тег img имеет атрибут src,
тег a — href, link — href.
Примеры
from solution import get_links

tags = [
  { 'name': 'img', 'src': 'hexlet.io/assets/logo.png' },
  { 'name': 'div' },
  { 'name': 'link', 'href': 'hexlet.io/assets/style.css' },
  { 'name': 'h1' },
]

links = get_links(tags)
## [
##   'hexlet.io/assets/logo.png',
##   'hexlet.io/assets/style.css'
## ] """
