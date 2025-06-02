import datetime

def display_current_time():

    current_time = datetime.datetime.now()
    
    formatted_time = current_time.strftime("%A, %B %d, %Y at %I:%M:%S %p")
    
    print(f"The exact current local time is: {formatted_time}")

if __name__ == "__main__":
    display_current_time()
