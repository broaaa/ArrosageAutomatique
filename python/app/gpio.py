import json

electrovannesHerbe = {
    '2': "off",
    '3': "off"
}

electrovannesPotager = {
    '4': "off"
}

def stopElectrovannePotager():
    print('connecting to GPIO')
    print('Stopping Electrovanne potager')
    for electrovanne in electrovannesPotager:
        electrovannesPotager[electrovanne] = "off"
    print('exiting GPIO')
    print('-------------------------')
    return "stopped potager"

def stopElectrovanneHerbe():
    print('connecting to GPIO')
    print('Stopping Electrovanne herbe')
    for electrovanne in electrovannesHerbe:
        electrovannesHerbe[electrovanne] = "off"
    print('exiting GPIO')
    print('-------------------------')
    return "stopped herbe"

def stop_gpio():
    stopElectrovanneHerbe()
    stopElectrovannePotager()
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(2, GPIO.OUT,initial=GPIO.HIGH)
    # GPIO.setup(3, GPIO.OUT,initial=GPIO.HIGH)
    # GPIO.setup(4, GPIO.OUT,initial=GPIO.HIGH)
    # GPIO.output(2, GPIO.HIGH)
    # GPIO.output(3, GPIO.HIGH)
    
    # GPIO.output(4, GPIO.HIGH)
    # GPIO.cleanup() """
    return "stopped GPIO"

def startElectrovanneHerbe():
    print('connecting to GPIO')
    for electrovanne in electrovannesHerbe:
        print('connecting electrovanne ', str(electrovanne))
        print('starting electrovanne ', str(electrovanne))
        electrovannesHerbe[electrovanne] = "on"
    print('exiting GPIO')
    #GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
    #GPIO.output(electrovanne, GPIO.LOW)
    print('-------------------------')

def startElectrovannePotager():
    print('connecting to GPIO')
    for electrovanne in electrovannesPotager:
        print('connecting electrovanne ', str(electrovanne))
        print('starting electrovanne ', str(electrovanne))
        electrovannesPotager[electrovanne] = "on"
    print('exiting GPIO')
    #GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
    #GPIO.output(electrovanne, GPIO.LOW)
    print('-------------------------')

# def stop_electrovanne(number):
#     print('connecting to GPIO')
#     print('connecting electrovanne ', str(number))
#     #GPIO.setup(electrovanne, GPIO.OUT,initial=GPIO.HIGH)
#     print('stoping electrovanne ', str(number))
#     electrovannesMock[number] = "off"
#     #GPIO.output(electrovanne, GPIO.HIGH)
#     print('exiting GPIO')
#     print('-------------------------')

def get_status():
    print('returning GPIO status ')
    print('-------------------------')
    return {'herbe': electrovannesHerbe, 'potager': electrovannesPotager}
