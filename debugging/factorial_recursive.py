def factorial(x):
    # Edge cases
    if x < 0: return -1
    if x == 0: return 1
    
    # Exit condition - x = 1
    if x == 1:
        return x
    else:
        # Recursive part
        return x * factorial(x - 1)
