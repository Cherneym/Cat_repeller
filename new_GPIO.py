#This api outputs data that does compensate for Daylight savings time.
#alt 3 comments out code, alt 4 uncomments out code

#from datetime import time, timedelta
#from datetime import datetime  #We imported the datetime class from the datetime module and called the now method on the class.
import datetime
import time
#import timedelta
#import board
#import busio
#import adafruit_mcp9808import logging

####################################################################################
#############This section initializes HAT Relays for RPi5 - Works!!!################
import gpiod
#print(getattr(gpiod, "version_string", lambda: "unknown")())   #returns "unknown"
relay4  =4
relay22 =22
relay6  =6
relay26 =26
chip = gpiod.Chip('gpiochip0')
led_line4 = chip.get_line(relay4)
led_line22 = chip.get_line(relay22)
led_line6 = chip.get_line(relay6)
led_line26 = chip.get_line(relay26)

led_line4.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
led_line22.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
led_line6.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
led_line26.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
try:
   while True:
       led_line4.set_value(1)	#on
       time.sleep(1)
       led_line4.set_value(0)	#off
       time.sleep(1)
       
       led_line22.set_value(1)	#on
       time.sleep(1)
       led_line22.set_value(0)	#off
       time.sleep(1)
       
       led_line6.set_value(1)	#on
       time.sleep(1)
       led_line6.set_value(0)	#off
       time.sleep(1)
       
       led_line26.set_value(1)	#on
       time.sleep(1)
       led_line26.set_value(0)	#off
       time.sleep(1)
finally:
   led_line4.release()
   led_line22.release()
   led_line6.release()
   led_line26.release()

###################This is old way for RPi4 and probably RPi3###########################
#import GPIOD as GPIO 
#GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
#RELAIS_2_GPIO = 4  #Light
#GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode
#GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # off
#GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # on

#RELAIS_3_GPIO = 22  #
#GPIO.setup(RELAIS_3_GPIO, GPIO.OUT) # GPIO Assign mode
#GPIO.output(RELAIS_3_GPIO, GPIO.LOW) # off
#GPIO.output(RELAIS_3_GPIO, GPIO.HIGH) # on
 
#RELAIS_4_GPIO = 6   #
#GPIO.setup(RELAIS_4_GPIO, GPIO.OUT) # GPIO Assign mode
#GPIO.output(RELAIS_4_GPIO, GPIO.LOW) # off
#GPIO.output(RELAIS_4_GPIO, GPIO.HIGH) # on

#RELAIS_5_GPIO = 26  #
#GPIO.setup(RELAIS_5_GPIO, GPIO.OUT) # GPIO Assign mode

#######################Logging when running script live (crontab) for trouble shooting###############################
#setup logging basic configuration for logging to a file
#logging.basicConfig( /home/dw00621/Automatic_chicken.py = 'chicken.log')    
#logging.basicConfig(filename = 'chicken.log', filemode='w', level=logging.info)   #w mode means it will rewrite the file each time it is called
#logging.basicConfig(filename = 'chicken.log'
#                    level=logging.INFO)
#                    format='%(asctime)s %(message)s')
#logging.basicConfig(filename = 'chicken.log')
#loglevel = logging.info
#name = 'ss_plus'
#logging.info('%s', name)

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

##################################################################
#################################################################################


    
###############How to see contents of txt from terminal###########
#cat output.txt    #This allows you to see print from script via SSH
#tail /var/log/syslog      #to confirm application is running    

###############Terminal Commands to run script every minute of every day#############

#crontab - e     #enables editing of the cron file in Nano   
#* * * * * python3 /home/dw00621/Automatic_chicken.py >> python3 /home/dw00621/output.txt 2>&1
###The above also writes to output.txt from troubling shooting crontab    
### cntl o, then enter, then control x to save the crontab
# from terminal window type: tail /var/log/syslog   #is useful for seeing if the crontab is running 

# from terminal window type: chmod a+r+x Automatic_chicken.py to give all users permission to read and execute the file
# from terminal window type: chmod a+r output.txt to give all users permission to read the file

###Can try this in crontab to see if it runs every 15 seconds (both line must be included in crontab:
#* * * * * python3 /home/dw00621/Automatic_chicken.py >> python3 /home/dw00621/output.txt
#* * * * * ( sleep 15 ; python /home/dw00621/Documents/Automatic_chicken.py) #supposed to run every 15 seconds
#WLAN IP address for SSH with putty: 192.168.4.43  
