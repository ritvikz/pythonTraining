'''What is an Exception?
An exception is an error that occurs during program execution.
If not handled, it stops your program.
Below is an exercise 
'''



ItemsInCart = 0
def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")
    elif ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")
    else:
        ItemsInCart += items_to_add
        print(f"{items_to_add} items added. Total in cart: {items_to_add}")

try:
    add_to_cart(2)
    add_to_cart(-1)
except Exception as e:
    print(e)