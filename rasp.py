import RPi.GPIO as GPIO
import paho.mqtt.client as mqttClient
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

broker_address= "m16.cloudmqtt.com"
port = 18767
user = "axnykpge"
password = "rvWvVARZSkIN"
topic = "Test"
instance = "Quadcopter"


////////////////////////////////////// First call for initial distance //////////////////////////////////////////////

int_dis=0
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(2)
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)
while GPIO.input(ECHO)==0:
  pulse_start = time.time()
while GPIO.input(ECHO)==1:
  pulse_end = time.time()
pulse_duration = pulse_end - pulse_start
int_dis = pulse_duration * 17150
int_dis = round(int_dis, 2)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

Connected = False   #global variable for the state of the connection
client = mqttClient.Client(instance)               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)



while True:
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)
	time.sleep(0.5)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
 		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
  		pulse_end = time.time()
	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	distance = int(distance)
	print "Distance:",distance,"cm"
	print(distance-int_dis)
	if((distance-int_dis)>=5):
        try:
            client.publish(topic,"420")
        except KeyboardInterrupt:
            client.disconnect()
            client.loop_stop()
