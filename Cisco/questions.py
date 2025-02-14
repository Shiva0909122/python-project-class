#Here are some **Python condition practice questions** for you to try! 🚀  

# Check Positive, Negative, or Zero**  
'''1. #
   Write a program that takes a number as input and prints:
   - `"Positive"` if it's greater than zero  
   - `"Negative"` if it's less than zero  
   - `"Zero"` otherwise   '''
#Odd or Even with Range**  
'''2. 
   Write a program that asks the user for a number `N` and prints **all even numbers** from `1` to `N`.'''
#Age Eligibility Check**  
'''3. 
   - If age is **18 or more**, print `"Eligible to vote"`  
   - If age is **less than 18**, print `"Not eligible to vote"`  '''
#Find Maximum of Two Numbers**  
'''4. 
   Take two numbers as input and print the largest one.  '''
#Multiple of 5 Checker**  
'''5. 
   Take a number as input and print `"Yes"` if it's a multiple of `5`, otherwise print `"No"`.'''

### **Triangle Validity Check**  
'''6. 
   Take three side lengths as input and check if they form a **valid triangle**.  
   (Sum of any two sides should be greater than the third side.)'''
#**Days in a Month**  
'''7. 
    Take the month number (`1-12`) as input and print the number of days in that month.  '''

### **Number Guessing Game (Limited Attempts)**  
'''8. 
    - Generate a random number between `1-50`.  
    - The user gets **5 chances** to guess it.  
    - Print `"Too High"` or `"Too Low"` hints.  
    - If the user guesses correctly, print `"You won!"`.  '''

#**Login Authentication System**  
'''9. 
    - Store a username and password.  
    - Ask the user to enter credentials.  
    - If correct, print `"Login Successful"`, otherwise allow **3 attempts** before exiting.  '''
#**Electricity Bill Calculator**  
'''10. 
    Based on **units consumed**, calculate the bill:  
    - **First 100 units** → ₹5 per unit  
    - **Next 200 units** → ₹7 per unit  
    - **Above 300 units** → ₹10 per unit  '''
# **Rock, Paper, Scissors Game**  
'''11.
    - User plays against the computer.  
    - Take input (`rock`, `paper`, `scissors`).  
    - Generate a random choice for the computer.  
    - Determine the winner.  '''

#**Check Armstrong Number**  
'''12. 
    - An Armstrong number of `n` digits is a number where the sum of its digits raised to the power `n` is equal to the number itself.  
    - Example: `153 = (1³ + 5³ + 3³)`.  '''
 #**Password Strength Checker**  
'''13.
    - A strong password should have:  
      - At least **8 characters**  
      - At least **one uppercase letter**  
      - At least **one number**  
      - At least **one special character** (`@, #, $, etc.`)  '''
#**FizzBuzz Game**  
'''14. 
    Print numbers from `1-50`, but:  
    - If a number is **divisible by 3**, print `"Fizz"`  
    - If **divisible by 5**, print `"Buzz"`  
    - If **divisible by both 3 and 5**, print `"FizzBuzz"`  '''


## Define the size of the square
'''15.This simple program "draws" a rectangle, making use of an old operator (+) in a new role:'''

#Question: Calculate End Time After a Given Duration
'''16.You need to write a Python program that calculates the end time of an event, given:

A starting time in hours (0–23) and minutes (0–59).
A duration in minutes (which can be arbitrarily large).'''

#Solution:
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Convert start time to total minutes
total_minutes = hour * 60 + mins + dura

# Calculate the new hour and minutes
end_hour = (total_minutes // 60) % 24  # Ensures wrap-around in 24-hour format
end_minute = total_minutes % 60

# Print the result
print(f"End time: {end_hour:02}:{end_minute:02}")
