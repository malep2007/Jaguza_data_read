import random
import serial
import config
import time
import requests



def check_port_is_available():
    try:
        ser = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE, timeout=config.PORT_READ_TIMEOUT)
        ser.close()
        return True
    except serial.serialutil.SerialException:
        return False


def listen_process():
    serial_port = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE, timeout=config.PORT_READ_TIMEOUT)
    # log_id = 1
    while True:
        data_read = serial_port.readline()

        if data_read:
            incoming = data_read.decode("utf-8")
            incoming = incoming.strip()
            print("Received: {}".format(incoming))
            
            
            
            serialindex = incoming.index("SN")
            deviceSerial = incoming[serialindex+2:serialindex+7]
            print("DEVICESERIAL: {}".format(deviceSerial))
            
        
            latindex = incoming.index("LAT")
            latitude = incoming[latindex+3:latindex+11]
            print("LATITUDE: {}".format(latitude))
            
        
            longindex = incoming.index("LONG")
            longitude = incoming[longindex+4:longindex+13]
            print("LONGITUDE: {}".format(longitude)) 
            
            
            timedatestr = time.asctime()
            logtime = timedatestr[11:19]
            logdate = timedatestr[0:10] + ' ' + timedatestr[20:24]
            print("TIME: {}".format(logtime)) 
            print("TIME: {}".format(logdate)) 
            
            filestr = str(serialindex)+ ','+ str(latitude)+ ','+ str(longitude)+ ','+ str(logtime) + ','+ str(logdate)
            
            # print("log_message: {}".format(log_message))
            datafile = open("logs.csv", 'a')
            datafile.write(filestr + "\n")
            datafile.close()

            # log_id += 1
