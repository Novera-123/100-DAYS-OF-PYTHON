print("Welcome to the tip calculator")
bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? 10,12 or 15 ? ")
total = int(tip)/100
percent = total * int(bill)
tip_added = percent + int(bill)
# print(tip_added)
people = input("Enter the number of people : ")
total_bill = tip_added / int(people)
print(f"Your bill per person is : ${total_bill}")

