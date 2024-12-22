FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

score = int(input())
def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    #"*** YOUR CODE HERE ***"
    pi = pi // pow(10, 100 - score) #开始没有读题，错误地认为pi是3.14159...
    # END PROBLEM 2
    return pi % 10 + 3
n = free_bacon(score)
print(n)