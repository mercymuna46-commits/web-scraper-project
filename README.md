Web Scraper Project

A polite, resilient web scraper in Python that extracts book listings (title, price, rating, stock status) from [books.toscrape.com](https://books.toscrape.com) — a sandbox site built for scraping practice — and exports the results to CSV and JSON.

 📌 Overview

- Fetch — downloads listing pages with retry logic, timeouts, and a custom User-Agent
- Parse — extracts structured records from HTML using BeautifulSoup
- Store — writes results to both `output/books.csv` and `output/books.json`
- Polite — rate-limits requests (1 second between pages) to avoid overloading the target

 🛠️ Tools & Technologies

- Language: Python 3.10+
- Libraries: Requests, BeautifulSoup4, unittest (standard library)
- Concepts: HTTP requests, HTML parsing, retry/backoff, rate limiting, unit testing

 🚀 How to Run

```bash
git clone https://github.com/YOUR-USERNAME/web-scraper-project.git
cd web-scraper-project
pip install -r requirements.txt
python -m scraper.main
