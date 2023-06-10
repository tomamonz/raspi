import sys
import time
from grove.gpio import GPIO

class GroveVibrationSensor(object):
    def __init__(self, pin):
        self.dio = GPIO(pin)

    def get_frequency(self):
        count = 0
        interval = 1  # Pomiar trwa przez 1 sekundę
        start_time = time.time()

        self.dio.dir(GPIO.IN)
        while time.time() - start_time < interval:
            if self.dio.read():
                count += 1
                while self.dio.read():
                    pass  # Czekaj, aż sygnał wróci do stanu niskiego

        frequency = count / interval
        return frequency

def main():
    if len(sys.argv) < 2:
        print('Usage: {} pin_number'.format(sys.argv[0]))
        sys.exit(1)

    vibration_sensor = GroveVibrationSensor(int(sys.argv[1]))

    print('Detecting vibration frequency...')
    while True:
        freq = vibration_sensor.get_frequency()
        if freq >= 0.1 and freq <= 180:
            print('{:.2f} Hz'.format(freq))
        else:
            print('0 Hz')  # Wartość zerowa, jeśli nie wykryto wibracji
        time.sleep(0.1)  # Opoznienie miedzy odczytami

if __name__ == '__main__':
    main()



# Detecting vibration frequency...
# 0 Hz
# 0 Hz
# 0 Hz
# 0 Hz
# 3.00 Hz
# 24.00 Hz
# 10.00 Hz
# 4.00 Hz
# 0 Hz
# 3.00 Hz
# 9.00 Hz
# 6.00 Hz
# 17.00 Hz
# 39.00 Hz
# 1.00 Hz
# 2.00 Hz
# 0 Hz
# 66.00 Hz
# 71.00 Hz
# 0 Hz
# 0 Hz
# 7.00 Hz
# 0 Hz
# 0 Hz
# 0 Hz
