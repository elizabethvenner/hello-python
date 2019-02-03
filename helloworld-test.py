import unittest
from helloworld import hello


class TestHelloWorld(unittest.TestCase):


    def test_hello_world(self):
        result = hello()
        self.assertEqual(result, 'hello')


if __name__ == '__main__':
    unittest.main()