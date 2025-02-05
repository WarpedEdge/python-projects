# python-projects
Personal repository for all python related projects.

## Data Types:

```
str = string text which can be anything from "hello", "hi", "89", or "8.9"
int = integer are whole numbers like 8, 7, -9, 100000
float = decimals like 6.0, 7.5, -9.8 
bool = boolean which are True and False conditions
```

## Arithmetics
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

## Comparison Operators 
```
<  greater than
>  less than
<=  greater than or equal to
>=  less than or equal to
==  is equal to
!=   is NOT equal to
```

## Conditions 
```
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

## Variables
Variables can only be lowercase letters, uppercase letters, underscores, and numbers. 
```
hello1 = 9 

1hello = 9 <- does not work
```

## Methods
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

## Logical Operators
`and` = If both things left and right are true then it will show as true, but if one is false then the result is false
`or` = Looks at the left and right side and if both are met the entire thing is true

### Examples
Both examples below are true as it is always going in a True or False method 5 == 5 is true but 7 == 8 is false which means the entire result is met meaning True, but the 3rd example is false as the True statement is correct, but the false statement is actually true as 7 does equal 7
```
True or False -> True
5 == 5 or 7 == 8 -> True 
5 == 5 or 7 == 7 -> False
```

## Defining functions and importing them from another file
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