#made a function that calculates the months it'll take to get a down payment depending on factors the user enters in such as salary and home price
def down_payment_time():

    #I ask for the user to enter in the cost of the house and then the annual salary to get the calculations started
    total_cost = float(input("Enter the total cost of the house: "))
    
    annual_salary = float(input("Enter your annual salary: "))
    
    #savings starts at 0
    current_savings = 0

    num_of_months = 0

    #used to get our monthly pay
    monthly_salary = annual_salary/12

    #25 percent is the amount needed for a down payment
    portion_down_payment = .25

    #calculates the down_payment we need to hit depending on the given house price
    down_payment = total_cost * portion_down_payment

    #a variable that calculates our money invested into the savings
    invested_savings = current_savings * .04 / 12

    #we are savings 10 percent of monthly pay to put into the savings account    
    portion_saved = (monthly_salary) * .1

    #continue this loop until our savings exceeds the down payment price we need to hit
    while down_payment > current_savings:

        #each loop cycle represents a month so we add the invested money with the saved amount each month and add it to our savings
        current_savings += invested_savings + portion_saved

        #increase number of months by 1 each time this while loop reiterates
        num_of_months += 1

    #this is our final result to give us the number of months it will take to afford the down payment
    return num_of_months

print("It will take this many months to afford the down payment:", down_payment_time())
