listofnum = [x for x in range(0,1000)]
counter = 0
for i in listofnum:
    print(f"{str(i):>6}",end="")
    counter += 1
    if counter == 10:
        print()
        counter = 0