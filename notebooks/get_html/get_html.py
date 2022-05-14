# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] tags=[]
# # `get_html.ipynb`
#
# <center>
#     <img src="images/html.png" style="width:60%; border-radius: 2%">
# </center>
#
# [🖼 Julia Barbosa | Unsplash](https://unsplash.com/photos/THW3r7A9sKk)
#
# ---
#
# - [List of 2020 Summer Olympics medal winners](https://en.wikipedia.org/wiki/List_of_2020_Summer_Olympics_medal_winners)
# - [List of 2022 Winter Olympics medal winners](https://en.wikipedia.org/wiki/List_of_2022_Winter_Olympics_medal_winners)
# - [List of LGBT Olympians](https://en.wikipedia.org/wiki/List_of_LGBT_Olympians)
# -

# ## 🐍 Python imports 🐍

import urllib.request
from bs4 import BeautifulSoup

# + [markdown] tags=[]
# ## 📁 Data 📁
# -

# ### ❄❄ Config variables

base_url = "https://en.wikipedia.org/wiki/"
urls = {
    "2020_medals": base_url + "List_of_2020_Summer_Olympics_medal_winners",
    "2022_medal": base_url + "List_of_2022_Winter_Olympics_medal_winners",
    "LGBT_athletes": base_url + "List_of_LGBT_Olympians",
}
base_path = "../../data/html/"
log_columns = "Request_date\tRequest_URL\n"

# ### 🌸🌸 Make log file

with open(base_path + "log.tsv", "a") as log:
    log.write(log_columns)
    log.close()

# ### ❄❄ Save HTML files and log retrieval time

for key in list(urls):
    url = urls[key]
    request = urllib.request.urlopen(url)
    soup = BeautifulSoup(request)

    with open(base_path + key + ".html", "x") as html:
        html.write(str(soup))
        with open(base_path + "log.tsv", "a") as log:
            log.write(f"{request.getheader('Date')}\t{url}\n")
            log.close()
        html.close()

# ## 📚 References 📚

# ### 🍲🍲 Beautiful Soup
#
# - [🔗 Saving content of a webpage using BeautifulSoup | Stack Overflow](https://stackoverflow.com/a/25257398)
# - [🔗 How to write the output to html file with Python BeautifulSoup | Stack Overflow](https://stackoverflow.com/a/40530238)

# ### 🐍🐼 `html.parser` + Pandas
#
# - [🔗 How to Convert HTML Tables into CSV Files in Python | PythonCode | Abdou Rockikz](https://www.thepythoncode.com/article/convert-html-tables-into-csv-files-in-python)
# - [📝 7.2. Reading and Writing Files | Python docs](https://docs.python.org/3/tutorial/inputoutput.html#tut-files)
