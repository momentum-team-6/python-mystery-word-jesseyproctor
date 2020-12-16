import random

#wrap entire thing in game play functiom to start it over when game__over equals true (call game play function in while loop when game_over == true)

#Prepare data from text file to be used in game:
opened_file = open("words.txt", "r")
read_file = opened_file.read().upper()
# print(type(read_file))
word_list = read_file.split()
# print(word_list)

# create easy, normal and hard word_lists:
# seperate all returned words in word_list in to three catogories based on length
def create_easy_word_list(list):
    new_list = []
    for word in list:
        if len(word) >= 4 and len(word) <= 5:
            new_list.append(word)
    # print(new_list)
    return(new_list)

def create_normal_word_list(list):
    new_list = []
    for word in list:
        if len(word) >= 6 and len(word) <= 8:
            new_list.append(word)
    # print(new_list)
    return(new_list)

def create_hard_word_list(list):
    new_list = []
    for word in list:
        if len(word) > 8:
            new_list.append(word)
    # print(new_list)
    return(new_list)

easy_list = create_easy_word_list(word_list)
normal_list = create_normal_word_list(word_list)
hard_list = create_hard_word_list(word_list)

#Player chooses difficulty level and computer selects word:
 
def get_word(level):
    word_dict = {
        "easy":random.choice(easy_list),
        "normal":random.choice(normal_list),
        "hard":random.choice(hard_list)
    }
    return word_dict[level]
    
while True:
    level = input('Please select game mode. Enter "easy", "normal", or "hard": ').lower()
    if level != "easy" and level != "normal" and level != "hard": 
        print(f'Error, "{level}" is not a game mode.')
        continue
    else:
        break

# if level == 'easy':
#     easy_word = random.choice(easy_list)
#     # print(easy_word)
#     returned_word = easy_word
# elif level == 'normal':
#     normal_word = random.choice(normal_list)
#     # print(normal_word)
#     returned_word = normal_word
# elif level == 'hard':
#     hard_word = random.choice(hard_list)
#     # print(hard_word)
#     returned_word = hard_word
# else:
#     print(f'Error, "{level}" is not a game mode.')
returned_word = get_word(level) 
print(returned_word)  

# print(returned_word)

#Set varaibles for game:
allowed_guesses = 8
used_guesses = 0
game_over = False
#list comprehension (values)=[(expression) for (item) in (items)]:
word_display = ['_' for letter in range(len(returned_word))]
returned_word_list = list(returned_word)

print(f'Guess your word one letter at a time.  Your word contains {len(returned_word)} letters.  You have 8 guesses.')

#Game Play:
while game_over == False:
    guess = input("Enter a letter here: ").upper()
    # store each index that the guess occurs at
    # resets with each guess (b/c while loop):
    guess_indices = []

    for index in range(len(returned_word)):
        if guess == returned_word[index]:
            guess_indices.append(index)
            
    if len(guess_indices) > 0:
        print(f'Good job! The letter "{guess}" appears in the word.')
        # Replace index in word display with guess:
        for i in guess_indices:
            word_display[i] = guess
        print(word_display)
        if word_display == returned_word_list:
            game_over == True
            print(f'{returned_word} is the word.  You win!')

    else:
        used_guesses +=1
        print(f'{guess} is not a letter in the word. You have {allowed_guesses - used_guesses} remaining guesses')
        if used_guesses == allowed_guesses:
            game_over = True
            print(f'You are out of guesses.  The word was {returned_word}.  Better luck next time!')
    
   

            
                
    

    
    



