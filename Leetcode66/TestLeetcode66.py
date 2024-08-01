import unittest
import Leetcode66
class TestLeetcode66(unittest.TestCase):
    def setUp(self):
        self.obj = Leetcode66.Solution()
    def test_plusOne1(self):
        self.assertEqual(self.obj.plusOne([4,3,2,1]),[4, 3, 2, 2])
    def test_plusOne2(self):
        self.assertEqual(self.obj.plusOne([0]),[1])
    def test_plusOne3(self):
        self.assertEqual(self.obj.plusOne([]),"Список пуст")
    def test_plusOne4(self):
        self.assertEqual(self.obj.plusOne([4,3,2,1,2,4,7,0,5,2,1]),[4,3,2,1,2,4,7,0,5,2,2])
unittest.main()