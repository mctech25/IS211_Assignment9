import requests
from bs4 import BeautifulSoup

# URL for Super Bowl Champions
url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"

# Send a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with Super Bowl champions
table = soup.find('table', class_='wikitable sortable')

if table:
    rows = table.find_all('tr')
    headers = [header.text.strip() for header in rows[0].find_all('th')]

    print("{:<10} {:<30} {:<15} {:<15} {:<30}".format(*headers))
    for row in rows[1:]:
        cols = [col.text.strip() for col in row.find_all('td')]
        if cols:
            print("{:<10} {:<30} {:<15} {:<15} {:<30}".format(*cols))
else:
    print("Could not find the table.")