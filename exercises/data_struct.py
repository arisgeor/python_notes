#! python3

count = 0

def powersOf3(n):
    global count
    count+=1
    if(n<1):
        return 0
    elif(n==1):
        print(1)
        return 1
    else:
        prev = powersOf3(n/3)
        curr = prev*3
        print(curr)
        return curr

powersOf3(150)
#print(count)
