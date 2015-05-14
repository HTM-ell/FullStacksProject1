import webbrowser
import time
import sys

total_breaks = 3
break_counts = 0

print("This program started on " + time.ctime())
while(break_counts < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=eB_qJb_QKS4")
    break_counts+=1
    print("You have had " + str(break_counts) + " break(s)")

print("This program ended on " + time.ctime())
