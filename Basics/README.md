# python-projects
Personal repository for all python related projects.

## [Data Types](https://www.w3schools.com/python/python_datatypes.asp)

```
str = string text which can be anything from "hello", "hi", "89", or "8.9"
int = integer are whole numbers like 8, 7, -9, 100000
float = decimals like 6.0, 7.5, -9.8 
bool = boolean which are True and False conditions
```

## [Arithmetic Operators](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)
```
* = multiplication
** = raise to the power of
/ = division
+ = addition
- = subtraction
% = modulas (remainder of a divison)
// = integer division
```

### Examples
```
x = 9
y = 8
z = * (y + y) quotes will follow PEMDAS standards 
x + y would give 17, but would not be stored anywhere
x = x + y <- this stores the what the value of the two items being
x += y is the shorthand division of x = x+y
z = x % y -> 1 due to the ramainder of how many times 2 can go into 5 which is 2 but then there is a reamainder of 1 left over so the answer is 1
z = x // y if x was 7 and y was 2, how many times can 2 going into 7 which is 3 times, so the answer is 3
```

## [Conditions](https://www.w3schools.com/python/python_conditions.asp) 
```
<  greater than
>  less than
<=  greater than or equal to
>=  less than or equal to
==  is equal to
!=   is NOT equal to

if = self explanatory
else = if the "if" condition is not met do this
elif = is short for "else if" allowing multiple conditions. You can have multiple elifs
```

### Examples
```
if age >= 18:
    print("Welcome to my first game!")
elif age >= 14:
    print("You can play with a parent's supervision")
else:
    print("You are not old enough to play...")
```

## [Variables](https://www.learnpython.org/en/Variables_and_Types)
Variables can only be lowercase letters, uppercase letters, underscores, and numbers. 
```
hello1 = 9 

1hello = 9 <- does not work
```

## [Methods](https://stackoverflow.com/questions/3786881/what-is-a-method-in-python)
```
.lower() = will make the input right after all lowercased
.upper() = will make the input right after all uppercased
```

### Examples
The `.lower()` at the end of the line below will make whichever response given transform into lowercase, in this case if someone typed in `Yes` or `yEs` it will automatically change it to yes so it meets the `==`
```
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
    if wants_to_play == "no":
        print("Goodbye!")
```

## [Logical Operators](https://www.w3schools.com/python/gloss_python_logical_operators.asp)
`and` = If both things left and right are true then it will show as true, but if one is false then the result is false
`or` = Looks at the left and right side and if both are met the entire thing is true

### Examples
Both examples below are true as it is always going in a True or False method 5 == 5 is true but 7 == 8 is false which means the entire result is met meaning True, but the 3rd example is false as the True statement is correct, but the false statement is actually true as 7 does equal 7
```
True or False -> True
5 == 5 or 7 == 8 -> True 
5 == 5 or 7 == 7 -> False
```

## [Built-in Functions](https://docs.python.org/3/library/functions.html)
```
print() => Prints to the standard output device
intput() => Asks user for input
set() => Returns a new set
int() => Converts value into an integer number
str() => Converts value into a string
```

## [Defining functions and importing them from another file](https://www.learnpython.org/en/Functions)
`def` = refers to the the start of a function you want to define

`from <file> import <function>` = Putting this anywhere in your file will import specific functions from those files that have been defined. This can be anywhere from function to function1, function2, function3, etc. or * meaning all def's in that file

### Examples
```
def game_start(health):
    wants_to_play = input("Do you want to play (yes/no)? ").lower()
```

The above is a quick def created in a file called something like adventure.py which also is located in a folder called "Game". The below example will be from the main.py in a shorthand example showing not only how to import this function, but a function from not the same directory

`from Game.adventure import game_start`

This will allow the main.py to use the def function created in Game/adventure.py which then can be called upon using the game_start

## [Classes and Objects](https://www.learnpython.org/en/Classes_and_Objects)
`class` = is a blueprint for creating objects

`object` = is an instance of a class

### Examples

Creating a class called User with a few attributes and methods (methods are essentially
functions that are part of a class)
```
class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")
```
The __init__ method is a special method that is called when the object is created.
It is used to initialize the object's attributes. The self parameter refers to the object itself.
It is then called like this
```
from user import User

app_user_one = User("rb@rb.com", "Richard B", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("cb@cb.com", "Chloe B", "supersecretmeatballs", "Financial Advisor")
app_user_two.get_user_info()
```
Lowercase user is the file name and uppercase User is the class name. 
You then can call Class just like a function with its parameters.
