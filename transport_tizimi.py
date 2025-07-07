import time
from os import system as sys
sys('cls')

class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def show_info(self):
        print(f'\nMashina ma\'lumotlari: \n\nMashina nomi: {self.name}\nMashina modeli: {self.model}\nMashina yili: {self.year}')

class MoreInfo(Car):
    def __init__(self, name, model, year, color, driver, carID):
        super().__init__(name, model, year)
        self.color = color
        self.driver = driver
        self.__carID = carID
 
    def show_info(self):
        super().show_info()
        print(f'Mashina rangi: {self.color}\nMashina haydovchisi: {self.driver}\nMashina raqami: {self.__carID}')
    
class DriveCar(MoreInfo):
    def __init__(self, maxspeed, minspeed, acceleration, deceleration, driver):
        self.driver = driver
        self.deceleration = deceleration
        self.acceleration = acceleration
        self.maxspeed = maxspeed
        self.minspeed = minspeed
        self.speed_start = 0

    def startcar(self):
        print(f'\n{self.driver}, sizning avtomobilingiz o\'t oldi')

    def stopcar(self):
        print(f'\n{self.driver}, sizning avtomobilingiz to\'xtadi')

    def accelerate(self):
        while self.speed_start < self.maxspeed:
            self.speed_start += self.acceleration
            print(f'Hozirgi tezlik: {self.speed_start} km/h')
            if self.speed_start == self.maxspeed:
                print(f'Tezlik {self.maxspeed} km/h tezlikka yetdi')
                break

    def decelerate(self):
        while self.speed_start > self.minspeed:
            self.speed_start -= self.deceleration
            print(f'Hozirgi tezlik: {self.speed_start} km/h')
            if self.speed_start == self.maxspeed:
                print(f'Tezlik {self.minspeed} km/h tezlikka yetdi')
                break

    def turnright(self):
        print('\nMashina o\'ngga burildi')

    def turnleft(self):
        print('\nMashina chapga burildi')

while True:
    name = input('\nMashina nomini kiriting: ')
    model = input('Mashina modelini kiriting: ')
    year = int(input('Mashina yilini kiriting: '))
    color = input('Mashina rangini kiriting: ')
    driver = input('Ism familiyangizni kiriting: ')
    carID = input('Mashina raqamini kiriting: ')
    
    print(f'\nMashinangiz tizimga muvaffaqiyatli qo\'shildi, {driver}')

    haydovchi = MoreInfo(name, model, year, color, driver, carID)
    haydovchi.show_info()

    time.sleep(3)

    sys('cls')

    driver = driver
    maxspeed = 0
    minspeed = 0
    acceleration = 0
    deceleration = 0

    haydash = DriveCar(maxspeed, minspeed, acceleration, deceleration, driver)

    start = input('Mashina ishga tushirilsinmi?(h/y): ')
    if start.lower() == 'h':
        haydash.startcar()
        while True:
            choice = input('\nTanlovingizning raqamini kiriting: \n1. Tezlikni oshirish\n2. Tezlikni kamaytirish\n3. O\'ngga burish\n4. Chapga burish\n5. Mashinani to\'xtatish\n\n>>>>> ')
            if choice == '1':
                maxspeed = int(input('\nTezlik chegarasini kiriting: '))
                acceleration = int(input('Tezlanishni kiriting: '))
                haydash.maxspeed = maxspeed
                haydash.acceleration = acceleration
                haydash.accelerate()
            if choice == '2':
                minspeed = int(input('\nTezlik chegarasini kiriting: '))
                deceleration = int(input('Sekinlanish tezligini kiriting: '))
                haydash.minspeed = minspeed
                haydash.deceleration = deceleration
                haydash.decelerate()
            if choice == '3':
                haydash.turnright()
            if choice == '4':
                haydash.turnleft()
            if choice == '5':
                haydash.stopcar()

            Continue = input('\nBoshqa amal bajarishni xohlaysizmi?(h/y): ')
            if Continue.lower() != 'h':
                break

    else: break
# ustoz 13.68% ChatGPT ishlatilgan deb chiqardi lekin 100% o'zim yozdim faqat vaqtni to'xtatishni so'radim xolos 
