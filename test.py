"""
Unit tests for the Concert Itinerary Builder.

This file contains unit tests for the ItineraryBuilder class in main.py.
Participants will implement tests based on the system specifications.
"""

import unittest
from main import Concert, ItineraryBuilder
from concerts_data import get_all_concerts, SortedByDate, GetFirstConcert

class ItineraryBuilderTest(unittest.TestCase):
    """Test cases for the ItineraryBuilder class."""
    
    def setUp(self):
        """Set up for the tests."""
        self.builder = ItineraryBuilder()
        
        self.all_concerts = get_all_concerts()
        self.sorted_concerts = SortedByDate()
        self.first_concert = GetFirstConcert(artist="Taylor Swift")
    
    # ----- Manual Test Cases -----
    # Participants will implement their manual test cases here. 
    
    def test_manual_1(self):
        """First manually written test case. Sort concert by date."""

        sorted_concets = self.sorted_concerts

        all_concerts = self.all_concerts
        all_concerts.sort(key=lambda i: i.date)
        self.assertEqual(sorted_concets, all_concerts, "Concerts dates are not sorted chronologically.")

    def test_manual_2(self):
        """Second manually written test case. Get artist firt concert."""

        first_concert = self.first_concert

        all_concerts = self.all_concerts
        for concert in all_concerts:
            if concert.artist == "Taylor Swift":
                self.assertEqual(first_concert, concert, "First concert of Taylor Swift is not correct.")
                break

    # ----- AI-Assisted Test Cases -----
    # Participants will implement their AI-assisted test cases here.
    # Please name your test in a way which indicates that these are AI-assisted test cases.
    def test_ai_assisted_artist_with_multiple_concerts(self):
        """AI-assisted test: Endast den tidigaste konserten per artist ska inkluderas."""
        concerts = [
            Concert(artist="Adele", date="2025-06-01", location="London", latitude=51.5074, longitude=-0.1278),
            Concert(artist="Adele", date="2025-05-01", location="Paris", latitude=48.8566, longitude=2.3522),
        ]
        builder = ItineraryBuilder()
        itinerary = builder.build_itinerary(concerts)

        self.assertEqual(len(itinerary), 1)
        self.assertEqual(itinerary[0].artist, "Adele")
        self.assertEqual(itinerary[0].location, "Paris")

def test_ai_assisted_conflict_same_day(self):
    """AI-assisted test: Om två konserter sker samma dag, ta den närmast den senaste."""
    concerts = [
        Concert(artist="Dua Lipa", date="2025-07-01", location="Berlin", latitude=52.5200, longitude=13.4050),
        Concert(artist="Ed Sheeran", date="2025-07-01", location="Amsterdam", latitude=52.3676, longitude=4.9041),
        Concert(artist="Coldplay", date="2025-06-28", location="Brussels", latitude=50.8503, longitude=4.3517),
    ]
    builder = ItineraryBuilder()
    itinerary = builder.build_itinerary(concerts)

    self.assertEqual(len(itinerary), 2)
    artists = [c.artist for c in itinerary]
    self.assertIn("Coldplay", artists)
    self.assertTrue("Dua Lipa" in artists or "Ed Sheeran" in artists)

def test_ai_assisted_artist_with_no_concert(self):
    """AI-assisted test: Om en artist inte har några konserter ska det indikeras i resplanen."""
    concerts = [
        Concert(artist="The Weeknd", date="2025-08-10", location="Lisbon", latitude=38.7169, longitude=-9.1399),
    ]
    builder = ItineraryBuilder()
    itinerary = builder.build_itinerary(concerts, include_artists=["The Weeknd", "Beyoncé"])

    self.assertEqual(len(itinerary), 2)
    artists = [concert.artist for concert in itinerary]
    self.assertIn("The Weeknd", artists)
    self.assertIn("Beyoncé", artists)

    for concert in itinerary:
        if concert.artist == "Beyoncé":
            self.assertEqual(concert.location, "No concert available")

if __name__ == "__main__":
    unittest.main()