import unittest
from api_status_result import get_api_status 

class APITest(unittest.TestCase):
	"""test class for the api status result"""
	def test_api_result(self):
		status = get_api_status()
		self.assertEqual(status, 200)


if __name__ == '__main__': 
	unittest.main()
