import unittest
from main import find_k_largest
class TestFindKthLargest(unittest.TestCase):
  def test_kth_largest(self):
    array = [15, 7, 22, 9, 36, 2, 42, 18]

    for k in range(1, len(array) + 1):
      expected_value = sorted(array, reverse=True)[k-1]
      expected_index = len(array) - k

      actual_value, actual_index = find_k_largest(array, k)

      self.assertEqual(expected_value, actual_value)
      self.assertEqual(expected_index, actual_index)

if __name__ == "__main__":
  unittest.main()