import subprocess
import slave

mylist = [1,2,3,4,5,6]

for i in mylist:
    #subprocess.run(["python3", "slave.py", str(i)])
    slave.myfunk(str(i))
    
