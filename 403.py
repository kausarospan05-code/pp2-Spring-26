import sys

def even_generator(n):
    """
    Generator function to yield even numbers from 0 to n.
    This uses almost no memory because it produces one number
    at a time instead of storing them all.
    """
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def solve():
    # Read the input integer n
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        
        # Use a generator to print numbers separated by commas
        # without storing them in a list first.                
        is_first = True
        for num in even_generator(n):
            if not is_first:
                sys.stdout.write(",")
            sys.stdout.write(str(num))
            is_first = False
        sys.stdout.write("\n")
        
    except ValueError:
        pass

if __name__ == "__main__":
    solve()