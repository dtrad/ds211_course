# You run a travel agency. The agency offers discounts to seniors if they are registered for the Senior's Discount program. Only one membership
# per household is allowed. If someone travels with a spouse, both partners must be seniors and only one of them can have an active Senior's Discount membership
# in order for them both to receive the discount. More than one membership per household is considered a violation of the program rules. Two individuals can provide
# the same membership number.
# Ordinary ticket prices are $350 per traveller. Senior's Discount prices are $275 per traveller.

SENIOR_AGE = 65
COST = 350
DISCOUNT_COST = 275

discount = False
partner = False
user_senior = False
partner_senior = False
member_code = ""
partner_member_code = ""

user_age = int(input("Enter your age: "))
if (user_age >= SENIOR_AGE):
    user_senior = True
    member_code = input("If applicable, enter your Senior's Discount membership code: ")

answer = input("Are you travelling with a partner?\nEnter 'y' for yes and 'n' for no: ")
if (answer == "y"):
    partner = True
    partner_age = int(input("Enter your partner's age: "))
    if (partner_age >= SENIOR_AGE):
        partner_senior = True
        partner_member_code = input("If applicable, enter your partner's Senior's Discount membership number: ")

if (user_senior and (partner_senior or not partner) or 
    ((member_code == "" and not partner_member_code == "") or 
    (member_code == "" and partner_member_code == "") or 
    (not member_code == "" and member_code == partner_member_code))):
    discount = True

if (discount):
    if (partner):
        print("Total cost for two tickets with senior discount: ", DISCOUNT_COST * 2)
    else:
        print("Total cost for one ticket with senior discount: ", DISCOUNT_COST)
else:
    if (partner):
        print("Total cost for two tickets at regular price: ", COST * 2)
    else:
        print("Total cost for one ticket at regular price: ", COST)
