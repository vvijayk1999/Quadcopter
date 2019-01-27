import paho.mqtt.client as mqttClient
import time




#----------------------------------------------------------------------
broker_address= "your server"
port = 187xx
user = "your username"
password = "yourr password"
topic = "your topic"
instance = "your instance"
#----------------------------------------------------------------------



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

try:
    while True:

        value = input('Enter the message:')
        client.publish(topic,value)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()
