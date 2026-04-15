card_details=[
    {"card_name":"prabha","card_number":987654,"pin":2288,"balance":17531},
    {"card_name":"palani","card_number":213141,"pin":1122,"balance":11000},
    {"card_name":"rocky","card_number":333231,"pin":7708,"balance":20000},
    {"card_name":"steve","card_number":221144,"pin":9080,"balance":22000}
]
cash_in_atm={"500":10,"200":10,"100":100}


def get_cardby_number (number):
    for n in card_details:
        if number==n["card_number"]:
            return n
    return None    


while True:
    card_num=int(input("enter your card number :"))
    card_information=get_cardby_number(card_num)
    if card_information==None:
         print("Invalid card")
         continue
    get_pin=int(input("enter your pin :"))
    if get_pin!=card_information["pin"]:
        print("Invalid pin")
        continue
    while True:
        amount=int(input("enter your amount:"))
        if amount>=card_information["balance"]:
            print("*************************")
            print("insufficient balance. \nAvailable Bank Balance:",card_information["balance"])
            print("*************************")
            continue
    
        if amount%500!=0:
            print("enter only round off '500s'")
            continue
        break

    dinomi=amount//500
    
    if dinomi>=cash_in_atm["500"]:
        print("insufficient in ATM")
        continue
    
    cash_in_atm["500"]=cash_in_atm["500"] - dinomi
    card_information["balance"]=card_information["balance"]-amount

    print("Please collect your cash",amount)
    print("your acc balance",card_information["balance"])
    print("Thank you for visiting Indian Bank ATM")
    
         
    
         
        
              
    
         

   

# print(get_cardby_number(333231))