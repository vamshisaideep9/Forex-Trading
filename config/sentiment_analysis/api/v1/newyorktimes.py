import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import time

# Define the start and end dates
start_date = datetime(2018, 1, 2)  # Start date: January 1, 2014
end_date = datetime(2019, 1, 1)  # End date: January 1, 2024

def scrape_nyt_for_date(date):
    """Scrapes New York Times archive for a specific date."""
    # Format the date to match NYT URL structure
    year = date.year
    month = date.month
    day = date.day
    
    # Generate the URL for the given date
    url = f"https://archive.nytimes.com/www.nytimes.com/indexes/{year}/{month:02d}/{day:02d}/todayspaper/index.html"
    print(f"Scraping URL: {url}")

    # Make the request
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}. HTTP Status: {response.status_code}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    articles = []

    # Extract relevant article links from the page
    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        # Filter for articles related to forex or currency
        if "forex" in title.lower() or "currency" in title.lower() or "exchange rate" in title.lower() or "EUR/USD" in title.lower():   
            full_link = link["href"]
            if full_link.startswith('/'):
                full_link = f"https://archive.nytimes.com{full_link}"
            articles.append({
                "date": date.strftime("%Y-%m-%d"),
                "title": title,
                "link": full_link
            })

    return articles

# Iterate over each date from start_date to end_date
current_date = start_date
all_articles = []

while current_date <= end_date:
    articles = scrape_nyt_for_date(current_date)
    all_articles.extend(articles)
    current_date += timedelta(days=1)  # Move to the next day
    time.sleep(1)  # To avoid getting blocked

# Save the results to a CSV file
df = pd.DataFrame(all_articles)
df.to_csv("config/sentiment_analysis/data/newyorktimes_forex_articles_5.csv", index=False)

print("Scraping complete. Data saved to nytimes_forex_articles.csv.")
