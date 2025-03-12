def greet_english(name):
	print("Hello, " + str(name) + ' welcome to the wonderful world of zipCode')

def greet_spanish(name):
	print("Hola, " + str(name))

def greet_french(name):
	print("Bonjour, " + str(name))
	
def greet_german(name):
	print("Guten Tag, " + str(name))
	
def name_input_english():
	print("Enter your name: ")
	x = input()
	return x

def name_input_spanish():
	print("Ingresa tu nombre: ")
	x = input()
	return x

def name_input_french():
	print("Entrez votre nom: ")
	x = input()
	return x

def name_input_german():
	print("Geben Sie Ihren Namen ein: ")
	x = input()
	return x

def language_input():
    print("Options: \n English \n Spanish \n French \n German \n")
    b = input("Choose a language \n")
    return b


h = language_input().lower()

if h == 'english':
    g = name_input_english()
    greet_english(g)
elif h == 'spanish':
    u = name_input_spanish()
    greet_spanish(u)
elif h == 'german':
	c = name_input_german()
	greet_german(c)
elif h == 'french':
    k = name_input_french()
    greet_french(k)
else:
	print("Not a recognized option")
	

#b = name_input()
#greet(b)
