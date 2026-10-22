"""Unit tests for the parse stage."""
import unittest

from scraper.parse import parse_books, _parse_price

SAMPLE_HTML = """
<html><body>
<article class="product_pod">
    <h3><a href="x" title="A Light in the Attic">A Light in the ...</a></h3>
    <p class="star-rating Three"></p>
    <div class="product_price">
        <p class="price_color">£51.77</p>
        <p class="availability">In stock</p>
    </div>
</article>
<article class="product_pod">
    <h3><a href="y" title="Tipping the Velvet">Tipping the ...</a></h3>
    <p class="star-rating One"></p>
    <div class="product_price">
        <p class="price_color">£53.74</p>
        <p class="availability">In stock</p>
    </div>
</article>
</body></html>
"""


class TestParse(unittest.TestCase):

    def test_parses_correct_number_of_books(self):
        self.assertEqual(len(parse_books(SAMPLE_HTML)), 2)

    def test_extracts_title(self):
        self.assertEqual(parse_books(SAMPLE_HTML)[0]["title"], "A Light in the Attic")

    def test_parses_price(self):
        self.assertAlmostEqual(parse_books(SAMPLE_HTML)[0]["price_gbp"], 51.77)

    def test_parses_rating(self):
        books = parse_books(SAMPLE_HTML)
        self.assertEqual(books[0]["rating"], 3)
        self.assertEqual(books[1]["rating"], 1)

    def test_in_stock_flag(self):
        self.assertTrue(parse_books(SAMPLE_HTML)[0]["in_stock"])

    def test_price_parser_handles_bad_input(self):
        self.assertIsNone(_parse_price("not a price"))


if __name__ == "__main__":
    unittest.main()
