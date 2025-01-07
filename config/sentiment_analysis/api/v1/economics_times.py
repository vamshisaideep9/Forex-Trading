import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import time

# Define the start and end dates
start_date = datetime(2014, 1, 1)  # Start date: January 1, 2014
end_date = datetime(2024, 12, 31)  # End date: December 31, 2024

def scrape_archive_for_date(date):
    """Scrapes Economic Times archive for a specific date."""
    year = date.year
    month = date.month
    day = date.day

    # Calculate starttime for the given date
    starttime_start = 41640  # Starttime for January 2014
    days_diff = (date - datetime(2014, 1, 1)).days
    starttime = starttime_start + days_diff

    # Generate the URL
    url = f"https://economictimes.indiatimes.com/archivelist/year-{year},month-{month},starttime-{starttime}.cms"
    print(f"Scraping URL: {url}")

    # Make the request
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}. HTTP Status: {response.status_code}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    articles = []

    # Extract relevant links and titles
    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        if "forex" in title.lower() or "eur/usd" in title.lower() or "currency" in title.lower():
            full_link = "https://economictimes.indiatimes.com" + link["href"]
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
    articles = scrape_archive_for_date(current_date)
    all_articles.extend(articles)
    current_date += timedelta(days=1)  # Move to the next day
    time.sleep(1)  # To avoid getting blocked

# Save the results to a CSV file
df = pd.DataFrame(all_articles)
df.to_csv("config/sentiment_analysis/data/forex_news_articles.csv", index=False)

print("Scraping complete. Data saved to forex_daily_articles.csv.")
