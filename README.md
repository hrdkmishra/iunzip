# iunzip

##Running a Python Script in the Background

First, you need to add a shebang line in the Python script which looks like the following:

>#!/usr/bin/env python3
This path is necessary if you have multiple versions of Python installed and /usr/bin/env will ensure that the first Python interpreter in your $$PATH environment variable is taken. You can also hardcode the path of your Python interpreter (e.g. #!/usr/bin/python3), but this is not flexible and not portable on other machines. Next, you’ll need to set the permissions of the file to allow execution:

>chmod +x test.py
Now you can run the script with nohup which ignores the hangup signal. This means that you can close the terminal without stopping the execution. Also, don’t forget to add & so the script runs in the background:

>nohup /path/to/test.py &
If you did not add a shebang to the file you can instead run the script with this command:

>nohup python /path/to/test.py &
The output will be saved in the nohup.out file, unless you specify the output file like here:

>nohup /path/to/test.py > output.log &
>nohup python /path/to/test.py > output.log &
If you have redirected the output of the command somewhere else - including /dev/null - that's where it goes instead.

## doesn't create nohup.out

>nohup command >/dev/null 2>&1   
If you're using nohup, that probably means you want to run the command in the background by putting another & on the end of the whole thing:

## runs in background, still doesn't create nohup.out

>nohup command >/dev/null 2>&1 &  
You can find the process and its process ID with this command:

>ps ax | grep test.py

## or
## list of running processes Python

>ps -fA | grep python
>ps stands for process status

If you want to stop the execution, you can kill it with the kill command:

>kill PID

**this project is made in python3
  to create fill extraction automation to the desired location and deleting the main compressed file
  works best in linux**
