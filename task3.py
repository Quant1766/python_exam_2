
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.

print(dataset)


def reByUser(phones = list(dataset.keys()), result = dict()):

    if phones==[]:
        return result

    hotels_dict = dataset[phones[0]]['hotels']

    count = len(hotels_dict.keys())

    result[phones[0]] = count


    return reByUser(phones[1:],result)



print("Task 3")

result = reByUser()

# result2 = recursionByUsers(dataset,list(dataset.keys()))
# result2 = recursionByUsers()
print(result)

print("\n\n")



# print(result2)