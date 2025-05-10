flag = False
while not flag:
    x = input("Give number ")
    try:
        x = int(x)
        flag = True
    except:
        flag = False