import unittest
from unittest.mock import patch
from unittest import mock
from lectures.tests.hen_house.hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        self.henhouse = HenHouse(25)

    def test_wrong_hen_count(self):
        self.assertRaises(ValueError, lambda: self.henhouse.__init__(3))

    def test_correct_hen_count(self):
        self.assertEqual(self.henhouse.__init__(7), None)

    def test_winter(self):
        with patch('lectures.tests.hen_house.hen_class.datetime.datetime') as _mock:
            _mock.today().month = 2
            self.assertEqual(self.henhouse.season, 'winter')

    def test_summer(self):
        with patch('lectures.tests.hen_house.hen_class.datetime.datetime') as _mock:
            _mock.today().month = 8
            self.assertEqual(self.henhouse.season, 'summer')

    def test_spring(self):
        with patch('lectures.tests.hen_house.hen_class.datetime.datetime') as _mock:
            _mock.today().month = 4
            self.assertEqual(self.henhouse.season, 'spring')

    def test_autumn(self):
        with patch('lectures.tests.hen_house.hen_class.datetime.datetime') as _mock:
            _mock.today().month = 10
            self.assertEqual(self.henhouse.season, 'autumn')

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'autumn')
    def test_productivity_index(self):
        self.assertEqual(self.henhouse._productivity_index(), self.henhouse.hens_productivity.get('autumn'))

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'incorrect_season')
    def test_productivity_index_incorrect_season(self):
        self.assertRaises(ErrorTimesOfYear, lambda: self.henhouse._productivity_index())

    @patch('lectures.tests.hen_house.hen_class.HenHouse._productivity_index', mock.Mock(return_value=0.25))
    def test_get_eggs_daily_in_winter(self):
        self.assertEqual(self.henhouse.get_eggs_daily(4), 1)

    @patch('lectures.tests.hen_house.hen_class.HenHouse._productivity_index', mock.Mock(return_value=1))
    def test_get_eggs_daily_in_summer(self):
        self.assertEqual(self.henhouse.get_eggs_daily(2), 2)

    @patch('lectures.tests.hen_house.hen_class.HenHouse._productivity_index', mock.Mock(return_value=0.75))
    def test_get_eggs_daily_in_spring(self):
        self.assertEqual(self.henhouse.get_eggs_daily(8), 6)

    @patch('lectures.tests.hen_house.hen_class.HenHouse._productivity_index', mock.Mock(return_value=0.5))
    def test_get_eggs_daily_in_autumn(self):
        self.assertEqual(self.henhouse.get_eggs_daily(10), 5)

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'winter')
    def test_get_max_count_for_soup(self):
        self.assertEqual(self.henhouse.get_max_count_for_soup(3), 12)

    @patch('lectures.tests.hen_house.hen_class.HenHouse.season', 'winter')
    def test_get_max_count_for_soup_returns_zero(self):
        self.assertEqual(self.henhouse.get_max_count_for_soup(10), 0)

    def test_food_price(self):
        with patch('lectures.tests.hen_house.hen_class.requests.get') as response:
            response.return_value.status_code = 200
            self.assertIsInstance(self.henhouse.food_price(),int)

    def test_food_price_connection_error(self):
        with patch('lectures.tests.hen_house.hen_class.requests.get') as response:
            response.return_value.status_code = 1
            self.assertRaises(ConnectionError, lambda: self.henhouse.food_price())


if __name__ == '__main__':
    unittest.main()
