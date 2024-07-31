import unittest
import Leetcode13
class TestLeetcode13(unittest.TestCase):
    def setUp(self):
        self.obj = Leetcode13.Solution()
    def test_romanToInt1(self):
        self.assertEqual(self.obj.romanToInt("MCMXCIV"),1994)
    def test_romanToInt2(self):
        self.assertEqual(self.obj.romanToInt("LXXXVII"),87)
    def test_romanToInt3(self):
        self.assertEqual(self.obj.romanToInt("asfsafas"),"Неверный Ввод")
    def test_romanToInt4(self):
        self.assertEqual(self.obj.romanToInt("MMMMDCCCLXXXVIII"),4888)
    def test_romanToInt5(self):
        self.assertEqual(self.obj.romanToInt(" "),"Неверный Ввод")
unittest.main()