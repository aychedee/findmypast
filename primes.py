from collections import defaultdict


def primes_generator(limit):
    primes = defaultdict(lambda: True)
    primes[0], primes[1] = False, False

    for candidate in range(limit):
        if primes[candidate]:
            yield candidate

            for i in range(candidate*candidate, limit, candidate):
                primes[i] = False
