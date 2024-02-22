# import datetime
# from datetime import date



# x = datetime.datetime(2018, 6, 1)     

# print(x.strftime("%B"))
# x = datetime.datetime.now()
# print(type(x))

# print(x.strftime("%H"))
# print(x.strftime("%M"))
# print(x.strftime("%l"))




# start_date = date(2023, 3, 1)


# year = start_date.year
# month = start_date.month
# day = start_date.day


# weekday = start_date.weekday()


# date_str = start_date.strftime('%Y-%m-%d')
# print(year)
# print(month)
# print(day)
# print(weekday)

# todays_date = date.today()

# print("Today's date =", todays_date)

# timestamp = date.fromtimestamp(132624364)
# print("Date =", timestamp)



# today = date.today() 

# print("Current year:", today.year)
# print("Current month:", today.month)
# print("Current day:", today.day)


# from datetime import time
# a= time(11,56,33)
# print(a)
# b= time(12,22,22,220336)
# print(b)


# c= time(15,6,22)
# print(c.hour)



# from datetime import datetime


# datetime_str = '05/02/10 13:55:26'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

# print(type(datetime_object))
# print(datetime_object)
# print(type(datetime_object.date()))
# print(type(datetime_object.time()))
# print(datetime_object.time())



# import time  
  
# current_time = time.localtime()  
# current_clock = time.strftime("%H:%M:%S", current_time)  
  
# print("The current timezone is:", current_clock)  



# from datetime import datetime
# import pytz  
  
# Get the current Datetime  
# object = datetime.now()  
# print('Timezone ', object)  
  
# object1 = datetime.now(pytz.utc)  
# print('Timezone ', object1)  

# us = datetime.now(pytz.timezone('US/Central'))  
# print('US DateTime',us)  
# for timezone in pytz.all_timezones:
#     print(timezone)

# print(datetime.now(pytz.timezone('UTC')))
# print(datetime.now(pytz.timezone('Indian/Christmas')))


# dt1= datetime.now(pytz.timezone('America/Argentina/Buenos_Aires'))  
# print("US Buenos DateTime:", dt1.strftime("%Y:%m:%d %H:%M:%S %Z %z")) 


# dt2 = datetime.now(pytz.timezone('America/Adak'))  
# print("US Adak timezone DateTime:", dt2.strftime("%Y:%m:%d %H:%M:%S %Z %z"))  
from datetime import datetime, timedelta
import pytz   


####difference between UTC  and germany timing  

dt_local = datetime.now(pytz.utc)  
print(dt_local)
print("UTC DateTime:", dt_local.strftime("%Y:%m:%d %H:%M:%S %Z %z"))  
print(type(dt_local))

dt_germany = pytz.timezone('Asia/Kolkata')
timeInGermany = datetime.now(dt_germany) + timedelta(hours=1)
print(dt_germany)
print(timeInGermany)
# print("india DateTime:", dt_germany.strftime("%Y:%m:%d %H:%M:%S %Z %z"))  
print(type(dt_germany))

# difference = pytz.timezone('Europe/Berlin') - datetime.datetime.utcnow()
# print(difference)
difference = (timeInGermany- dt_local) .total_seconds()/60
print(difference)


##### difference between localtime and UTC timing 
difference1 = datetime.now() - datetime.utcnow()
print(difference1)




# from datetime import datetime, timedelta

# # Get current UTC time
# utc_now = datetime.utcnow()

# # Get current Germany time (CET)
# cet_now = datetime.now() + timedelta(hours=1)  # Germany is typically UTC+1

# # Calculate the time difference in minutes
# time_difference_minutes = (cet_now - utc_now).total_seconds() / 60

# print("Time difference between Germany (CET) and UTC:", time_difference_minutes, "minutes")
