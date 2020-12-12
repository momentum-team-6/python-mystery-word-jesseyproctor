#Prepare data from text file to be used in game:
opened_file = open("words.txt", "r")
read_file = opened_file.read().upper()
# print(type(read_file))
word_list = read_file.split()
# print(type(word_list))

#create easy, normal and hard word_lists:
#seperate all returned words in word_list in to three catogories based on length
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
level = input('Please select game mode. Enter "easy", "normal", or "hard": ')
if level == 'easy' or level == 'Easy':
    easy_word = random.choice(easy_list)
    print(easy_word)
elif level == 'normal' or level == 'Normal':
    normal_word = random.choice(normal_list)
    print(normal_word)
elif level == 'hard' or level == 'Hard':
    hard_word = random.choice(hard_list)
    print(hard_word)
else:
    print(f'Error, "{level}" is not a game mode.')

# if level != "easy" and level != "Easy" and level != "normal" and level != "Normal" and level != "hard" and level != "Hard": 
#     print(level)
# else:
#     print(f'Error, "{level}" is not a game mode.')



# #Set varaibles for game:
# allowed_guesses = 8
# used_guesses = 0
# game_over = False
# word = 
# word_display = []

# while game_over == False:
#     print(")
#     guess = input()
#     used_guesses +=1
      
#     if guess == computer_num:
#         print('You won!')
#     game_over = True
#     else:
#         print("Your guess was incorrect. You have", allowed_guesses - used_guesses, "remaining guesses")
#             if used_guesses == allowed_guesses:
#                 print("Game Over")
#                 game_over = True



