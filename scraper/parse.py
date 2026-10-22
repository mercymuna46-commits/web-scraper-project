"""Parse stage: extract structured records from HTML."""
from bs4 import BeautifulSoup

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_books(html: str) -> list[dict]:
    """Extract book records from a books.toscrape.com listing page.

    Returns a list of dicts with keys:
        title, price_gbp, rating, in_stock
    """
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for card in soup.select("article.product_pod"):
        title_tag = card.select_one("h3 > a")
        title = (
            title_tag["title"].strip()
            if title_tag and title_tag.has_attr("title")
            else None
        )

        price_tag = card.select_one("p.price_color")
        price = _parse_price(price_tag.get_text(strip=True) if price_tag else "")

        rating_tag = card.select_one("p.star-rating")
        rating = None
        if rating_tag:
            for cls in rating_tag.get("class", []):
                if cls in RATING_MAP:
                    rating = RATING_MAP[cls]
                    break

        stock_tag = card.select_one("p.availability")
        in_stock = bool(stock_tag and "In stock" in stock_tag.get_text())

        if title and price is not None:
            books.append({
                "title": title,
                "price_gbp": price,
                "rating": rating,
                "in_stock": in_stock,
            })

    return books


def _parse_price(text: str) -> float | None:
    """Convert '£51.77' -> 51.77. Returns None on failure."""
    cleaned = text.replace("£", "").replace("Â", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return None
