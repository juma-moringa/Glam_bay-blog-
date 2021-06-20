import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
       
        self.random_quote = Quote( "Itsjay again","Why always me each time tommorow might be be the best time ever")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        self.assertEqual(self.random_quote.author,"Itsjay again" )
        self.assertEqual(self.random_quote.quote,"Why always me each time tommorow might be be the best time ever")