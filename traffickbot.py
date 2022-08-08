#import sys
#import os
import webbrowser
import time
#x = 1

try:
 link = input('enter link of site to traffic: ')
 visit = 0
 num = float(input('number of times to execute traffic: '))
 while visit < num:
  visit += 1
  webbrowser.open(f'{link}')
  time.sleep(2)
except KeyboardInterrupt:
 print ('you have exited the programme')
except ValueError:
 print ('must be a number')
