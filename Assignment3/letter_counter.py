def letter_counter():
    word = input("Please enter an english word ")
    #puts the word into lower case
    word = word.lower()
    #made a dictionary to store the letter and amounts the letter shows up
    counts = {}

    #goes letter by letter in the word
    for char in word:
        #increase the count if it's already been counted at least one time
        if char in counts:
            counts[char] += 1
        #if its the first time this letter has been found then just make it 1 for count
        else:
            counts[char] = 1
    
    #sorts the letters in alphabetical order
    #prints out our counts dictionary
    for letter in sorted(counts):
        print(letter, ":", counts[letter])

print(letter_counter())
    