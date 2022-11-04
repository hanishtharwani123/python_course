def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip ()

this = "        hanish is a good           "
n = remove_and_split(this, "hanish")
print(n)
