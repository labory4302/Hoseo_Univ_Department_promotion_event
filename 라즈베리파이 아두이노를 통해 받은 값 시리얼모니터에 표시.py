import serial
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.image as mpimg
import matplotlib
import numpy
ser = serial.Serial('/dev/ttyACM0',9600)
ser.baudlate = 9600

rows = 2
cols = 1

def showtime1():
        Now = time.localtime()
        Real_Year = str(Now.tm_year)
        Real_Month = str(Now.tm_mon)
        Real_Day = str(Now.tm_mday)
        Real_Hour = str(Now.tm_hour)
        Real_Minute = str(Now.tm_min)
        Real_Second = str(Now.tm_sec)
        print(Real_Year+"/" +Real_Month+"/"+Real_Day+"   "+Real_Hour+":"+Real_Minute+":"+Real_Second+"   데이터 수신 대기중...\n\n")

def showtime2():
        Now = time.localtime()
        Real_Year = str(Now.tm_year)
        Real_Month = str(Now.tm_mon)
        Real_Day = str(Now.tm_mday)
        Real_Hour = str(Now.tm_hour)
        Real_Minute = str(Now.tm_min)
        Real_Second = str(Now.tm_sec)
        print(Real_Year+"/" +Real_Month+"/"+Real_Day+"   "+Real_Hour+":"+Real_Minute+":"+Real_Second+"   데이터가 수신되었습니다! 데이터를 분석중입니다...\n\n")

def result(a, arr, name, data):
        showtime2()
        time.sleep(2)
        print("데이터를 보낸 사람 : "+name)
        print("메시지 : "+data+"\n\n")
        
        print(a, end ="\n")
        print("가방일 확률 : "+arr[0])
        print("의자일 확률 : "+arr[1])
        print("볼펜일 확률 : "+arr[2])
        print("사람일 확률 : "+arr[3])
        print("핸드폰일 확률 : "+arr[4]+"\n\n\n")
        
        
        img = mpimg.imread('logo.bmp')
        percent = [float(arr[0]),float(arr[1]),float(arr[2]),float(arr[3]),float(arr[4])]
        label = ["Bag", "Chair", "Pen", "People", "Phone"]
        
        fig = plt.figure(figsize=(9,9))
        rows = 2
        cols = 1
        
        move_figure(fig, 960, 0)
        
        ax1 = fig.add_subplot(rows, cols, 1)
        ax1.set_position([0.07, 0.23, 0.90, 0.7])
        plt.rcParams["font.family"] = 'Malgun Gothic'
        plt.rcParams["font.size"] = 12
        x = numpy.arange(len(label))
        
        plt.bar(x-0.0, percent, label='percentage', width=0.5, color=['#ef7e4d', '#efae4d', '#efdf4d', '#cfef4d', '#9eef4d'])
        plt.xticks(x, label, size = 15)
        plt.ylabel('percent', size = 15)
        plt.ylim(0, 100)
        
        ax2 = fig.add_subplot(rows, cols, 2)
        ax2.imshow(img)
        ax2.axis('off')
        ax2.set_position([0.02, 0, 0.96, 0.2])
        plt.show()
        

def move_figure(f, x, y):
        backend = matplotlib.get_backend()
        if backend == 'TkAgg':
                f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
        elif backend == 'WXAgg':
                f.canvas.manager.window.SetPosition((x, y))
        else:
                f.canvas.manager.window.move(x, y)


while(1):
	c = ser.readline()
	receive = c[:-2].decode()
	tmp = receive.split(',');

	if(tmp[0]=="1"):
		a = "이것은 가방입니다"
		arr = [tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
		name = tmp[6]
		data = tmp[7]
		result(a, arr, name, data)
		tmp[0] = 0

	elif(tmp[0]=="2"):
		a = "이것은 의자입니다"
		arr = [tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
		name = tmp[6]
		data = tmp[7]
		result(a, arr, name, data)
		tmp[0] = 0

	elif(tmp[0]=="3"):
		a = "이것은 펜입니다"
		arr = [tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
		name = tmp[6]
		data = tmp[7]
		result(a, arr, name, data)
		tmp[0] = 0

	elif(tmp[0]=="4"):
		a = "이것은 사람입니다"
		arr = [tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
		name = tmp[6]
		data = tmp[7]
		result(a, arr, name, data)
		tmp[0] = 0

	elif(tmp[0]=="5"):
		a = "이것은 핸드폰입니다"
		arr = [tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
		name = tmp[6]
		data = tmp[7]
		result(a, arr, name, data)
		tmp[0] = 0

	elif(tmp[0]=="6"):
		a = "이것은 아무것도 아닙니다"
		arr = [tmp[1], tmp[2], tmp[3], tmp[4], tmp[5]]
		name = tmp[6]
		data = tmp[7]
		result(a, arr, name, data)
		tmp[0] = 0

	else:
                time.sleep(1)
                showtime1()
















