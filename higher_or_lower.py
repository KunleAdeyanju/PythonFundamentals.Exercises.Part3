from random import randrange

a = int (input("Provide a number between 0 and 10 \n"))

def rand_number():
    return randrange(10)

def compare_numbers(x,y):
    if x > y:
        print("Too high")
    elif y < x:
        print("Too Low")
    elif x == y:
        print("You guessed correct")

b = int (rand_number())
#print(compare_numbers(a,b))
compare_numbers(a,b)

print("The random number was: " + str (b))
print("Your guess was: " + str (a))

