# Mobile_Recharge_Plan_Checker.....
name=input("enter customer name :")
plan_type=input("enter plan type-(basic/standard/premium) :")
amount=int(input("enter recharge amount :"))
print("customer name :",name)
print("plan type : ", plan_type)
print("recharge amount :",amount)
if plan_type=="basic":
    if amount>=299 :
        print("plan status : Activated \n validity : 42 days \n Offer : Extra 5GB Data")
    elif amount>=199 :
        print("plan status : Activated \n validity : 28 days \n Offer : Extra 3GB Data")
    else:
        print("invalid recharge amount")
elif plan_type=="standard":
    if amount>=499 :
        print("plan status : Activated \n validity : 70 days \n Offer : Extra 9GB Data")  
    elif amount>=399 :
        print("plan status : Activated \n validity : 56 days \n Offer : Extra 6GB Data")
    else:
        print("invalid recharge amount")
elif plan_type=="premium":
    if amount>=799 :
        print("plan status : Activated \n validity : 100 days \n Offer : Extra 16GB Data")  
    elif amount>=599 :
        print("plan status : Activated \n validity : 84 days \n Offer : Extra 11GB Data")
    else:
        print("invalid recharge amount")
 

 
