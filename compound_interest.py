#Compound interest is the addition of interest to the principal sum of a loan or deposit, or in other words, interest on interest. 
# It is the result of reinvesting interest, rather than paying it out, 
# so that interest in the next period is then earned on the principal sum plus previously accumulated interest.

def compound_interest(monthly_savings,months,percent): #Parameters used to call the function 
                                                       #(monthly savings amount, months that the savings will last, monthly interest percentage) 
    previous_savings = 0 
    for i in range(0,months): #iteration trough the months

    	print("Month [",i+1,"] ---> monthly savings: $","{:.2f}".format(monthly_savings),end="") #amount of monthly saving
    	print("---> last_savings: $","{:.2f}".format(previous_savings),end="") #amount of previous savings
    	print("---> total saving: $","{:.2f}".format(monthly_savings+previous_savings)) #total savings amount
        #printing are with two decimal places 
        
    	previous_savings = (monthly_savings+previous_savings) * (1+(percent/100)) #calculation of compound interest month by month
    	
compound_interest(1000,13,1.277) #Example with a monthly saving of $ 1,000, at 13 months and with a monthly interest of 1,277% 
#Here you can modify the parameters to calculate different amounts of savings, months that the savings will last and the monthly interest. 
