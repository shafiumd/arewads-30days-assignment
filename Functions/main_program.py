import car_functions
from car_functions import make_car
from car_functions import make_car as create_car
import car_functions as cf
from car_functions import *

car1 = car_functions.make_car('Toyota', 'Camry', color='blue')

car2 = make_car('Honda', 'Civic', year=2023)

car3 = create_car('Ford', 'Mustang', color='red')

car4 = cf.make_car('Chevrolet', 'Malibu', fuel_type='hybrid')

car5 = make_car('Nissan', 'Altima', transmission='automatic')

print("Approach 1:", car1)
print("Approach 2:", car2)
print("Approach 3:", car3)
print("Approach 4:", car4)
print("Approach 5:", car5)
