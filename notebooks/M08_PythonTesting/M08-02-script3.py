import unittest

class TestStringMethods(unittest.TestCase):
	# test function
	def test_negative(self):
		testValue = True
		# error message in case if test case got failed
		message = "Test value is not false."
		# assetFalse() to check test value as false
		self.assertFalse( testValue, message)

if __name__ == '__main__':
	unittest.main()