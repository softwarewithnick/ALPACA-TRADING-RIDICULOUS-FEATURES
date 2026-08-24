import pandas as pd
import requests
from bs4 import BeautifulSoup

comb_df = pd.DataFrame()

for i in range(1966, 2027):
    # get the page html
    r = requests.get(f"https://vehiclesafetyrecalls.com/year/{i}/ford-motor-company")

    # parse the html
    soup = BeautifulSoup(r.text, "html.parser")

    # grab a couple elements of the html
    severities = soup.find_all('span', class_ = "severity-badge svelte-18kr9ml")
    subjects = soup.find_all('div', class_ = "subject svelte-18kr9ml")
    components = soup.find_all('span', class_ = "component svelte-18kr9ml")
    dates = soup.find_all('span', class_="date")

    # create a pd series of desired info
    severities = pd.Series([x.text for x in severities])
    subjects = pd.Series([x.text for x in subjects])
    components = pd.Series([x.text for x in components])
    dates = pd.Series([x.text for x in dates])

    # create DataFrame with resulting info
    df = pd.DataFrame({
        "severity" : severities.tolist(),
        "subjects" : subjects.tolist(),
        "components" : components.tolist(),
        "date" : dates.tolist()
    })

    comb_df = pd.concat([comb_df, df], ignore_index = True)



comb_df.head()

comb_df.describe()
comb_df.dtypes  


comb_df['date'] = pd.to_datetime(comb_df['date'], format="%b %d, %Y")

comb_df.to_csv('data/ford-recalls.csv', index = False)

