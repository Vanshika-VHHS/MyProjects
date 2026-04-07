Str = input("Enter a string: ")
print("The string you entered is:", Str)
str_length = len(Str)
print("The length of the string is:", str_length)
str_upper = Str.upper()
print("The string in uppercase is:", str_upper)
str_lower = Str.lower()
print("The string in lowercase is:", str_lower)
str_concatenated = Str + " is a string."
print("Concatenated string:", str_concatenated)

#counting the words in the string
str_words = Str.split()
print("The words in the string are:", str_words)


str_vowels = [char for char in Str if char.lower() in 'aeiou']
print("The vowels in the string are:", str_vowels)

str_reversed = Str[::-1]
print("The string in reverse is:", str_reversed)

str_slice = Str[1:5]
print("The slice of the string from index 1 to 4 is:", str_slice)