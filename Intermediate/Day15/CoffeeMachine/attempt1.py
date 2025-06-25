# from menu import MENU, resources
# money = 0
# enough_resources = True
# while enough_resources:
#     # TODO: 1. Prompt user what coffee they would like
#     coffee_prompt = input("What would you like? (espresso/latte/cappuccino):\n").lower()
#     # coffee_prompt = "latte"
#     # TODO: 2. Turn off the machine by entering "off" in prompt
#     if coffee_prompt == "off":
#         print("Powering down...")
#     # TODO: 3. Print report when "report" in prompt
#     elif coffee_prompt == "report":
#         for key, value in resources.items():
#             print(f"{key}: {value}")
#         print(f"money: ${money}")
#     # TODO: 4. Check resources of machine when coffee choice made, if sufficient subtract resources
#
#     elif coffee_prompt == "espresso":
#         water_requirement = MENU["espresso"]["ingredients"]["water"]
#         coffee_requirement = MENU["espresso"]["ingredients"]["coffee"]
#         if water_requirement > resources["water"]:
#             print("Not enough water.")
#         elif coffee_requirement > resources["coffee"]:
#             print("Not enough coffee.")
#         else:
#             resources["water"] -= water_requirement
#             resources["coffee"] -= coffee_requirement
#             print(resources)
#
#     elif coffee_prompt == "latte":
#         water_requirement = MENU["latte"]["ingredients"]["water"]
#         milk_requirement = MENU["latte"]["ingredients"]["milk"]
#         coffee_requirement = MENU["latte"]["ingredients"]["coffee"]
#         if water_requirement > resources["water"]:
#             print("Not enough water.")
#         elif milk_requirement > resources["milk"]:
#             print("Not enough milk.")
#         elif coffee_requirement > resources["coffee"]:
#             print("Not enough coffee.")
#         else:
#             resources["water"] -= water_requirement
#             resources["milk"] -= milk_requirement
#             resources["coffee"] -= coffee_requirement
#             print(resources)
#
#     elif coffee_prompt == "cappuccino":
#         water_requirement = MENU["cappuccino"]["ingredients"]["water"]
#         milk_requirement = MENU["cappuccino"]["ingredients"]["milk"]
#         coffee_requirement = MENU["cappuccino"]["ingredients"]["coffee"]
#         if water_requirement > resources["water"]:
#             print("Not enough water.")
#         elif milk_requirement > resources["milk"]:
#             print("Not enough milk.")
#         elif coffee_requirement > resources["coffee"]:
#             print("Not enough coffee.")
#         else:
#             resources["water"] -= water_requirement
#             resources["milk"] -= milk_requirement
#             resources["coffee"] -= coffee_requirement
#             print(resources)
#
#     # TODO: 5. Process coins ".01", ".05", ".10" and ".25" and add them up in the end
#     penny = .01
#     nickel = .05
#     dime = .10
#     quarter = .25
#
#     pennies = int(input("How many pennies? "))
#     nickels = int(input("How many nickels? "))
#     dimes = int(input("How many dimes? "))
#     quarters = int(input("How many quarters? "))
#
#     calculated_pennies = penny * pennies
#     calculated_nickels = nickel * nickels
#     calculated_dimes = dime * dimes
#     calculated_quarters = quarter * quarters
#
#     combined_total = calculated_pennies + calculated_nickels + calculated_dimes + calculated_quarters
#     rounded_total = round(combined_total, 2)
#
#     print(f"${rounded_total}")
#
#     # TODO: 6. Compare money provided to cost of drink, if not enough refund money, if over provide change
#     if coffee_prompt == "espresso":
#         if rounded_total == MENU["espresso"]["cost"]:
#             print("Purchase Successful")
#             money += rounded_total
#             print(f"Current machine money: ${money}")
#         elif rounded_total < MENU["espresso"]["cost"]:
#             print(f"Not enough money, here is your money back: ${rounded_total}")
#         else:
#             customer_change = rounded_total - MENU["espresso"]["cost"]
#             customer_change_rounded = round(customer_change, 2)
#             print(f"Purchase successful. Here is your espresso.\nYour change: ${customer_change_rounded}")
#     if coffee_prompt == "latte":
#         if rounded_total == MENU["latte"]["cost"]:
#             print("Purchase Successful")
#             money += rounded_total
#             print(f"Current machine money: ${money}")
#         elif rounded_total < MENU["latte"]["cost"]:
#             print(f"Not enough money, here is your money back: ${rounded_total}")
#         else:
#             customer_change = rounded_total - MENU["latte"]["cost"]
#             customer_change_rounded = round(customer_change, 2)
#             print(f"Purchase successful. Here is your latte\nYour change: ${customer_change_rounded}")
#     if coffee_prompt == "cappuccino":
#         if rounded_total == MENU["cappuccino"]["cost"]:
#             print("Purchase Successful")
#             money += rounded_total
#             print(f"Current machine money: ${money}")
#         elif rounded_total < MENU["cappuccino"]["cost"]:
#             print(f"Not enough money, here is your money back: ${rounded_total}")
#         else:
#             customer_change = rounded_total - MENU["cappuccino"]["cost"]
#             customer_change_rounded = round(customer_change, 2)
#             print(f"Purchase successful. Here is your cappuccino\nYour change: ${customer_change_rounded}")
#
# # TODO: 7. Have the machine make coffee and present it to the user and adjust resources