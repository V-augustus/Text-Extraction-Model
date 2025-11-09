import random     #used to pick a random word 
from collections import Counter    #used to count letters 

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon dragonfruit kiwi gooseberry '''   #string of words 

someWords = someWords.split(' ') #split changes the string into a list 
word = random.choice(someWords)   #secret word chosen at random 

if __name__ == '__main__':    #standard
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        print('_', end=' ')   #to print empty spaces 
    print()

    letterGuessed = ''  #string where guessed letters are appended 
    chances = len(word) + 2   #no. of chances one gets to guess 
    flag = 0    #will set to 1 when player wins, exiting outer loop 

    try:
        while (chances != 0) and flag == 0:  #Flag is updated when the word is correctly guessed
            print()
            chances -= 1   #you lose a chance even before you play 

            try:
                guess = (input('Enter a letter to guess: '))     #reads user's guess
            except:
                print('Enter only a letter!')
                continue
            
            if not guess.isalpha():     #string that checks if all characters in the string are alphabets
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            
            if guess in word:
                k = word.count(guess)    #no. of times guessed letter appears 
                for _ in range(k):
                    letterGuessed += guess  

            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')     #prints correctly guessed letter 
                    
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)    #all letters guessed correctly 
                    flag = 1      #breaks out of loop 
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                
                else:
                    print('_', end=' ')

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You are out of chances! Try again')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()