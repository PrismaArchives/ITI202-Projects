#dictionary giving each letter a scrabble point.
scrabble_points_dict = {
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1,
    'L': 1,
    'N': 1,
    'R': 1,
    'S': 1,
    'T': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10,

}

#has the user input a word
inputted_word = input("Enter your word to evaluate how many scrabble points its worth:")

#initializing the score variable for the for loop, will be the words total score at the end
score = 0

#iterates through each letter in the inputted word and checks if its in the dictionary
for letter in inputted_word: 
    if letter.upper() in scrabble_points_dict:
        score += scrabble_points_dict[letter.upper()]

#printing in a user friendly manner
print(f"For the word {inputted_word}, you recieve {score} points!")