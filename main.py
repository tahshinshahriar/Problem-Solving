from __future__ import annotations

def largest_three_elements(arr: list) -> list:
    """
    Returns the three largest elements in the given list.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: A list containing the three largest elements in descending order.
    """
    arr.sort()
    return arr[-3:][::-1]


def second_largest_elem(arr: list) -> int:
    """
    Returns the second largest element in the given list.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - int: The second largest element.
    """
    arr.sort()
    return arr[-2]


def zeroes_to_end(arr: list) -> list:
    """
    Moves all occurrences of 0 to the end of the list while maintaining the order of other elements.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The modified list with 0s moved to the end.
    """
    for i in arr:
        if i == 0:
            arr.remove(i)
            arr.append(i)
    return arr


def even_greater_than_odd(arr: list) -> list:
    """
    Sorts the list such that every even-indexed element is greater than its adjacent odd-indexed element.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The modified list satisfying the condition.
    """
    for i in range(len(arr) - 1):
        if i % 2 == 0 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def rearrange(arr: list) -> list:
    """
    Rearranges the list such that every element is followed by its maximum element.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The modified list with each element followed by its maximum element.
    """
    arr.sort()
    j = len(arr) - 1
    for i in range(0, len(arr), 2):
        arr.insert(i, arr[j])
        arr.pop()
    return arr


def segregate(arr: list) -> list:
    """
    Segregates even and odd numbers in the list.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The modified list with even numbers followed by odd numbers.
    """
    j = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr


def rotation(arr: list, d: int) -> list:
    """
    Rotates the list to the left by 'd' positions.

    Parameters:
    - arr (list): The input list of integers.
    - d (int): The number of positions to rotate.

    Returns:
    - list: The modified list after left rotation.
    """
    j = 0
    while j < d:
        obj = arr[0]
        arr.remove(obj)
        arr.append(obj)
        j += 1
    return arr


def wave_sort(arr: list) -> list:
    """
    Sorts the list into a wave-like pattern.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The modified list arranged in a wave-like pattern.
    """
    arr.sort()
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def arr_sort(arr: list) -> list:
    """
    Sorts the list such that the value at each index is the index + 1.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The modified list satisfying the condition.
    """
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            arr[i] = i + 1
        i += 1
    return arr


def triangles(arr: list) -> int:
    """
    Counts the number of triangles that can be formed using elements of the list as sides.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - int: The count of triangles that can be formed.
    """
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) - 1):
            if arr[i] < (arr[j] + arr[j + 1]):
                count += 1
    return count


def bin_to_dec(bin: str) -> int:
    """
    Converts a binary string to decimal.

    Parameters:
    - bin (str): The input binary string.

    Returns:
    - int: The decimal equivalent of the binary string.
    """
    bin_len = len(bin)
    bin = bin[::-1]
    dec = 0

    for i in range(bin_len):
        if int(bin[i]) == 0:
            dec += 0
        else:
            dec += 2 ** i
    return dec

def fib_triangle(n: int) -> None:
    """
    Prints a triangle of Fibonacci numbers up to the given level.

    Parameters:
    - n (int): The number of levels in the triangle.

    Returns:
    - None
    """
    for i in range(1, n + 1):
        a = 0
        b = 1
        print('*', end="\t")
        for j in range(1, i):
            c = a + b
            a, b = b, c
            print('*', end='\t')
        print()

def armstrong_num(number: int) -> bool:
    """
    Checks if a given number is an Armstrong number.

    Parameters:
    - number (int): The input integer.

    Returns:
    - bool: True if the number is an Armstrong number, False otherwise.
    """
    num = str(number)
    num_len = len(num)
    num_sum = 0
    for i in range(num_len):
        num_sum += int(num[i]) ** num_len
    return num_sum == number

def fib(n: int) -> int:
    """
    Returns the nth Fibonacci number.

    Parameters:
    - n (int): The index of the desired Fibonacci number.

    Returns:
    - int: The nth Fibonacci number.
    """
    a = 0
    b = 1
    for i in range(2, n + 1):
        nth_fib = a + b
        a, b = b, nth_fib
    return nth_fib

def gcdd(num1: int, num2: int) -> int:
    """
    Returns the greatest common divisor (GCD) of two numbers.

    Parameters:
    - num1 (int): The first integer.
    - num2 (int): The second integer.

    Returns:
    - int: The GCD of the two input integers.
    """
    divisor = num2 if num1 > num2 else num1
    dividend = num1 if num1 > num2 else num2
    rem = 0
    while rem != 1:
        rem = dividend % divisor
        if rem == 0:
            return divisor
        dividend, divisor = divisor, rem
    return None

def plusMinus(arr: list) -> None:
    """
    Prints the ratios of positive, negative, and zero elements in the array.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - None
    """
    n = len(arr)
    pos_count = 0
    neg_count = 0
    zero_count = 0

    for i in range(n):
        if arr[i] > 0:
            pos_count += 1
        elif arr[i] < 0:
            neg_count += 1
        else:
            zero_count += 1
    print("{:.6f}".format(pos_count / n))
    print("{:.6f}".format(neg_count / n))
    print("{:.6f}".format(zero_count / n))

def miniMaxSum(arr: list) -> None:
    """
    Prints the minimum and maximum possible sums of 4 out of 5 elements in the array.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - None
    """
    min_sum = 1000000
    max_sum = -1
    for i in range(len(arr)):
        curr_sum = arr[i]
        j = i + 1
        while j > i:
            curr_sum += arr[j]
            j += 1
            if j == len(arr) - 1:
                j = 0
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < min_sum:
            min_sum = curr_sum
    print(min_sum, " ", max_sum)

