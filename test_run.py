 
import time
count=0

while count < 30:
    now_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    count+=1
    print(count,now_time)
    time.sleep(1)