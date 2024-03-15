#Your Name

#Date

#Assignment Name

#A brief description of the project

#WHY DOES IDLE NOT SUPPORT /b MAN

print("this program calculates and displays travel expenses")
print(' ')
print("enter budget:",end=' ')
user_budget=int(input())
print("Enter budget:",user_budget)
print("Enter your travel destination:",end=' ')
user_destination=(input())
print("Enter your travel destination",user_destination)
print("How much do you think you will spend on gas?",end=' ')
user_gas=int(input())
print("How much do you think you will spend on gas?",user_gas)
print("Approximately, how much will you need for accomodation/hotel?",end=' ')
user_hotel_price=int(input())
print("Approximately, how much will you need for accomodation/hotel?",user_hotel_price)
print("Last, how much do you need for food?",end=' ')
user_food_price=int(input())
print("Last, how much do you need for food?",user_food_price)
print()

print("------------Travel Expenses------------")
print('location:',user_destination)
print("Initial Budget:",f'${user_budget:.2f}')
print('Fuel:',f'${user_gas:.2f}')
print('Accomodation:',f'${user_hotel_price:.2f}')
print('food:',f'${user_food_price:.2f}')
print("---------------------------------------")
user_expenses_sum=int(user_gas+user_hotel_price+user_food_price)
user_remaining_balance=int(user_budget-user_expenses_sum)
print(' ')
print('Remaining Balance:',f'${user_remaining_balance:.2f}')
