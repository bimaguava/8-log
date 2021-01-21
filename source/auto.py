import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get("https://abdullahainun.github.io")
soup = BeautifulSoup(page.content, 'html.parser')
main = soup.find(id="main")
main_juduls = main.select(".article-title")
juduls = [a.get_text() for a in main_juduls]
href = [a.get('href') for a in main_juduls]
dfBlog = pd.DataFrame({
        "judul": juduls,
        "link" : href
    })
print(dfBlog)
