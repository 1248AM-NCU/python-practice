from ast import If


def hello():
    """a function that prints hello"""
    print("Hello")

def pack(x, y, z):
    """description here"""
    return [x,y,z]

def eat_lunch(li):
    """Eat the list of items"""
    if len(li) == 0:
        print("My lunchbox is empty!")
        return
    isFirst = True
    for i in li:
        if isFirst:
            print(f"First I eat {i}")
            isFirst = False
        else:
            print(f"Then I eat {i}")
