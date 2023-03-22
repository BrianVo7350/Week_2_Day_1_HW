

num = 1
while True:
    cube = num ** 3
    if cube > 1000:
      break
    print(cube)
    num += 1



for i in range(2,101): 
    for j in range(2,101):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")



age = input("How old are you bro? ")

age = 18

if age < 18:
  print("Dang you just a kid")

elif age <= 65:
  print("Oh ok you an adult")

else:
  print("Dang you old senior")