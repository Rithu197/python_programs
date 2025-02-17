from datetime import datetime

def calculate_time_difference(date1_str, date2_str):
    # Define the format for the input date
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # Convert the date strings to datetime objects
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    # Calculate the difference between the two dates
    time_difference = abs(date2 - date1)
    
    # Extract days, hours, minutes, and seconds
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes, seconds

# Take two dates as input from the user
date1_input = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_input = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# Calculate the difference
days, hours, minutes, seconds = calculate_time_difference(date1_input, date2_input)

print(f"Time difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
