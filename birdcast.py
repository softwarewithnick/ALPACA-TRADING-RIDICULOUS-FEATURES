# ---------------------------------------------------------------- #
# PROJECT:  ALPACA-TRADING
# FILE:     Untitled-1
# PURPOSE:  What this script does
#
# AUTHOR:   Nick Amato (@softwarewithnick)
# CREATED:  2026-08-31
# MODIFIED: 2026-08-31
#
# NOTES:    -
# ---------------------------------------------------------------- #
from datetime import date, timedelta

today = date.today()
today.day


from bs4 import BeautifulSoup
import requests


r = requests.get("https://dashboard.birdcast.org/region/US-WI?night=2026-08-30")

soup = BeautifulSoup(r.content, 'html.parser')

peak_traffic_birds = soup.find_all("span", class_ = "Heading--thin")[1].text.replace(",", "")
location_birds = soup.find_all("span", class_ = "is-visuallyHidden")[1].text


