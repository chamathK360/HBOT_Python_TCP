import math
from socket import *
import time
counter = 0
angle1 = [0]
angle2 = [0]

#X====  1700  -1300
#Y====  4300  -4300

filepath = '/Users/macbookm1/Documents/Final_machine_Control_Sorce/Python_HBOT/code.txt' #Change Location Due to your Parameters

address = ('169.254.88.53', 8888)  # match arduino IP + port
client_socket = socket(AF_INET, SOCK_DGRAM)
print(address)
client_socket.settimeout(10)  # wait up to 5 seconds

# Motor parameters
r = 27.5/2

def forward(theta1, theta2):
    x = 0.5 * (theta1 + theta2) /((10000/30)/(2* math.pi * r))
    y = 0.5 * (theta1 - theta2) /((10000/30)/(2* math.pi * r))
    return [x, y]


def inverse(displacement_x, displacement_y):

#   1 turn -> 18 * 5 mm (Liner movement)

    motor1_angle = (displacement_x + displacement_y)*(10000/30)/(2* math.pi * r)
    motor2_angle = (displacement_x - displacement_y )*(10000/30)/(2* math.pi * r)
    return motor1_angle, motor2_angle
    #Y+ up #X+ up #Y- up  #X- up

while(True):

    time.sleep(0.1)
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            txt = "{}".format(line.strip())
            a = txt.split()
            if 3 < len(a):  # check the array location is availbe
                F = a[2].split("F", 1)
                A = a[3].split("A", 1)
            if a:
                if (a[0])[0] == 'X':
                    x = a[0].split("X", 1)
                    y = a[1].split("Y", 1)
                    coordinate = inverse(float(x[1]),float(y[1]))
                    print(forward(coordinate[0] , coordinate[1]))
                    a = round(coordinate [0],2)
                    b = round(coordinate [1],2)
                    print(a,b,F[1],A[1])
                    client_socket.sendto(('a' + str(a) + ' b' + str(b)+ ' F' + str(F[1]) + ' A' + str(A[1])).encode(), address)
                    time.sleep(0.1)
                else:
                    if (a[0])[0] == "A":
                        a = txt.split()
                        gr = a[1]
                        delay = a[2]
                        if gr == "TIME":
                            # print("TIME :" , (int(del_pre)+int(delay))/1000 )
                            full_time = (int(del_pre)+int(delay))/1000 + full_time
                            del_pre = 0
                        time.sleep(int(delay)/1000)
    print();  
  



                                       

  







