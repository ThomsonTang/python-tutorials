import time

localTime = time.gmtime(1516328612000)
localTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)

print("time: ", localTime)
