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
        print(data_read)

        if data_read:
            incoming = data_read.decode('utf-8')
            incoming = incoming.strip()
            print("Received: {}".format(incoming))    
            print(incoming.find('RELAY'))  
            if incoming.find('RELAY') == -1:
                
                serialindex = incoming.index("SN")
                deviceSerial = incoming[serialindex:serialindex+7]
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
                print("DATE: {}".format(logdate)) 
                
                recvstr = deviceSerial + 'RECIEVED'
                serial_port.write(recvstr.encode('UTF-8') + b"\n")
                
                print("Sending to CSV")
                
                filestr = str(deviceSerial) + ','+ str(latitude)+ ','+ str(longitude)+ ','+ str(logtime) + ','+ str(logdate)
                print(filestr)
                
                ''''
                postrequest = 'http://jaguzalivestockug.com/mobileapp/api/?cmd=devicelocation&device=' 
                postrequest += str(deviceSerial)
                postrequest += '&latitude='
                postrequest += str(latitude)
                postrequest += '&longitude='
                postrequest += str(longitude)
                postrequest += '&time='
                postrequest += str(logdate) + ' '+ str(logtime)'''
                
                jaguzaurl = 'http://jaguzalivestockug.com/mobileapp/api/'
                
                jaguzadata = {
                        'cmd' : 'devicelocation',
                        'device' : str(deviceSerial),
                        'latitude' : str(latitude),
                        'longitude' : str(longitude),
                        'time' : str(logdate) + ' '+ str(logtime),
                        }
                
                response = requests.post(url = jaguzaurl, data = jaguzadata)
                
                print(response.content)
                
                # print("log_message: {}".format(log_message))
                datafile = open("logs.csv", 'a')
                datafile.write(filestr + "\n")
                datafile.close()
                
                

