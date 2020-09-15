from unittest import TestCase


class Test(TestCase):
    def test_ijk(self):
        test1in = "1\n1\n1\n2"
        test1out = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        self.assertEqual(self, test1in, test1out)
        self.fail()
        
