import webbrowser
import time

total_breaks = 4
count = 0

print("break_time initiated at "+time.ctime())
while (count < total_breaks):
    time.sleep(7200)
    webbrowser.open_new("https://www.youtube.com/watch?v=hVbp9b57zXY")
    count = count + 1

    
