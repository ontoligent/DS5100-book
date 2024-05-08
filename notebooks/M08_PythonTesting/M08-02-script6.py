# unit test case
import unittest

class TestStringMethods(unittest.TestCase):
	# test function to test equality of two value
	def test_positive(self):
		firstValue = "geeks"
		secondValue = "geeks"
		# error message in case if test case got failed
		message = "First value and second value are not equal !"
		# assertEqual() to check equality of first & second value
		self.assertEqual(firstValue, secondValue, message)

if __name__ == '__main__':
	unittest.main(verbosity=2)