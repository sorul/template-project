"""
Test suite for to_sum() function in src.calculator.math module.
Contains unit tests verifying correct behavior for basic usage,
edge cases with zeroes and negative numbers, and mixed positive/negative
inputs."""
import unittest

from templateproject.calculator import to_sum


class TestToSum(unittest.TestCase):
  """Unit tests for to_sum() function.

  Tests basic usage, edge cases with zeroes and negatives,
  and mixed positive/negative inputs."""

  def test_to_sum_basic(self):
    self.assertEqual(to_sum(1, 2), 3)

  def test_to_sum_zero(self):
    self.assertEqual(to_sum(0, 0), 0)

  def test_to_sum_negatives(self):
    self.assertEqual(to_sum(-1, -2), -3)

  def test_to_sum_mixed_signs(self):
    self.assertEqual(to_sum(1, -2), -1)
