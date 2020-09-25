from unittest import TestCase
from MaximizeIt import MaximizeIt, maxing


class TestMaximizeIt(TestCase):

    def test_MaximizeitInstantiation(self):
        foo = open("MaximizeItTest.txt")
        m = MaximizeIt(foo.read())
        self.assertIsNotNone(m)
        foo.close()

    def test_parse_input(self):
        foo = open("MaximizeItTest.txt")
        some_input = foo.read()
        m = MaximizeIt(some_input)
        input = m.parse_input(some_input)
        output = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]], 1000
        self.assertEqual(input, output)
        foo.close()

    def test_slice_input(self):
        foo = open("MaximizeItTest.txt")
        some_input = foo.read()
        m = MaximizeIt(some_input)
        listin = [[2, 5, 4], [2, 1, 3]]
        listout = m.slice_input(listin)
        result = [(5, 1), (5, 3), (4, 1), (4, 3)]
        self.assertEqual(listout, result)
        foo.close()

    def test_totaling(self):
        foo = open("MaximizeItTest.txt")
        some_input = foo.read()
        m = MaximizeIt(some_input)
        slicein = m.totaling([2, 2, 2], 2)
        self.assertEqual(slicein, 0)
        foo.close()

    def test_is_biggest(self):
        foo = open("MaximizeItTest.txt")
        some_input = foo.read()
        m = MaximizeIt(some_input)
        biggestin = m.is_biggest(15)
        self.assertEqual(biggestin, 15)
        foo.close()


class Test(TestCase):
    def test_maxing(self):
        foo = maxing("MaximizeItTest.txt")
        self.assertEqual(foo, 206)