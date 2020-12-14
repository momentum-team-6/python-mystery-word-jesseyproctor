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
import random
 
while True:
    level = input('Please select game mode. Enter "easy", "normal", or "hard": ')
    if level != "easy" and level != "Easy" and level != "normal" and level != "Normal" and level != "hard" and level != "Hard": 
        print(f'Error, "{level}" is not a game mode.')
        continue
    else:
        break

if level == 'easy' or level == 'Easy':
    easy_word = random.choice(easy_list)
    # print(easy_word)
    returned_word = easy_word
elif level == 'normal' or level == 'Normal':
    normal_word = random.choice(normal_list)
    # print(normal_word)
    returned_word = normal_word
elif level == 'hard' or level == 'Hard':
    hard_word = random.choice(hard_list)
    # print(hard_word)
    returned_word = hard_word
else:
    print(f'Error, "{level}" is not a game mode.')
#This else statement is unnecesary except to close out loop.  How do I get rid of it or what do I put in it's place?
#also, I was orginignally trying to combine if statements and while loop because I thought the the level variable I defined 
#in loop would dissapear after loop was used.  Why does this work?
print(returned_word)

#Set varaibles for game:
allowed_guesses = 8
used_guesses = 0
game_over = False
#list comprehension (values)=[(expression) for (item) in (items)]:
word_display = ['_' for letter in range(len(returned_word))]
positions = []

print(f'Guess your word one letter at a time.  Your word contains {len(returned_word)} characters.  You have 8 guesses.')

while game_over == False:
    guess = input("Enter a letter here: ").upper()
    # used_guesses +=1 #if guessed correctly this doesnt count as a guess
    for index in range(len(returned_word)):
        if guess == returned_word[index]:
            positions.append(index)
            print(f'Good job! The letter "{guess}" appears in your word.')
            for position in positions:
                word_display[position] = guess 
                print(word_display)
        else:
            used_guesses +=1
            print(f'{guess} is not a letter in your word. You have {allowed_guesses - used_guesses} remaining guesses')
            if used_guesses == allowed_guesses:
                print("Game Over")
                game_over = True
    
    print(word_display)
    
    



