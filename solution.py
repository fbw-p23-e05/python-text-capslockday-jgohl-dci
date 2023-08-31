user_input = input("Give me a sentence: ")

if user_input.isupper() == True:
    print(user_input.capitalize() + '!')
else:
    print(user_input.capitalize() + '.')