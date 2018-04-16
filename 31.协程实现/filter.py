import time
def follow(thefile, target):
    thefile.seek(0,2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # Sleep briefly
            continue
        print "Did you send the data to the coroutine?"
        target.send(line)
 
#@coroutine
def printer():
 while True:
    line = (yield)
    print line
    
#@coroutine
def grep(pattern,target):
    while True:
        line = (yield) # Receive a line
        if pattern in line:
            target.send(line) # Send to next stage
            
if __name__ == "__main__":
    f = open("access-log")
    print "open successful!!"
    follow(f,grep('python',printer()))