# 1. Even or odd 
if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#2. Convert a Number to a String
def number_to_string(num):
    return str(num)


#3. Remove String Spaces
def no_space(x):
    x=x.replace(" ", "")
    return x

#4. Vowel Count (if you want to try a challenge with loops!) -
def get_count(sentence):
    count = 0
    vowels = "aeiouAEIOU"
    for char in sentence:
        if char in vowels:
            count += 1
    return count