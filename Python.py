
#####################

print("Welcome to the website, please enter you name and age.")

#####################


name = "David"
age = 16  


#####################

if age >= 100:
    is_allowed = "too old"
elif age <= 17:
    is_allowed = "not allowed"
else:
    is_allowed = "allowed"

#####################

welcome_sentence = f"Hello {name.upper()}, you are {is_allowed.upper()} to join!"
print(welcome_sentence)

######################


