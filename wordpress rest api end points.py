from httpx import get
from pprint import pprint

# url = 'https://www.globalsqa.com/wp-json/wp/v2'
# post_api = f'{url}/posts'
# r = get(post_api)
# pprint(r.json())

url = 'https://www.globalsqa.com/wp-json/wp/v2'
pages_api = f'{url}/pages?page=4'
res = get(pages_api)
data = res.json()
for page in data:
    try:
        print(page.get('_links'))
    except:
        print("Page not found")