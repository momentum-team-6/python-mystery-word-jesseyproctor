#Prepare data from text file to be used in game:
opened_file = open("words.txt", "r")
read_file = opened_file.read()
# print(type(read_file))
word_list = read_file.split()
print(type(word_list))


#Computer selects random word:
import random 
computer_word = random.choice(word_list)
print(computer_word)