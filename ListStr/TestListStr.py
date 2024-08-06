import unittest
import ListStr
class TestListStrInt(unittest.TestCase):
    def setUp(self):
        self.obj = ListStr.Solution()
    def test_ListStr1(self):
        self.assertEqual(self.obj.ListStr(["Mary", "Gary", "Harry"],[2, 3, 1]), ["Gary", "Harry", "Mary"])
    def test_ListStr2(self):
        self.assertEqual(self.obj.ListStr(["Mary", "Gary", "Harry","Max","Maex","Maxx","Macx","Maxim"], [8, 3, 1, 6, 4, 5, 7, 2]),['Maxim', 'Harry', 'Mary', 'Maxx', 'Max', 'Maex', 'Macx', 'Gary'])
    def test_ListStr3(self):
        with self.assertRaises(Exception):
            self.assertEqual(self.obj.ListStr([],[1]))
unittest.main()