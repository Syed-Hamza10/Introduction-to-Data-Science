from sorting import bubble_sort, selection_sort
import unittest
class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [3, 1, 4, 2, 5]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        self.assertEqual(bubble_sort(arr), [])

    def test_single_element_array(self):
        arr = [1]
        self.assertEqual(bubble_sort(arr), [1])

class TestSelectionSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(selection_sort(arr), [1, 2, 3, 4, 5])

    def test_random_array(self):
        arr = [3, 1, 4, 2, 5]
        self.assertEqual(selection_sort(arr), [1, 2, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        self.assertEqual(selection_sort(arr), [])

    def test_single_element_array(self):
        arr = [1]
        self.assertEqual(selection_sort(arr), [1])

if __name__ == '__main__':
    unittest.main()

