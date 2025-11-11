def isGuessed(secret_word, list_of_guessed_letters):
    #runs each letter in our secret word to see if there is a match with the guessed letters
    for letter in secret_word:
        #if there is a letter that isn't guessed then we haven't guessed the word
        if letter not in list_of_guessed_letters:
            return False
    return True

print(isGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(isGuessed('apple', ['e', 'p', 'k', 'l', 'a']))