# ******* FUNCTION DEFINING WITH USER INPUTS *******
def Name(name):
    print("What is your name?")
    print(f"My name is {name}")
Name('Pavan')

def greetings(name):
    print(f"Hello, {name}")
    print("How are you?")
greetings('Pavan')
#NOTE: Here in two cases 'name' is called parameter and 'pavan' is called argument.
#parameter - name of the data that is passed in
#argument - value of the data.

#FUNCTION DEFINING WITH 'MULTIPLE' USER INPUTS
def Name(name, age):
    print(f'My name is {name} and iam {age} old.')
Name('Pavan',19)
#Here positions of parameners and arguments are important
Name(19,'Pavan')  #It gives an weird output

#FUNCTION DEFINING WITH USER INPUTS - keyword arguments
#The another solution for the above positional problem is, we can use keywords in arguments
def Name(name, age):
    print(f'My name is {name} and iam {age} old.')
Name(age=19, name='Pavan')

