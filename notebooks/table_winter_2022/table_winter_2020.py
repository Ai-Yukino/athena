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

# # `table_winter_2020.ipynb`
#
# <center>
#     <img src="../../images/table_winter_2022/table_winter_2022.png" style="width:60%; border-radius:2%;">
# </center>
#
# [🖼 Jéan Béller | Unsplash](https://unsplash.com/photos/yhUqpjd1F9I)
#
# ---
#
# [📝 2022 Winter Olympics medal table | Wikipedia](https://en.wikipedia.org/wiki/2022_Winter_Olympics_medal_table)

# ## 🐍 Python imports 🐍

# +
import urllib.request

import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer
# -

# ## ❄ Path variables ❄

# +
name = "table_winter_2022"

wikipedia = "https://en.wikipedia.org/wiki/"
article = "2022_Winter_Olympics_medal_table"
url = wikipedia + article

folder_html = "../../data/html/"
file_html = name + ".html"
path_html = folder_html + file_html

folder_csv = "../../data/csv/"
file_csv = name + ".csv"
path_csv = folder_csv + file_csv

folder_log = "../../data/log/"
file_log = "log_" + name + ".tsv"
path_log = folder_log + file_log
# -

# ## 🌸 `GET` request 🌸

# +
req = urllib.request.urlopen(url)

dictionary = dict(req.getheaders())
req_headers = pd.Series(dictionary)

# req_headers
columns_log = "file\treq_date\treq_last-modified\turl\n"
# -

# ## ❄ Make soup ❄

strainer = SoupStrainer(
    "table",
    {
        "class": "wikitable sortable plainrowheaders jquery-tablesorter",
        "style": "text-align:center",
    },
)
soup = BeautifulSoup(req, features="lxml", from_encoding="utf-8", parse_only=strainer)

# ## 🌸 Save `html` snippet 🌸

# + tags=[]
with open(path_html, "x", encoding="utf-8") as file:
    file.write(str(soup))
    with open(path_log, "a") as log:
        log.write(columns_log)
        log.write(
            f'{file_html}\t{req_headers["date"]}\t{req_headers["last-modified"]}\t{url}\n'
        )
        log.close()
    file.close()
# -

# ## 🌸 `html` snippet -> `DataFrame` 🌸

# ### 🌸🌸 Constructor variables

# +
table = soup.tbody

tr = table.select("tr:first-child")[0]
cols_ResultSet = tr.select("th")
cols = [e.get_text() for e in cols_ResultSet]
# -

zipped = zip(cols, [None] * len(cols))
dict_ser = dict(zipped)

# ### 🌸🌸 `Rank`

es = table.select("td:first-child")
listed = []
# es

# +
for e in es:
    if e.attrs == {}:
        listed += [e.get_text()]
    else:
        listed += int(e.attrs["rowspan"]) * [e.get_text()]
listed = [int(le) for le in listed]

ser = pd.Series(listed)
dict_ser["Rank"] = ser
# -

# ### 🌸🌸 `NOC`

es = table.select("th[scope='row']:not([colspan='2']) > a")
listed = []
# es

# +
for e in es:
    listed += [e.get_text()]

ser = pd.Series(listed)
dict_ser["NOC"] = ser
# -

# ### 🌸🌸 `Gold`

es = table.select("td:not([style='font-weight:bold']):nth-last-of-type(4)")
listed = []
# es

# +
for e in es:
    listed += [e.get_text()]
listed = [int(le) for le in listed]

ser = pd.Series(listed)
dict_ser["Gold"] = ser
# -

# ### 🌸🌸 `Silver`

es = table.select("td:not([style='font-weight:bold']):nth-last-of-type(3)")
listed = []
# es

# +
for e in es:
    listed += [e.get_text()]
listed = [int(le) for le in listed]

ser = pd.Series(listed)
dict_ser["Silver"] = ser
# -

# ### 🌸🌸 `Bronze`

es = table.select("td:not([style='font-weight:bold']):nth-last-of-type(2)")
listed = []
# es

# +
for e in es:
    listed += [e.get_text()]
listed = [int(le) for le in listed]

ser = pd.Series(listed)
dict_ser["Bronze"] = ser
# -

# ### 🌸🌸 `Total`

es = table.select("td:not([style='font-weight:bold']):nth-last-of-type(1)")
listed = []
# es

# +
for e in es:
    listed += [e.get_text()]
listed = [int(le) for le in listed]

ser = pd.Series(listed)
dict_ser["Total"] = ser
# -

# ### 🌸🌸 Construct `DataFrame`

df = pd.concat(dict_ser, axis=1)
# df

# ## ❄ Export `csv` ❄

df.to_csv(path_csv, index=False)

# ## 📚 References 📚

# ### ❄❄ Beautiful Soup
#
# - [📝 Searching by CSS class | Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=selector#searching-by-css-class)
# - [🔗 Python `bs4.SoupStrainer()` Examples | programcreek.com](https://www.programcreek.com/python/example/83291/bs4.SoupStrainer)

# ### 🌸🌸 MDN Web Docs
#
# - [📝 CSS selectors | MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)
# - [📝 Pseudo-classes | MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)
# - [📝 Pseudo-elements | MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)
