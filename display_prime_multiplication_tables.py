#!/usr/bin/env python
import sys
from table import format_table, multiplied_primes_table
error_message = (
        'You must provide a positive integer for '
        'the number of primes as the first arguemnt '
        'to this script'
    )

try:
    number_of_primes = int(sys.argv[1])
except IndexError:
    print error_message
    sys.exit(1)
except ValueError:
    print error_message
    print 'You provided "{}"'.format(sys.argv[1])
    sys.exit(1)

print format_table(multiplied_primes_table(number_of_primes))
