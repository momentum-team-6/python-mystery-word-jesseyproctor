#Prepare data from text file to be used in game:
opened_file = open("words.txt", "r")
read_file = opened_file.read()
# print(type(read_file))
word_list = read_file.split()
# print(type(word_list))


#Computer selects random word:
import random 
computer_word = random.choice(word_list)
print(computer_word)

#Player chooses difficulty level:
word_length = len(computer_word)
if word_length <= 5:
    print("Easy") 
elif word_length > 5 & word_length <= 7:
    #ask why the first part of line 18 is being observed without the second part
    print("Normal")
else:
    print("Hard")

#Display length of computer's word:
print(word_length)
#keep above print statement for user

#Set varaibles for game:
allowed_guesses = 8
used_guesses = 0
game_over = False

# use for loop (or list comprehension) to iterate through
#the letters in the computers word

