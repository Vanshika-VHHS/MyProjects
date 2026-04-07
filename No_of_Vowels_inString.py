string = input("Enter a string: ")  #Dynamic input from the user
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)



