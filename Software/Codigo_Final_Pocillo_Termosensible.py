#Librerias:
import onewire
import machine
import ds18x20
from machine import RTC, I2C, Pin
from ssd1306 import SSD1306_I2C
import time


#Variables:

Pin_buzzer = 25 #Pin del buzzer
buzzer = machine.Pin(Pin_buzzer, machine.Pin.OUT)
oled = SSD1306_I2C(128, 64, I2C(0,scl=Pin(27), sda=Pin(26))) #Parametros de las dimensiones y la ubicacion de los pines
ds_pin = machine.Pin(32)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()

#Funciones:

def dibujar_carita_feliz():
    oled.fill(0)  # Limpia el display (fondo negro)
    # Dibuja el rostro (círculo)
    oled.fill_rect(55, 10, 70, 50, 1)
    # Dibuja los ojos (círculos)
    oled.fill_rect(75, 25, 10, 10, 0)  # Ojo izquierdo (fondo negro)
    oled.fill_rect(105, 25, 10, 10, 0)  # Ojo derecho (fondo negro)
    # Dibuja la boca (arco)
    oled.fill_rect(70, 45, 40, 10, 0)# Boca (fondo negro)
    oled.fill_rect(80, 45, 20, 5, 1) #Curva pa la sonrisa (Fondo Azul)
    oled.show()  # Actualiza el display
def dibujar_carita_triste():
    oled.fill(0)  # Limpia el display (fondo negro)
    # Dibuja el rostro (círculo)
    oled.fill_rect(55, 10, 70, 50, 1)
    # Dibuja los ojos (círculos)
    oled.fill_rect(75, 25, 10, 10, 0)  # Ojo izquierdo (fondo negro)
    oled.fill_rect(105, 25, 10, 10, 0)  # Ojo derecho (fondo negro)
    # Dibuja la boca (arco)
    oled.fill_rect(70, 45, 40, 10, 0)# Boca (fondo negro)
    oled.fill_rect(80, 50, 20, 5, 1) #Curva de la boca triste (Fondo Azul)
    oled.show()  # Actualiza el display
def dibujar_carita_normal():
    oled.fill(0)  # Limpia el display (fondo negro)
    # Dibuja el rostro (círculo)
    oled.fill_rect(55, 10, 70, 50, 1)
    # Dibuja los ojos (círculos)
    oled.fill_rect(75, 25, 10, 10, 0)  # Ojo izquierdo (fondo negro)
    oled.fill_rect(105, 25, 10, 10, 0)  # Ojo derecho (fondo negro)
    # Dibuja la boca (arco)
    oled.fill_rect(70, 45, 40, 10, 0)# Boca (fondo negro)
    oled.show()  # Actualiza el display
def encender_buzzer():
    buzzer.value(1)
def apagar_buzzer():
    buzzer.value(0)
def ciclo_buzzer_1():
    encender_buzzer()
    time.sleep(1)
    apagar_buzzer()
def temperatura_fria():
    while True:
        dibujar_carita_normal()
        ds_sensor.convert_temp()
        for rom in roms:
            temperatura = ds_sensor.read_temp(rom)
        if float(temperatura) > 25:
            break
        oled.text("Temp:",0,20)
        oled.text("{}C".format(round(float(temperatura), 2)),0,40)
        oled.show()
        time.sleep(1)
        

def temperatura_media():
    while True:
        dibujar_carita_feliz()
        ds_sensor.convert_temp()
        for rom in roms:
            temperatura = ds_sensor.read_temp(rom)
        if float(temperatura) > 50:
            break
        if float(temperatura) <= 25:
            break
        oled.text("Temp:",0,20)
        oled.text("{}C".format(round(float(temperatura), 2)),0,40)
        oled.show()
        time.sleep(1)
        
        
def temperatura_caliente():
    while True:
        dibujar_carita_triste()
        ds_sensor.convert_temp()
        for rom in roms:
            temperatura = ds_sensor.read_temp(rom)
        if float(temperatura) < 50:
            break
        oled.text("Temp:",0,20)
        oled.text("{}C".format(round(float(temperatura),2)),0,40)
        oled.show()
        time.sleep(1)

#Ciclo principal

while True:
    temperatura_fria()
    ciclo_buzzer_1()
    temperatura_media()
    ciclo_buzzer_1()
    temperatura_caliente()
    ciclo_buzzer_1()




