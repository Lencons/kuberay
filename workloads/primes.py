""" Calculate Prime Numbers

Calculate a set of prime nnumbers using a variety of different algorithms
across a Ray cluster.

"""
import argparse
import ray
import math
import timeit

@ray.remote(num_cpus=1)
def sieve_eratosthenes(limit : int) -> dict:
    """Generates a sequence of primes < n.

    Uses the full sieve of Eratosthenes with O(n) memory.

    Parameters
    ----------
    limit : int
        Number to calculate pimes up too..

    Returns
    -------
    dict
        Dictonary containing a processing information message in 'info' and
        a list of all the calculated prime numbers.

    """
    start_time = timeit.default_timer()

    sieve = [True] * limit
    sqrtn = int(math.ceil(math.sqrt(limit)))

    for i in range(2, sqrtn):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    primes = []
    for p in range(2, len(sieve)):
        if sieve[p] : primes.append(p)

    return {
        'info': f'Sieve of Eratosthenes: {len(primes)} primes, {timeit.default_timer() - start_time:.2f} seconds.',
        'primes': primes,
    }


@ray.remote(num_cpus=1)
def sieve_sundaram(limit : int) -> dict:
    """Generate prime numbers using the Sieve of Sundaram.
    
    Parameters
    ----------
    limit : int
        Number to calculate pimes up too..

    Returns
    -------
    dict
        Dictonary containing a processing information message in 'info' and
        a list of all the calculated prime numbers.
    """
    start_time = timeit.default_timer()

    k = math.floor((limit - 1) / 2)

    sieve = [True] * (k + 1)
      
    for i in range(1, int(math.ceil(math.sqrt(k)))):
        j = i
        while ((i + j + 2 * i * j) <= k):
            sieve[i + j + 2 * i * j] = False
            j += 1

    primes = [ ]
    for p in range(len(sieve)):
        if sieve[p] : primes.append(p)

    return {
        'info': f'Sieve of Sundaram: {len(primes)} primes, {timeit.default_timer() - start_time:.2f} seconds.',
        'primes': primes,
    }


@ray.remote(num_cpus=1)
def sieve_atkin(limit : int) -> dict:
    """Generate prime numbers using the Sieve of Atkin.
    
    The algorithm creates a sieve of prime numbers smaller than 60 except for
    2, 3, 5. Then, it divides the sieve into 3 separate subsets. After that,
    using each subset, it marks off the numbers that are solutions to some
    particular quadratic equation and that have the same modulo-sixty remainder
    as that particular subset. In the end, it eliminates the multiples of
    square numbers and returns 2, 3, 5 along with the remaining ones.
    The result is the set of prime numbers smaller than n.
    
    Parameters
    ----------
    limit : int
        Number to calculate pimes up too..

    Returns
    -------
    dict
        Dictonary containing a processing information message in 'info' and
        a list of all the calculated prime numbers.
    """
    start_time = timeit.default_timer()

    sieve=[False] * (limit + 1)

    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n%12 == 1 or n%12 == 5) : sieve[n] = not sieve[n]
            n = 3 * x**2 + y**2
            if n <= limit and n%12 == 7 : sieve[n] = not sieve[n]
            n = 3 * x**2 - y**2
            if x > y and n <= limit and n%12 == 11 : sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit + 1, x**2):
                sieve[y] = False

    primes = [2, 3]
    for p in range(5, limit):
        if sieve[p] : primes.append(p)

    return {
        'info': f'Sieve of Atkin: {len(primes)} primes, {timeit.default_timer() - start_time:.2f} seconds.',
        'primes': primes,
    }


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='primes',
        description='Prime number generator.',
    )

    # Program configuration arguments.
    parser.add_argument(
        '-d', '--dump',
        action='store_true',
        help='dump prime numbers from job'
    )
    parser.add_argument(
        '-m', '--max',
        type=int,
        default=None,
        help='value to search up to for primes (in millions)'
    )
    parser.add_argument(
        '-n', '--num',
        type=int,
        default=None,
        help='number of instances of each prime calculator'
    )
    parser.add_argument(
        '-r', '--ray',
        default=None,
        help='Ray cluster client connection URL',
    )

    # Environment configuration arguments.
    parser.add_argument(
        '--test',
        action='store_true',
        help='use settings for test environments'
    )

    # Processing configuration arguments.
    parser.add_argument(
        '--eratosthenes',
        action='store_true',
        help='calulate primes using the sieve of Eratosthenes',
    )
    parser.add_argument(
        '--sundaram',
        action='store_true',
        help='calculate primes using the sieve of Sundaram',
    )
    parser.add_argument(
        '--atkin',
        action='store_true',
        help='calculate primes using the sieve of Atkin'
    )
    args = parser.parse_args()

    if args.ray is None:
        ray.init()
    else:
        print(f'Connecting to remote cluster: {args.ray}')
        ray.init(args.ray)

    # Set environment based processing parameters
    if args.test:
        # Parameters to work with raycluster-test manifests.
        test_max = 250
        if args.max is not None:
            if args.max > test_max:
                print(f'Setting max prime to test environment limit: {test_max}')
                args.max = test_max
        else:
            args.max = test_max

        # Workers will have two CPU's each, limit one job per worker.
        #sieve_eratosthenes.options(num_cpus=2)
        #sieve_sundaram.options(num_cpus=2)
        #sieve_atkin.options(num_cpus=2)

    # Set default parameters for anything not specificly set
    if args.max is None : args.max = 500
    if args.num is None : args.num = 1

    limit = args.max * 1000000
    futures = []

    # Calculate memory requirements for sieves as they are very memory hungry.
    sieve_eratosthenes.options(memory=limit * 1.1)
    sieve_sundaram.options(memory=int(limit / 2) * 1.1)
    sieve_atkin.options(memory=limit * 1.1)

    # For the number of requested algorithm instances, run the selected
    # algorithms.
    for i in range(args.num):
        if args.eratosthenes:
            futures.append(sieve_eratosthenes.remote(limit))
        if args.sundaram:
            futures.append(sieve_sundaram.remote(limit))
        if args.atkin:
            futures.append(sieve_atkin.remote(limit))

    # If specific algorithms haven't been selected on the command line, run
    # them all.
    if len(futures) == 0:
        for i in range(args.num):
            futures += [
                sieve_eratosthenes.remote(limit),
                sieve_sundaram.remote(limit),
                sieve_atkin.remote(limit),
            ]

    for result in ray.get(futures):
        print(result['info'])
        if args.dump : print(result['primes'])
