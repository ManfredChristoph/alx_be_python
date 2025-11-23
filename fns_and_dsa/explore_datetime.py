from datetime import datetime, timedelta

def display_current_datetime():
"""Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
   current_date = datetime.now()
   formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")




def calculate_future_date(days):
"""Calculate and display the future date after adding given number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
     print(f"Future date: {formatted_future}")
