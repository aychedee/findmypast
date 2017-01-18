from table import multiplied_primes_table


def test_multiplied_primes_table():
    expected_table = [
        [None, 2, 3, 5],
        [2, 4, 6, 10],
        [3, 6, 9, 15],
        [5, 10, 15, 25]
    ]
    assert multiplied_primes_table(3) == expected_table
