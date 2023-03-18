import random
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letter_pool_list = []
    for letter in LETTER_POOL:
        for freq in range(LETTER_POOL[letter]):
            letter_pool_list.append(letter)
    letter_bank = random.sample(letter_pool_list, 10)    
    return letter_bank

def uses_available_letters(word, letter_bank):
    for letter in word:
        if letter not in letter_bank:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass