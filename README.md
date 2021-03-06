FindMyPast Exercise from Hansel Dunlop
======================================

To Install requirements
=======================

    make install


To Test
=======

    make test

To print out the calculated table
=================================

   ./display_prime_multiplication_tables.py 10

    |      |    2 |    3 |    5 |    7 |   11 |   13 |   17 |   19 |   23 |   29 |
    |    2 |    4 |    6 |   10 |   14 |   22 |   26 |   34 |   38 |   46 |   58 |
    |    3 |    6 |    9 |   15 |   21 |   33 |   39 |   51 |   57 |   69 |   87 |
    |    5 |   10 |   15 |   25 |   35 |   55 |   65 |   85 |   95 |  115 |  145 |
    |    7 |   14 |   21 |   35 |   49 |   77 |   91 |  119 |  133 |  161 |  203 |
    |   11 |   22 |   33 |   55 |   77 |  121 |  143 |  187 |  209 |  253 |  319 |
    |   13 |   26 |   39 |   65 |   91 |  143 |  169 |  221 |  247 |  299 |  377 |
    |   17 |   34 |   51 |   85 |  119 |  187 |  221 |  289 |  323 |  391 |  493 |
    |   19 |   38 |   57 |   95 |  133 |  209 |  247 |  323 |  361 |  437 |  551 |
    |   23 |   46 |   69 |  115 |  161 |  253 |  299 |  391 |  437 |  529 |  667 |
    |   29 |   58 |   87 |  145 |  203 |  319 |  377 |  493 |  551 |  667 |  841 |


Areas to improve
================

The primes generator. I initially wrote it as a generator because I thought I
could create a low memory sieve solution. Halfway through I realised that a
sieve solution really needs to know its endpoint to be useful. 

Also, if I didn't write it as a generator then I wouldn't have to guess how
many primes I needed to generate in the table creating function... 

For the output, I could make it change the number of spaces it used for padding
automatically. 

For the user input I could use something like argparse to tidy up some of that code.

The prime generator could also be cached somehow between runs, maybe even storing
primes on disk.
