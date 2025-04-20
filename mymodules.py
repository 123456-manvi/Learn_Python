#python compiler
# modules in python

def say_hello(name):
    return print(f"Hello, {name}")
    
import mymodule
mymodule.say_hello('Madhav')



# ..................
person1={'name' : 'keshav', 'age' : 16}

from mymodule import person1
print(person1['age'])
