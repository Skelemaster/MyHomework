import unittest
import Leetcode1913
class TestLeetcode1913(unittest.TestCase):
    def setUp(self):
        self.obj = Leetcode1913.Solution()
    def test_maxProductDifference1(self):
        self.assertEqual(self.obj.maxProductDifference([1,2,3,4,5,6]),28)
    def test_maxProductDifference2(self):
        self.assertEqual(self.obj.maxProductDifference([1,2,3,4,5,6,7,8,9,0,1,2,1,21,23,41,2231,54,78,54,23,123,43]),274413)
    def test_maxProductDifference3(self):
        self.assertEqual(self.obj.maxProductDifference([4,4,4,4]),0)
    def test_maxProductDifference4(self):
        self.assertEqual(self.obj.maxProductDifference([1.5,2.5,2.2,5.5]),10.45)
    def test_maxProductDifference5(self):
        self.assertEqual(self.obj.maxProductDifference([123323131,-5325325,-322222,1214124214124,-9,0,-23424111]),149729474767682191169)
    def test_maxProductDifference6(self):
        self.assertEqual(self.obj.maxProductDifference([-1,-2,-3,-4,-5]),-18)
unittest.main()