def timeConversion(s: str) -> str:
    """
    Converts a 12-hour time format to a 24-hour time format.

    Parameters:
    - s (str): The input time string in 12-hour format.

    Returns:
    - str: The time string in 24-hour format.
    """
    am_pm = s[-2:]
    hour = s[0:2]
    if am_pm == 'AM':
        hour = int(hour) % 12
        if len(str(hour)) == 1:
            hour = '0' + str(hour)
    else:
        hour = 12 + int(hour) % 12
    return f"{hour}{s[2:len(s) - 2]}"

def matchStrings(str1: str, str2: str) -> list:
    """
    Counts the occurrences of each character in str2 within str1.

    Parameters:
    - str1 (str): The input string.
    - str2 (str): The substring.

    Returns:
    - list: A list containing the count of occurrences for each character in str2 within str1.
    """
    count = [0] * (len(str2) - 1)
    for i in range(1, len(str2)):
        for j in range(1, len(str1)):
            if str2[i] == str1[j]:
                count[i - 1] += 1
    return count


def unique_elem(arr: list) -> int:
    """
    Finds and returns the unique element in the given list.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - int: The unique element in the list.
    """
    for i in range(len(arr)):
        count = arr.count(arr[i])
        if count == 1:
            return arr[i]


def flippingBits(n: int) -> int:
    """
    Flips the bits of the given integer.

    Parameters:
    - n (int): The input integer.

    Returns:
    - int: The result after flipping the bits.
    """
    binary = bin(n)
    binary = binary[2:].zfill(32)
    binary = list(binary)

    for i in range(len(binary)):
        if binary[i] == "0":
            binary[i] = "1"
        else:
            binary[i] = "0"
    binary = "".join(binary)
    return int(binary, 2)


def abs_diff(arr: list) -> int:
    """
    Calculates the absolute difference between the sums of the diagonals in a square matrix.

    Parameters:
    - arr (list): The input square matrix.

    Returns:
    - int: The absolute difference between the sums of diagonals.
    """
    lsum = 0
    rsum = 0
    for i in range(len(arr)):
        for j in range(i, i + 1):
            lsum += arr[i][j]
    for i in range(len(arr)):
        for j in range(len(i) - 1,):
            rsum += arr[i][j]
    return abs(lsum - rsum)


def countingSort(arr: list) -> list:
    """
    Performs counting sort on the given list.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - list: The sorted list using counting sort algorithm.
    """
    upper_bound = max(arr) + 1
    count_arr = [0] * upper_bound
    for i in range(len(count_arr)):
        count_arr[i] = arr.count(i)
    return count_arr


def missingNums(arr: list) -> int:
    """
    Finds the missing number in a sequence.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - int: The missing number in the sequence.
    """
    n = max(arr)
    total_sum = (n * (n + 1)) / 2
    arr_sum = sum(arr)
    return int(total_sum - arr_sum)


def repeatingNum(arr: list) -> list:
    """
    Finds and returns the first repeating number in the given list.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - int: The first repeating number in the list.
    """
    temp = sorted(arr)
    for i in range(len(arr)):
        count = temp.count(arr[i])
        if count > 1:
            return arr[i]


def sum_close_to_zero(arr: list) -> str:
    """
    Finds and returns a pair of elements whose sum is closest to zero in the given list.

    Parameters:
    - arr (list): The input list of integers.

    Returns:
    - str: A string representation of the pair of elements whose sum is closest to zero.
    """
    arr.sort()
    ls = 0
    rs = len(arr) - 1
    min_sum = 100000

    while ls < rs:
        curr_sum = abs(arr[ls] + arr[rs])
        if curr_sum < min_sum:
            min_sum = curr_sum
            elem1, elem2 = arr[ls], arr[rs]
        if curr_sum > 0:
            rs -= 1
        if curr_sum < 0:
            ls += 1
    return f"Pairs : {elem1}, {elem2}"


def find_pair(arr: list, diff: int) -> str:
    """
    Finds a pair of elements in the given list whose absolute difference is equal to the specified value.

    Parameters:
    - arr (list): The input list of integers.
    - diff (int): The target absolute difference.

    Returns:
    - str: A string representation of the pair of elements or "No pairs found" if no such pair exists.
    """
    diff = abs(diff)
    arr.sort()
    ls = 0
    rs = len(arr) - 1
    while ls < rs:
        current_diff = abs(arr[ls] - arr[rs])
        if current_diff == diff:
            return f"{arr[ls]}, {arr[rs]}"
        elif current_diff > diff:
            ls += 1
        else:
            rs -= 1
    return "No pairs found"


def romanToInt(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.

    Parameters:
    - s (str): The input Roman numeral string.

    Returns:
    - int: The integer equivalent of the Roman numeral.
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = s.count('IV') * 4 + s.count('IX') * 9 + s.count('XL') * 40 + s.count('XC') * 90 + s.count('CD') * 400 + s.count('CM') * 900
    s = s.replace('IV', "").replace('IX', "").replace('XL', "").replace('XC', "").replace('CD', "").replace('CM', "")
    for char in s:
        num += roman_dict[char]
    return num


def findCommonPrefix(arr: list) -> str:
    """
    Finds the common prefix among a list of strings.

    Parameters:
    - arr (list): The input list of strings.

    Returns:
    - str: The common prefix among the strings.
    """
    if not arr:
        return ""

    result_set = set(arr)
    if len(result_set) == 1:
        return arr[0]

    result = []
    j = 0

    while True:
        i = 0
        result_set = set()
        while i < len(arr):
            if j < len(arr[i]):
                result_set.add(arr[i][j])
            i += 1

        if len(result_set) > 1:
            return "".join(result)
        else:
            result.append(result_set.pop())
            j += 1
