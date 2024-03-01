import unittest
from main import find_k_largest
class TestFindKLargest(unittest.TestCase):
  def test_basic(self):
    array = [15, 7, 22, 9, 36, 2, 42, 18]
    for k in range(1, len(array)):
      kth_largest, position = find_k_largest(array, k)
      expected_largest = sorted(array, reverse=True)[k - 1]
      expected_position = len(array) - k
      self.assertEqual(kth_largest, expected_largest)
      self.assertEqual(position, expected_position)

  def test_invalid_k(self):
    array = [1, 2, 3]
    with self.assertRaises(ValueError):
      find_k_largest(array, 0)
    with self.assertRaises(ValueError):
      find_k_largest(array, len(array) + 1)

if __name__ == "__main__":
  unittest.main()
