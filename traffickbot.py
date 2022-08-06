import sys
import os
import webbrowser
import time
x = 1
link = input('enter link of site to traffic: ')
visit = 0
num = float(input('number of times to execute traffic: '))
while visit < num:
 visit += 1
# p = termux-open-url
# chrome_path = '/data/data/com.termux/files/home/python_projects/Chrome.app'
 webbrowser.open(f'{link}')
 time.sleep(2)
# webbrowser.open_new_tab(f'{link}')
# time.sleep(2)




# sys.exit()



#while True:
#  webbrowser.open(f'{link}')
#  time.sleep(15)
#	webbrowser.open_new_tab(f'{link}')
#	time.sleep(10)
#	webbrowser.open_new_tab(f'{link}')
#	time.sleep(10)	
#	webbrowser.open_new_tab(f'{link}')
#	time.sleep(10)
#	webbrowser.open_new_tab(f'{link}')
#	time.sleep(10)	
#	webbrowser.open_new_tab(f'{link}')
#	time.sleep(10)
#	x +=1

#while visit > num
