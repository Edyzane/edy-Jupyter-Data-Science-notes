span = ["cat","bat","rat","elephant"]

print(span[0:-1])
print(span[-3])
print(span[1:3])
print(span[0:4])
print(span[1:])
print(span[:])

print(span[-1])
print(span[-3])

print("the " + span[-1] + " is afraid of the " + span[-3] + ".")

print(span[0])
print(span[3])

print("hello "+ span[1])


span1= [["cat","bat"],[10,20,30,40,50]]
print(span1[0])
print(span1[0][1])
print(span1[1][4])


span = ["cat","bat","rat","elephant"]
span[1]="blyatman"
print(span[1])
span[0]=span[1]
print(span[0])
span[-1]="blyatman"
print(span[3])


a = [1,2,3,4]
b = ["a","b","c","d"]
c = a+b
d = a*3
print(c)
print(d)


a = [1,2,3,4]
del a[2]
print(a)
