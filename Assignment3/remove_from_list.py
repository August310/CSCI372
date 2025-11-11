def remove_from_alphabet():
    guess_list = input("Enter your guessed letters with spaces inbetween: ").split()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    #we convert the guesses into a list for comparing
    guess_list = [letter.lower() for letter in guess_list]

    available = ''
    #check each letter in alphabet
    for letter in alphabets:
        #if a letter isn't part of our guess then it's still available to guess
        if letter not in guess_list:
            available += letter
    
    print("Remaining letters:", available)


print(remove_from_alphabet())