# return masked string

#my first solution 
def maskify(cc):  
    lst = list(cc)
    for i in range(len(lst)-4):
        lst[i] = "#"
    return "".join(lst)

#better solution
def maskify2(cc):
	return '#'*(len(cc)-4)+cc[-4:]

string = "This is a string i wanna keep safe"
maskify(string)
maskify2(string)
print('Complete!')