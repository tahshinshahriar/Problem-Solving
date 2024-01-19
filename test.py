import unittest
from main import (
    largest_three_elements,
    second_largest_elem,
    zeroes_to_end,
    even_greater_than_odd,
    rearrange,
    segregate,
    rotation,
    wave_sort,
    arr_sort,
    triangles,
    dec_to_bin,
    bin_to_dec,
    fib_triangle,
    armstrong_num,
    fib,
    gcdd,
    plusMinus,
    miniMaxSum,
    timeConversion,
    matchStrings,
    unique_elem,
    flippingBits,
    abs_difff,
    countingSort,
    repeatingNum,
    missingNums,
    sum_close_to_zero,
    romanToInt,
    find_pair,
    findCommonPrefix
)

class TestYourFunctions(unittest.TestCase):

    def test_largest_three_elements(self):
        self.assertEqual(largest_three_elements([5, 2, 8, 1, 7]), [5, 2, 8])
        self.assertEqual(largest_three_elements([10, 20, 30, 40, 50]), [30, 40, 50])

    def test_second_largest_elem(self):
        self.assertEqual(second_largest_elem([5, 2, 8, 1, 7]), 7)
        self.assertEqual(second_largest_elem([10, 20, 30, 40, 50]), 40)

    def test_zeroes_to_end(self):
        self.assertEqual(zeroes_to_end([0, 2, 0, 1, 7]), [2, 1, 7, 0, 0])
        self.assertEqual(zeroes_to_end([10, 20, 30, 0, 50]), [10, 20, 30, 50, 0])

    def test_even_greater_than_odd(self):
        self.assertEqual(even_greater_than_odd([5, 2, 8, 1, 7]), [2, 5, 1, 8, 7])
        self.assertEqual(even_greater_than_odd([10, 20, 30, 40, 50]), [20, 10, 40, 30, 50])

    def test_rearrange(self):
        self.assertEqual(rearrange([5, 2, 8, 1, 7]), [7, 1, 5, 2, 8])
        self.assertEqual(rearrange([10, 20, 30, 40, 50]), [50, 10, 40, 20, 30])

    def test_segregate(self):
        self.assertEqual(segregate([1, 2, 3, 4, 5]), [1, 3, 5, 2, 4])
        self.assertEqual(segregate([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])

    def test_rotation(self):
        self.assertEqual(rotation([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
        self.assertEqual(rotation([10, 20, 30, 40, 50], 3), [40, 50, 10, 20, 30])

    def test_wave_sort(self):
        self.assertEqual(wave_sort([1, 2, 3, 4, 5]), [2, 1, 4, 3, 5])
        self.assertEqual(wave_sort([10, 20, 30, 40, 50]), [20, 10, 40, 30, 50])

    def test_arr_sort(self):
        self.assertEqual(arr_sort([1, 3, 2, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(arr_sort([10, 20, 30, 40, 50]), [1, 2, 3, 4, 5])

    def test_triangles(self):
        self.assertEqual(triangles([3, 4, 5, 7]), 2)
        self.assertEqual(triangles([10, 20, 30, 40, 50]), 0)

    def test_dec_to_bin(self):
        self.assertEqual(dec_to_bin(10), '1010')
        self.assertEqual(dec_to_bin(25), '11001')
        self.assertEqual(dec_to_bin(0), '0')

    def test_bin_to_dec(self):
        self.assertEqual(bin_to_dec('1010'), 10)
        self.assertEqual(bin_to_dec('11001'), 25)
        self.assertEqual(bin_to_dec('0'), 0)

    def test_armstrong_num(self):
        self.assertTrue(armstrong_num(153))
        self.assertFalse(armstrong_num(123))
        self.assertTrue(armstrong_num(9474))
        
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)

    def test_gcdd(self):
        self.assertEqual(gcdd(24, 18), 6)
        self.assertEqual(gcdd(35, 14), 7)
        self.assertEqual(gcdd(45, 60), 15)

    def test_timeConversion(self):
        self.assertEqual(timeConversion('07:05:45PM'), '19:05:45')
        self.assertEqual(timeConversion('12:00:00AM'), '00:00:00')

    def test_matchStrings(self):
        self.assertEqual(matchStrings("hello", "he"), [1, 1])

    def test_unique_elem(self):
        self.assertEqual(unique_elem([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]), None)
        self.assertEqual(unique_elem([1, 2, 3, 4, 5, 6, 7, 8, 9]), 1)

    def test_flippingBits(self):
        self.assertEqual(flippingBits(10), 4294967285)
        self.assertEqual(flippingBits(0), 4294967295)

    def test_countingSort(self):
        self.assertEqual(countingSort([4, 2, 2, 8, 3, 3, 1]), [0, 1, 2, 2, 1, 0, 0, 1, 1])

    def test_missingNums(self):
        self.assertEqual(missingNums([1, 2, 4, 6, 3, 7, 8]), 5)
        self.assertEqual(missingNums([10, 7, 5, 3, 2, 1, 0]), 4)

    def test_repeatingNum(self):
        self.assertEqual(repeatingNum([1, 2, 3, 4, 2, 5]), 2)
        self.assertEqual(repeatingNum([1, 2, 3, 4, 5]), None)
    def test_sum_close_to_zero(self):
        self.assertEqual(sum_close_to_zero([1, 5, -10, 8, -6]), "Pairs : -6, 5")
        self.assertEqual(sum_close_to_zero([2, 7, -5, 4, 11, -3]), "Pairs : -3, 4")

    def test_find_pair(self):
        self.assertEqual(find_pair([1, 7, 5, 3, 2, 9, 8], 2), "No pairs found")
        self.assertEqual(find_pair([4, 3, 2, 1, 5, 6], 2), "1, 3")

    def test_romanToInt(self):
        self.assertEqual(romanToInt("III"), 3)
        self.assertEqual(romanToInt("IX"), 9)
        self.assertEqual(romanToInt("LVIII"), 58)
        self.assertEqual(romanToInt("MCMXCIV"), 1994)

    def test_findCommonPrefix(self):
        self.assertEqual(findCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(findCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(findCommonPrefix(["apple", "ape", "april"]), "ap")


if __name__ == '__main__':
    unittest.main()
