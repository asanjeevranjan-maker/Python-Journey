for x in reversed(range(1,my_time)):
    seconds= x %60
    minutes = int(x/60) %60
    hours = int(x/3600) %60
    time.sleep(1)
    print(f"The time remaining is {hours:.2f}:{minutes:.2f}:{seconds:.2f}")

#this is where , I am in python
