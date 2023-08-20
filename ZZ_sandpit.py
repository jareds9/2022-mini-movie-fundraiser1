import random

characters = [
    "a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z","1","2","3","4","5","6","7","8","9",",",".","@","!","#","$","%","^","&","*","(",")","/","{","}","-","_","=","+"
]

def number_checker(question):
    user_input = input(question)

    try:
        return int(user_input)
    except ValueError:
        print("Input must be a whole number!")
        print()
        return number_checker(question)

length = number_checker("Length: ")
random_string = ""

for i in range(0,length):
    random_string += random.choice(characters)

print()
print(random_string)
print()

what_for = input("What is this password for? ")
location = input("Where would you like to save this? ")

opened = open(f"{location}.txt","a")
opened.write(f"{what_for}: {random_string}\n\n")