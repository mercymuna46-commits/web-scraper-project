"""Entry point — scrape N listing pages and save results."""
import time

from scraper.fetch import fetch_page
from scraper.parse import parse_books
from scraper.storage import save_to_csv, save_to_json

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
MAX_PAGES = 3
DELAY_BETWEEN_PAGES = 1.0


def run_scraper(max_pages: int = MAX_PAGES) -> list[dict]:
    """Scrape `max_pages` listing pages and return all records."""
    all_books = []
    for page in range(1, max_pages + 1):
        url = BASE_URL.format(page)
        print(f"[MAIN] Fetching page {page}: {url}")
        html = fetch_page(url)
        books = parse_books(html)
        print(f"[MAIN] Parsed {len(books)} books from page {page}")
        all_books.extend(books)
        if page < max_pages:
            time.sleep(DELAY_BETWEEN_PAGES)
    return all_books


if __name__ == "__main__":
    print("="  50)
    print("Starting web scraper...")
    print("="  50)
    books = run_scraper()
    save_to_csv(books, "output/books.csv")
    save_to_json(books, "output/books.json")
    print("="  50)
    print(f"Scraper completed. Total records: {len(books)}")
    print("="  50)
