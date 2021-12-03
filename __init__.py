from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import serial
import time
import subprocess

class solaireSkill(MycroftSkill):

    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')

    @intent_handler('sun.intent')
    def handle_not_are_you_intent(self, message):
        self.speak_dialog("sun")
        serA = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        serA.flush()
        serA.write(b"sun")
        serB = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        serB.flush()
        serB.write(b"sun")        
        serC = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
        serC.flush()
        serC.write(b"sun")
        #serD = serial.Serial('/dev/ttyACM3', 9600, timeout=1)
        #serD.flush()
        #serD.write(b"sun")    

    def stop(self):
        pass

def create_skill():
    return solaireSkill()
