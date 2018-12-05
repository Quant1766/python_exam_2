from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import getUserPhone,getHotelPrice


from task1 import addUserHotels


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserProductValidator():
    price = getHotelPrice()

    user_name = getUserPhone()

    hotel_name = input("Enter hotelname: ")

    addUserHotels(user_name, hotel_name, price)



print("Task 2")
addUserProductValidator()
print(dataset)


print("\n\n")