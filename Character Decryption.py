#Pierre Victor T. Zurbito
#Object Oriented Programming
#BSCPE 1-4
#Polytechnic University of the Philippines
#PROBLEM 2

#Allows the user to input a certain string
input_string=input("Please input a string to decrypt:")
#String undergoes decryption
if "*" in input_string:
    string_a_decrypt=input_string.replace("*", "a")