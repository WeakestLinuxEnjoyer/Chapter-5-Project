import pandas as pd
import requests
from bs4 import BeautifulSoup

def revenue(url):
	"""This function prints last 5 revenue of a company from a website."""
	# Extract .html from website URL
	html_data  = requests.get(url).text
	soup = BeautifulSoup(html_data, 'html.parser')
	table = soup.find_all("tbody")[1]

	# Reconstruct table into Pandas Dataframe
	table_revenue = pd.DataFrame(columns=["Date", "Revenue"])
	for row in table.find_all("tr"):
	    col = row.find_all("td")
	    date = col[0].text
	    revenue = col[1].text
	    new_row = pd.DataFrame({"Date": [date], "Revenue": [revenue]})
	    table_revenue = pd.concat([table_revenue, new_row], ignore_index=True)

	# Data cleanup
	table_revenue["Revenue"] = table_revenue['Revenue'].str.replace(r',|\$',"", regex=True)
	table_revenue.dropna(inplace=True)
	table_revenue = table_revenue[table_revenue['Revenue'] != ""]

	# Print last 5 row
	print(table_revenue.tail())

#Tesla revenue
# tesla_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
# revenue(tesla_url)
