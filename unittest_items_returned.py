import unittest
from hn_items_returned import top_items_returned

class TestItemsReturned(unittest.TestCase):
	"""testing the number of results from the top hn items"""
	def test_hn_top_items(self):
		top_item_count = top_items_returned()
		indicator = top_item_count < 500
		self.assertTrue(indicator)


if __name__ == '__main__': 
	unittest.main()


