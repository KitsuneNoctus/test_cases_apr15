'''
Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a
repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

    lumberjacks
    background
    downstream
    six-year-old

The word isograms, however, is not an isogram, because the s repeats.

Pseudo:
- function takes in a string
- Create a new list
- Loop through the string
-- if character is in the new list
--- return False
-- else:
--- append character to the new list
- return True
'''

def is_isogram(text):
    ''' Check if a string is an isogram (no letters repeat)'''
    # for edges Cases --- if letters repeat, but have different casing, without .lower(), it returns True
    # text = text.lower()
    # Edge case of no text at all
    # if text == "":
    # return False
    #-
    list = []
    for char in text:
        if char in list:
            return False
        else:
            list.append(char)
    return True

#Good Test cases
print("Good Tests")
print(is_isogram("lumberjacks"))
print(is_isogram("background"))
print(is_isogram("isograms"))
#
# #Bad Test Cases
# print("Bad Test")
# print(is_isogram(12456)) int isnt iterable
# print(is_isogram(124-5+6))

#Edge Cases
# list = ["a",7,"c"]
# print(is_isogram(list))
# print(is_isogram("iSograms"))
# print(is_isogram("")) #return true
# print(is_isogram("1234567890qwertyuiopasdfghjklzxcvbnm,./;[]{}")) - Impossible to go too long with normal characters
