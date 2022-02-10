while True:
    name= input("enter your name : ")
    if  name != "joe":
        continue
    password = input("what is the password joe")
    if password == "fish":
        break
print("access granted")