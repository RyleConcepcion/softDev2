import serial
import time

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=1)

while True:
    command = input("Enter input: ")
    if command in ["lights on", "lights off"]:
        arduino.write(f"{command}\n" on.encode())
        time.sleep(1)
    else:
        print ("Lights Off")