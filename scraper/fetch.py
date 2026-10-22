"""Fetch stage: retrieve HTML from a URL with retries and rate limiting."""
import time

import requests

USER_AGENT = "Mozilla/5.0 (compatible; PortfolioScraper/1.0)"
DEFAULT_DELAY = 1.0   seconds between retries


def fetch_page(url: str, retries: int = 3, delay: float = DEFAULT_DELAY) -> str:
    """Fetch HTML from a URL, retrying on transient failures.

    Args:
        url: Target URL.
        retries: Number of attempts before giving up.
        delay: Seconds to wait between attempts.

    Returns:
        HTML content as a string.

    Raises:
        RuntimeError: If all attempts fail.
    """
    headers = {"User-Agent": USER_AGENT}
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:
            last_error = exc
            print(f"[FETCH] Attempt {attempt}/{retries} failed for {url}: {exc}")
            if attempt < retries:
                time.sleep(delay)

    raise RuntimeError(f"Failed to fetch {url} after {retries} attempts: {last_error}")
