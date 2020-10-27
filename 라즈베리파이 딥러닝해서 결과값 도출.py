from PIL import Image
import os, glob, numpy as np
from keras.models import load_model
import tensorflow as tf
import serial
import time
from matplotlib import pyplot
import numpy
seed = 5
tf.set_random_seed(seed)
np.random.seed(seed)

image_w = 128
image_h = 128

pixels = image_h * image_w * 3

model = load_model('./model/image_classfication_school.model')

def sendtxt(k, c, input_name, input_mess):
    print("가방일 확률 :"+str(round(k[0]*100,4)))
    print("의자일 확률 :"+str(round(k[1]*100,4)))
    print("볼펜일 확률 :"+str(round(k[2]*100,4)))
    print("사람일 확률 :"+str(round(k[3]*100,4)))
    print("핸드폰일 확률:"+str(round(k[4]*100,4)))
    arduino.write(bytes(c.encode()))
    arduino.write(",".encode())
    arduino.write(str(round(k[0]*100,2)).encode())
    arduino.write(",".encode())
    arduino.write(str(round(k[1]*100,2)).encode())
    arduino.write(",".encode())
    arduino.write(str(round(k[2]*100,2)).encode())
    arduino.write(",".encode())
    arduino.write(str(round(k[3]*100,2)).encode())
    arduino.write(",".encode())
    arduino.write(str(round(k[4]*100,2)).encode())
    arduino.write(",".encode())
    arduino.write(bytes(input_name.encode()))
    arduino.write(",".encode())
    arduino.write(bytes(input_mess.encode()))
    time.sleep(3)


j = 0
for j in range(1,2):
    caltech_dir = "1.jpg"

    X = []
    filenames = []
    files = glob.glob(caltech_dir)
    arduino = serial.Serial('/dev/ttyACM1',9600)
    for i, f in enumerate(files):
        img = Image.open(f)
        img = img.convert("RGB")
        img = img.resize((image_w, image_h))
        data = np.asarray(img)
        
        filenames.append(f)
        X.append(data)
        
        X = np.array(X)
        X = X.astype(float) / 255
        
        prediction = model.predict(X)
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
        input_name = input('name :')
        input_mess = input('messages :')
        for k in prediction:
            if k[0] >= 0.9:
                c = '1'
                sendtxt(k, c, input_name, input_mess)
            elif k[1] >= 0.9:
                c = '2'
                sendtxt(k, c, input_name, input_mess)
            elif k[2] >= 0.9:
                c = '3'
                sendtxt(k, c, input_name, input_mess)
            elif k[3] >= 0.9:
                c = '4'
                sendtxt(k, c, input_name, input_mess)
            elif k[4] >= 0.9:
                c = '5'
                sendtxt(k, c, input_name, input_mess)
            else :
                c = '6'
                sendtxt(k, c, input_name, input_mess)

            percent = [k[0]*100,k[1]*100,k[2]*100,k[3]*100,k[4]*100]
            label = ["bag","chair","pen","people","phone"]
            pyplot.rcParams["font.family"] = 'Malgun Gothic'
            pyplot.rcParams["font.size"] = 12
            pyplot.rcParams["figure.figsize"] = (12,8)
            pyplot.figure()
            x = numpy.arange(len(label))

            pyplot.bar(x-0.0, percent, label='percentage', width=0.5, color='#dd0000')
            pyplot.xticks(x, label)

            pyplot.legend()
            pyplot.xlabel('judge')
            pyplot.ylabel('percent')
            pyplot.ylim(0, 100)
            pyplot.title('made by information and communication')

            pyplot.show()

 
