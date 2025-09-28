from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now()
    return (f" current date and time: {current_date.year}-{current_date.month}-{current_date.day} {current_date.hour}:{current_date.minute}:{current_date.second}")
current_days=int(input("Enter number of days to add to the current date: "))
def calculate_future_date(curret_days):
    future_date=datetime.now()+timedelta(days=curret_days)
    return (f"Future date: {future_date.year}-{future_date.month}-{future_date.day} ")
"""def main():
    display_current_datetime()
    calculate_future_date(current_days) 
if __name__=="__main__":
    main()"""