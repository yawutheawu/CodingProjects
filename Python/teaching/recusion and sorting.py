def fib(n,memo={0:1,1:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
        return memo[n]

def lucas(n,memo={0:2,1:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = fib(n-1,memo) + fib(n-2,memo)
        return memo[n]

def padovan(n,memo={0:1,1:1,2:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = padovan(n-2,memo) + padovan(n-3,memo)
        return memo[n]

termsToPrint = 25

print(f"Fibonacci ({25}):")
count = 0
for i in range(termsToPrint):
    if count < 10:
        print(fib(i), end=", ")
        count += 1
    else:
        print(str(fib(i))+",")
        count =0
    
print("\n--------------------------")
print(f"Lucas ({25}):")
count = 0
for i in range(termsToPrint):
    if count < 10:
        print(lucas(i), end=", ")
        count += 1
    else:
        print(str(lucas(i))+",")
        count = 0
print("\n--------------------------")
print(f"Padovan ({25}):")
count = 0
for i in range(termsToPrint):
    if count < 10:
        print(padovan(i), end=", ")
        count += 1
    else:
        print(str(padovan(i))+",")
        count = 0
print("\n--------------------------")
def custom(n,memo={0:3,1:2,2:3}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = (custom(n-1,memo)*custom(n-3,memo)) - custom(n-2,memo)
        return memo[n]

print(f"Custom Sequence ({25}):")
count = 0
for i in range(termsToPrint):
    if count < 10:
        print(custom(i), end=", ")
        count += 1
    else:
        print(str(custom(i))+",")
        count = 0
print("\n--------------------------")
def bubblesort(inList):
    inputlist = inList.copy()
    for iter_num in range(len(inputlist)-1,0,-1):
        for idx in range(iter_num):
            if inputlist[idx]>inputlist[idx+1]:
                temp = inputlist[idx]
                inputlist[idx] = inputlist[idx+1]
                inputlist[idx+1] = temp
    return inputlist

def merge_sort(unsorted_list):
   if len(unsorted_list) <= 1:
      return unsorted_list
# Find the middle point and devide it
   middle = len(unsorted_list) // 2
   left_list = unsorted_list[:middle]
   right_list = unsorted_list[middle:]

   left_list = merge_sort(left_list)
   right_list = merge_sort(right_list)
   return list(merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      print(f"Left: {left_half}, Right: {right_half}")
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   print(f"Merged: {res}")
   return res


x = [fib(x) for x in range(11,0,-1)]
