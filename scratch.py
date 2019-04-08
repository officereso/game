save = open("save1.txt")

temp = save.readline()
temp.split(' ')
temp1 = int(temp[0])
temp2 = int(temp[2])
temp3 = int(temp[4])
temp = temp1, temp2, temp3
print(temp)
