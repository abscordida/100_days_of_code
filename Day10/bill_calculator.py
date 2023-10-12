# getting user input
total_bill = float(input("what's the total bill: "))
number_of_people = int(input("Enter the number of people: "))
tip = int(input("Select one 15,18 and 20 percent for tip: "))

# calculating 
tipping_bill = tip / 100 * total_bill + total_bill
bill_per_person = tipping_bill / number_of_people
bill_per_person = round(bill_per_person,2)
print("You each owe",bill_per_person)
