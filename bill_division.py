print("Welcome to the Bill calculator")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage would you like to give? 10, 12 or 15? "))
people = int(input("How  many people to slipt the bill?"))

result = (total_bill * (1 + percentage / 100)) / people
final_result = '{:.2f}'.format(result)
print(f"Each person sould pay: ${final_result}")
input("Press enter to finish the program")

