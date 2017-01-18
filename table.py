from primes import primes_generator


def multiplied_primes_table(number_of_primes):
    primes = list(primes_generator(number_of_primes*3))[:number_of_primes]

    table = [
        [None] * (number_of_primes + 1)
        for _ in range(number_of_primes + 1)
    ]

    for i, prime in enumerate(primes, 1):
        table[i][0] = prime
        table[0][i] = prime

    for x, factor_x in enumerate(primes, 1):
        for y, factor_y in enumerate(primes, 1):
            table[x][y] = factor_x * factor_y

    return table


def format_table(table):
    output = '\n'
    for row in table:
        if row[0] is None:
            output += '\t|      |'
        else:
            output += '\t|'
        output += ''.join(['{: 5d} |'.format(r) if r else '' for r in row])
        output += '\n'

    return output
