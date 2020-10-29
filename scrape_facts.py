# %%
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

# %%
user_agent = ('Mozilla/5.0 (Windows; U; Windows NT 5.1;'
              ' en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')
headers = {'User-Agent': user_agent}

dict_urls = {'history': "https://www.thefactsite.com/100-history-facts/",
             'space': 'https://www.thefactsite.com/100-space-facts/',
             'food': 'https://www.thefactsite.com/100-random-food-facts/',
             'technology': 'https://www.thefactsite.com/top-100-technology-facts/'}

all_facts = []
all_keys = []
for key, url_val in dict_urls.items():

    request = urllib.request.Request(url_val, None, headers)
    page = urllib.request.urlopen(request)

    facts_list = [fact.text for fact in BeautifulSoup(page).findAll('h2')]

    all_facts += facts_list
    all_keys += [key]*len(facts_list)

df_facts = pd.DataFrame(
    {'fact_key': all_keys,
     'fact_text': all_facts})

df_facts.to_csv('./data/facts.csv', index=False, sep=';')