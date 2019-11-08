'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    to_find = 'th'

    #Base
    if len(word) == 0 or len(word) < len(to_find):
        return 0
    #Recurse and count or recurse
    if word[0:len(to_find)] == to_find:
        return 1 + count_th(word[len(to_find) - 1:])
    else:
        return count_th(word[len(to_find) - 1:])
