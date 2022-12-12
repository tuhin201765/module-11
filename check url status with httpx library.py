
import httpx
from pprint import pprint

# api_key = 'e95a66dde32f24ded84f58cf264cfa59'
# city = 'Dhaka'
# api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
#
# r= httpx.get(api)
# pprint(r.json())
url_list = [
    'https://www.dogfoodadvisor.com/best-dog-foods/best-dry-dog-foods/',
    'https://www.nbcnews.com/select/shopping/best-dog-food-ncna1189551',
    'https://www.insider.com/guides/pets/best-dog-food',
    'https://www.dogfoodadvisor.com/dog-food-reviews/brand/'
]
for url in url_list:
    r = httpx.get(url)
    text = f'{url}--------{r.status_code}'
    file = open('Link list.txt', 'a+')
    file.writelines(text +'\n')
    file.close()

file = open('Link list.txt', 'r+')
urllist = file.readlines()
file.close()
print(urllist)
    # print(url, r.status_code, sep='----')
