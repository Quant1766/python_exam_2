from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію
print(dataset)

def addUserHotels(user_name, hotel_name, price):

    if user_name is None and hotel_name is None and price is None:
        return

    clients = list(dataset.keys())

    if user_name not in clients:
        dataset[user_name]={
        "hotels" : {
                    hotel_name: {"price":[price]},

        }

        }

        return



    hotels_client = list(dataset[user_name]['hotels'].keys())

    if hotel_name not in hotels_client:
        dataset[user_name]['hotels'][hotel_name]={"price":[price]}

        return


    dataset[user_name]['hotels'][hotel_name]['price'].append(price)



print("Task 1")
addUserHotels(user_name='(063)-603-7146', hotel_name='hostel1', price=300)

#Додати нового користувача та нову покупку
# addUserProduct(?,?,?)
#
# #Додати існуючому користувачу нову покупку нового продукту
# addUserProduct(?,?,?)
#
# #Додати існуючому користувачу нову покупку існуючого продукту
# addUserProduct(?,?,?)

print(dataset)


print("\n\n")