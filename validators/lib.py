
"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getUserPhone():

    user_input = input("Entet phone number: ")

    while not (re.match(r"^\(\d{3}\)-\d{3}-\d{4}$", user_input) ):
        user_input = input("Entet phone number: ")
    return user_input
    # else:
    #     return False


"""
    Написати валідатор ....
    Правило валідації
"""

# def getProductName():
#     #TODO



"""
    Написати валідатор ....
    Правило валідації
"""


def getHotelPrice():
    user_input = input("Entet price: ")

    while not (re.match(r"^\d{4}$", user_input)):
        user_input = input("Entet price: ")
    return  user_input
