# Just having Fun

def fib(n: int) -> str:
    """
    int => str

    takes in n which is the number of fibonacci
    sequence to display

    >>>fib(7)
        0 1 1 2 3 5 8
    """
    if n < 2:
        raise Exception("number should be greater than 1")

    sequence = ["0", "1"]

    if n > 2:
        for i in range(n-2):
            sequence.append( str( int(sequence[-2]) + int(sequence[-1]) ) )

    return " ".join(sequence)

print(fib(2))