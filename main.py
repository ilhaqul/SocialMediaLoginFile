userlist = []

f = open("userlist.txt", "r")
for i in f.readlines():
	userlist.append(i[:-1])
f.close()

def home():
  global username
  print("1. Login")
  print("2. Registration")
  a = input("here : ")
  if a == "1":
    found = False
    username = input("Input Username : ")
    password = input("Input Password : ")
    for i in userlist:
      if i==username:
        found = True
        f = open(i+".txt","r")
        if f.readlines()[1][:-1]==password:
          see()
        else:
          input("Password does not match")
        break
    if not found:
      print("invalid Username")
  elif a == "2":
    username = input("Input username : ")
    while username in userlist:
      print("Name has been taken,use another username")
      username = input("Input username : ")
    password = input("Input password : ")
    name = input("Input name : ")
    birthday = input("Input birthday : ")
    list1 = [username,password,name,birthday]
    userlist.append(username)
    f = open("userlist.txt", "a")
    f.writelines(username+"\n")
    f.close()
    f = open(username+".txt","w")
    for i in list1:
      f.writelines(i+"\n")
    f.close()
  else:
    print("Just input 1 or 2")

def see():
  global username
  f = open(username+".txt", "r")
  temp = f.readlines()
  f.close()
  print("Nama : ",temp[2]+"Birthday : ", temp[3])
  input("Press enter for logout")

while True:
  home()

  