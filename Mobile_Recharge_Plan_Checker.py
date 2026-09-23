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
