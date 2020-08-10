'''
We sell the lemonade and each lemonade is 5dollars.
the customer always comes with 5, 10 or 20 dollars bills
you are suppose to give a change if payment is higher than 5.
if you have all change until end return true else return false
'''

given = [5,5,10,20,5]


def buy_and_change(arr):
    fives = 0
    tens = 0
    for i in range(len(arr)):
        if arr[i] == 5:
            fives += 1
        elif arr[i] == 10:
            tens += 1
            fives -= 1
        elif arr[i] == 20:
            if tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3

        if fives < 0 or tens < 0:
            return False
    return True

res = buy_and_change(given)
print(res)