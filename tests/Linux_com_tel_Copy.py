import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def move(direction,speed,duration):
    if direction=='up':
        ser.write(bytes([80, 2, 17, 36, speed, 0, 0, 0]))
    elif direction=='down':
        ser.write(bytes([80, 2, 17, 37, speed, 0, 0, 0]))
    elif direction=='left':
        ser.write(bytes([80, 2, 16, 37, speed, 0, 0, 0]))
    elif direction=='right':
        ser.write(bytes([80, 2, 16, 36, speed, 0, 0, 0]))

    ser.read(1)
    time.sleep(duration)

    if direction=='up' or direction=='down':
        ser.write(bytes([80, 2, 17, 36, 0, 0, 0, 0]))
    else:
        ser.write(bytes([80, 2, 16, 36, 0, 0, 0, 0]))
    
    ser.read(1)

move('down',9,1)

ser.close()