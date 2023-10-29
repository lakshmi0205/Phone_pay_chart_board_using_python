# phone pay chart board
print("1 - Have an issue with a transaction?. \n 2 - No just to try it. ")
step_1 = int(input("Do you have any issue: "))
if step_1 == 1:
    print("1 - Issue with failed payments. \n 2 - Issue with pending payments. \n 3 - Issue with successful payments. \n 4 - Issue with payments made to merchants. \n 5 - Issue with refunds.")
    step_2 = int(input("Enter the isse:"))
    if step_2 == 1:
        print("1 - Why did my UPI payment fail? \n 2 - Why is my money deducted for my failed payment? \n 3 - Why is my money not refunded yet? \n 4 - Where can I find the UTR number for this payment?")
        step_3 = int(input("Enter the isse:"))
        if step_3 == 1:
            print("May failed due to netwrk issue! ")
        elif step_3 == 2:
            print("No need to worry your money is Absolutely")
        elif step_3 == 3:
            print("Banks usually refund the money anywhere btw 3 to 5 days from the time of payment")
        elif step_3 == 4:
            print("> History > failed paymentn for which u like to view the UTR number > you will see the 12 digit UTR number in the Debited from the section on the screen.")
        else:
            print("Go back!")
    elif step_2 == 2:
        print("1 - Why is my UPI payment pending? \n 2 - What do I do if my UPI payment is pending ? \n 3 - Why do I have to wait for 48 hrs to know the final payment status? \n 4 - How do I cancel my pending payment? \n 5 - What if my payment is pending for more than 48 hrs?")
        step_3 = int(input("Enter the isse:"))
        if step_3 == 1:
            print("In rare case, Due to Technical issues, banks may take additional time deposit the payment money into the receivers account ")
        elif step_3 == 2:
            print("you need to wait for 48 hrs for your bank to update the final status of the payment.")
        elif step_3 == 3:
            print("As per current banking timelines, banks can take anywhere btw 2min to 48hrs.")
        elif step_3 == 4:
            print("You cant cancel UPI payments once initiated as they are debited bank to bank transfers.")
        elif step_3 == 5:
            print("Banks usually confirm the final payment status within 48 hrs from the time you made, if still pending create a ticket.")
        else:
            print("Go back!")
    elif step_2 == 3:
        print("1 - Payments made to a phone number or UPI ID \n 2 - Payments made to a bank account.")
        step_3 = int(input("Enter the isse:"))
        if step_3 == 1:
            print("Inside 6 steps are there wait lets do afterwards!")
        elif step_3 == 2:
            print("Inside 5 steps are there wait lets do afterwards!")
    elif step_2 == 4:
        print("1 - What if the merchant denies having received amount for a successful payment? \n 2 - What if I have paid twice for an order or booking? \n 3 - What if the order or booking is not confirmed for a successful payment? ")
        step_3 = int(input("Enter the isse:"))
        if step_3 == 1:
            print("Create a ticket for relevant payment ")
        elif step_3 == 2:
            print("contact ur bank directly and raise a complaint with the UTR number for the relevant payment.")
        elif step_3 == 3:
            print("you contact the merchant directly for the update")
        else:
            print("Go back!")
    elif step_2 == 5:
        step_3 = print("1 - Refunds for UPI payments. \n 2 - Refunds for card payment. \n 3 - Refunds for payment made to a merchant. ")
        step_3 = int(input("Enter the isse:"))
        if step_3 == 1:
            print("It showing 2 option please check it!")
        elif step_3 == 2:
            print("It also showing 2 option please check it!")
        elif step_3 == 3:
            print("When will I receive a refund for a cancelled or failed order?")
        else:
            print("Go back!")
else:
    print("U can try later bye!!!")
