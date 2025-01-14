from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    
    # Calculate the difference in years, months, and days
    years = today.year - birthdate.year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        years -= 1
    
    # Calculate months
    months = today.month - birthdate.month
    if today.day < birthdate.day:
        months -= 1
    if months < 0:
        months += 12
    
    # Calculate days
    day_of_birth = birthdate.replace(year=today.year, month=today.month, day=today.day)
    if today < day_of_birth:
        day_of_birth = birthdate.replace(year=today.year, month=today.month-1, day=today.day)
    
    days = (today - day_of_birth).days
    
    # Calculate weeks
    weeks = days // 7
    days_left = days % 7
    
    return years, months, weeks, days, days_left

# Input: birthdate in YYYY-MM-DD format
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

# Calculate age
years, months, weeks, days, days_left = calculate_age(birthdate)

print(f"Your age is {years} years, {months} months, {weeks} weeks, and {days_left} days.")
