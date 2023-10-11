import time
print()
print("      Please Insert Your ATM Card      ")
print("----------------------------------------------")
time.sleep(2)

password=2003

print()


pin=int(input("Please Enter Your ATM Pin:"))
if pin==password:

  print()
  card_number="7029 9215 5080"
  print("Your ATM Card Number Is : ",card_number)
  

  print()
  card_holder="Arnab Datta"
  print("Your ATM Card Holder Name Is:",card_holder)
  while True:
    print()
    
    balance = 1000

    print("     Welcome To My ATM  🤑      ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(""" 
    1)    Balance
    2)    Withdraw
    3)    Deposit
    4)    Quit        
    """)

    try:
        option=int(input("Choose An Option:"))
    except Exception as e:
        print("Error",e)
        print("Choose 1, 2, 3 or 4 Only")
        continue
    if(option==1):
        print()
        print("Your Account Balance Is $ :",balance)

    if(option==2):
        print()
        print("Your Account Balance Is $ ",balance)
        withdraw=float(input("Please Enter Withdraw Amount To Withdraw $ :"))
        print()
        if(withdraw>balance):
            print("SORRY !!! Your Account Balance Is Incufficent 😐 ")
        else:    
         CurrentBalance= float(balance-withdraw)
         print("Your", withdraw ,"Withdraw Is Sucessfully !! 🙂")
         print()
         print("Your Account Current Balance Is:",CurrentBalance)
    if(option==3):
        deposit=float(input("Please Enter Your Deposit Amount:"))
        print()
        if deposit>0:
          new_balance=balance+deposit
          print("Your",deposit, "Deposit Is Sucessfully 🙂")
          print()
          print("Your Current Account Balance Is:",new_balance)
        else:
           print("No Deposit Made 😒")
    if(option==4):
       print()
       print("ThankYou For Choosing Me Please Visit Again..🙏🙏 ")
       print()
       exit()
else:
   print("SORRY !!! Your ATM Pin Is Wrong.")
    