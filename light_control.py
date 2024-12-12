#This api outputs data that does compensate for Daylight savings time.
#alt 3 comments out code, alt 4 uncomments out code

#from datetime import time, timedelta
#from datetime import datetime  #We imported the datetime class from the datetime module and called the now method on the class.
import datetime
from suntime import Sun, SunTimeException
import time
#import timedelta
import logging


##################################################################################
#######################This section gets Sunrise/sunset from API###################
d = datetime.datetime.now()
today_date = d.date() # date today
time_now = d.time() # time now
print('time now ', time_now)
logging.debug('time now', time_now)

time_now_min = d.hour * 60 + d.minute # time now
#time_now_min_test = 1150 #for testing
print('time now in minutes ', time_now_min)
logging.info('time now in minutes ', time_now_min)

latitude = 41.55
longitude = -90.49

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_local_sunrise_time()
today_ss = sun.get_local_sunset_time()
test_sr = time_now
test_ss = time_now
# print('Today at Bettendorf the sun raised at {} and set down at {} UTC'.
#       format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))
#print('Hour: ', today_sr.hour)
print('Sunrise ', today_sr.strftime('%H:%M'))   #strftime converts objects back to strings
print('Sunset ', today_ss.strftime('%H:%M'))    #strptime converts strings to objects
logging.info('Sunrise ', today_sr.strftime('%H:%M')) 
logging.info('Sunset ', today_ss.strftime('%H:%M'))    

##################################################################