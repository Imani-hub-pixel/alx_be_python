from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now()
    return f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}"
current_days = int(input("Enter number of days to add to the current date: "))

def calculate_future_date(current_days):
    future_date=datetime.now()+timedelta(days=current_days)
    return f"Future date: {future_date.strftime('%Y-%m-%d')}"
"""def main():
    display_current_datetime()
    calculate_future_date(current_days) 
if __name__=="__main__":
    main()"""