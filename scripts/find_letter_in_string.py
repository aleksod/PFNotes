user_string = str(raw_input("Please enter your string: "))
user_letter = str(raw_input("Please enter the letter to count in the string: "))

print user_string.lower().count(user_letter.lower())
