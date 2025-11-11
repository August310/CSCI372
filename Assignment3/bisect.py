def bisect_square_root():
    x = float(input("Enter the number that you want to find the square root of"))
    epsilon = 0.01
    low = 0
    high = x
    #this is used to bisect our guess and divide and conquer through finding an answer
    guess = (high + low) / 2.0
    #epsilon gives us our acceptable range for error
    while abs(guess**2 - x) >= epsilon:
        #allows us to see if our guess was lower or higher
        if guess**2 < x :
            low = guess
        else:
            high = guess
        #then we cut our guess in half again too until we find our answer
        guess = (high + low) / 2.0
    
    print(guess, "is close to the square root of", x)

print(bisect_square_root())