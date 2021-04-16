import json
import RPi.GPIO as GPIO

electrovannesHerbe = {
    2: "off",
    3: "off"
}

electrovannesPotager = {
    4: "off"
}

def init():
    GPIO.setmode(GPIO.BCM)

def stopElectrovannePotager():
    print('potager - connecting to GPIO')
    print('potager - stopping Electrovanne potager')
    for electrovanne in electrovannesPotager:
        print('potager - stoping electrovanne ', str(electrovanne))
        GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
        GPIO.output(electrovanne, GPIO.HIGH)
        electrovannesPotager[electrovanne] = "off"
    print('potager - exiting GPIO')
    print('-------------------------')
    return "stopped potager"

def stopElectrovanneHerbe():
    print('herbe - connecting to GPIO')
    print('herbe - stopping Electrovanne herbe')
    for electrovanne in electrovannesHerbe:
        print('herbe - stoping electrovanne ', str(electrovanne))
        GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
        GPIO.output(electrovanne, GPIO.HIGH)
        electrovannesHerbe[electrovanne] = "off"
    print('herbe - exiting GPIO')
    print('-------------------------')
    return "stopped herbe"

def stop_gpio():
    stopElectrovanneHerbe()
    stopElectrovannePotager()
    
    return "stopped GPIO"

def startElectrovanneHerbe():
    print('herbe - connecting to GPIO')
    for electrovanne in electrovannesHerbe:
        print('herbe - connecting electrovanne ', str(electrovanne))
        print('herbe - starting electrovanne ', str(electrovanne))
        GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
        GPIO.output(electrovanne, GPIO.LOW)
        electrovannesHerbe[electrovanne] = "on"
    print('exiting GPIO')
    print('-------------------------')

def startElectrovannePotager():
    print('potager - connecting to GPIO')
    for electrovanne in electrovannesPotager:
        print('potager - connecting electrovanne ', str(electrovanne))
        print('potager - starting electrovanne ', str(electrovanne))
        GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
        GPIO.output(electrovanne, GPIO.LOW)
        electrovannesPotager[electrovanne] = "on"
    print('exiting GPIO')
    print('-------------------------')

def get_status():
    print('returning GPIO status ')
    print('-------------------------')
    return {'herbe': electrovannesHerbe, 'potager': electrovannesPotager}
