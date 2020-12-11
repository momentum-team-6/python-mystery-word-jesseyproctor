#Prepare data from text file to be used in game:
opened_file = open("words.txt", "r")
read_file = opened_file.read().upper()
# print(type(read_file))
word_list = read_file.split()
# print(type(word_list))

#create easy, normal and hard word_lists:
easy_list = []
normal_list = []
hard_list = []
#seperate all returned words in word_list in to three catogories based on length
#I'll need to know the length of word in wordlist
#call the function in a function where user selects easy normal or hard
def create_easy_word_list(list, new_list):
    for word in list:
        if len(word) >= 4 and len(word) <= 5:
            new_list.append(word)
        # print(new_list)
        return(new_list)

def create_normal_word_list(list, new_list):
    for word in list:
        if len(word) >= 6 and len(word) <= 8:
            new_list.append(word)
        # print(new_list)
        return(new_list)

def create_hard_word_list(list, new_list):
    for word in list:
        if len(word) > 8:
            new_list.append(word)
        # print(new_list)
        return(new_list)

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
    print(f'Error, {level} is not a game mode.')



#Computer selects random word:
# import random 
# computer_word = random.choice(word_list)
# computer_word_length = len(computer_word)
# print(computer_word)
# print(computer_word_length)


#Player chooses difficulty level:
# def select_difficulty():
#     level = input('Please select a level of difficulty. Enter "easy", "normal", or "hard": ')
#     word_length = len(computer_word)
#     while input() == 'easy' or 'Easy':

#     while input() == 'normal' or "Normal":
#     while input() == 'difficult' or 'difficult':


        

# if word_length <= 5:
#     print("Easy") 
# elif word_length > 5 and word_length <= 7:
#     #ask why the first part of line 18 is being observed without the second part
#     print("Normal")
# else:
#     print("Hard")

# #Display length of computer's word:
# print(word_length)
# #keep above print statement for user

# #Set varaibles for game:
# allowed_guesses = 8
# used_guesses = 0
# game_over = False

# # use for loop (or list comprehension) to iterate through
# #the letters in the computers word
# # while game_over == False:
# #     print(")
# #     guess = int(input())
# #     used_guesses +=1
   


