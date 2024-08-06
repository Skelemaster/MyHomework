import unittest
import ChetnoeSort
class TestChetnoeSort(unittest.TestCase):
    def setUp(self):
        self.obj = ChetnoeSort.Solution()
    def test_chetnoesort1(self):
        self.assertEqual(self.obj.ChetnoeSort([1, 10, 3, 4, 5, 8]),[1, 4, 3, 8, 5, 10])
    def test_chetnoesort2(self):
        self.assertEqual(self.obj.ChetnoeSort([-1, -10, -3, -4, -5, -8]),[-1, -10, -3, -8, -5, -4])
    def test_chetnoesort3(self):
        self.assertEqual(self.obj.ChetnoeSort([]),[]) 
    def test_chetnoesort4(self):
        self.assertEqual(self.obj.ChetnoeSort([113212, 102221, 346457, 4121234, 51829730128, -8213091230]),[-8213091230, 102221, 346457, 113212, 4121234, 51829730128])
unittest.main()