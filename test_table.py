from table import multiplied_primes_table


def test_multiplied_primes_table_with_three_primes():
    expected_table = [
        [None, 2, 3, 5],
        [2, 4, 6, 10],
        [3, 6, 9, 15],
        [5, 10, 15, 25]
    ]
    assert multiplied_primes_table(3) == expected_table


def test_multiplied_primes_table_with_five_primes():
    expected_table = [
        [None, 2, 3, 5, 7, 11],
        [2, 4, 6, 10, 14, 22],
        [3, 6, 9, 15, 21, 33],
        [5, 10, 15, 25, 35, 55],
        [7, 14, 21, 35, 49, 77],
        [11, 22, 33, 55, 77, 121],
    ]

    assert multiplied_primes_table(5) == expected_table
