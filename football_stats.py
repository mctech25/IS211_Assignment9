import requests
from bs4 import BeautifulSoup

# URL for CBS Sports NFL Player Statistics - Touchdowns
URL = "https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/"

# Send request to the website
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing player stats
    table = soup.find("table")
    
    if table:
        rows = table.find_all("tr")[1:21]  # Skipping header row, taking top 20

        print(f"{'Rank':<5} {'Player':<20} {'Position':<10} {'Team':<10} {'TDs':<5}")
        print("=" * 50)

        for index, row in enumerate(rows, start=1):
            cols = row.find_all("td")
            if len(cols) > 4:
                player = cols[0].text.strip()
                position = cols[1].text.strip()
                team = cols[2].text.strip()
                touchdowns = cols[3].text.strip()

                print(f"{index:<5} {player:<20} {position:<10} {team:<10} {touchdowns:<5}")
    else:
        print("Error: Could not find the stats table.")
else:
    print(f"Failed to retrieve page. Status Code: {response.status_code}")