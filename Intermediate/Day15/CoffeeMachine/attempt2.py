MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_format(resources_dict):
    for key, value in resources.items():
        print("{} {}".format(key, value))

def resources_requirement():
    if coffee_prompt == "espresso":
        water_requirement = MENU["espresso"]["ingredients"]["water"]
        print(water_requirement)
        coffee_requirement = MENU["espresso"]["ingredients"]["coffee"]
        print(coffee_requirement)
    elif coffee_prompt == "latte":
        water_requirement = MENU["latte"]["ingredients"]["water"]
        print(water_requirement)
        coffee_requirement = MENU["latte"]["ingredients"]["coffee"]
        print(coffee_requirement)
    else:
        water_requirement = MENU["cappuccino"]["ingredients"]["water"]
        print(water_requirement)
        coffee_requirement = MENU["cappuccino"]["ingredients"]["coffee"]
        print(coffee_requirement)
# TODO: 1. Prompt user what coffee they would like
operation_status = True
while operation_status:
    coffee_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # coffee_prompt = "espresso"
    # TODO: 4. Check resources of machine when coffee choice made, if sufficient subtract resources
    if coffee_prompt == "espresso" or "latte" or "cappuccino":
        resources_requirement()
    # TODO: 2. Turn off the machine by entering "off" in prompt
    elif coffee_prompt == "off":
        operation_status = False
    # TODO: 3. Print report when "report" in prompt
    elif coffee_prompt == "report":
        operation_status = False
        resources_format(resources)
    else:
        operation_status = False




# TODO: 5. Process coins ".01", ".05", ".10" and ".25" and add them up in the end

# TODO: 6. Compare money provided to cost of drink, if not enough refund money, if over provide change

# TODO: 7. Have the machine make coffee and present it to the user and adjust resources