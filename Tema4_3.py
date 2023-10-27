import datetime
import time

end_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
while datetime.datetime.now() < end_time:
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущее время: {formatted_time}")
    time.sleep(1)