# import requests
# from bs4 import BeautifulSoup as BS

# file = open('test.html', encoding='utf-8')
# html = file.read()
# soup = BS(html,'html.parser')

# # conteiner = soup.find('div',{'class':'conteiner'}).find('div',{'class':'navigations-conteiner'})
# # ul_list = conteiner.find('ul',{'class':'menu'})
# # li_list = conteiner.find_all('li')
# # for li in li_list:
# #     print(li.text.strip())

# content = soup.find('div',{'class':'content-conteiner'})
# posts = content.find_all('div',{'class':'post'})
# for post_list in posts:
#     title = post_list.find('h1',{'class':'title'})
#     print(title.text.strip())