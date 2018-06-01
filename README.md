# Data Reader version for python 2 compatibility

## Setting up the RaspberryPi to run the script

Navigate to the /etc/rc.local file and type the following in a line below
/yourpath/bin/yourscript.sh &

Then in yourscript.sh put:
#!/bin/sh
(sleep 10; python /path_to_python_file/src/main.py