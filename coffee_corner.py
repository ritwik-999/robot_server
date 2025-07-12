
#hello!....this is a simple programme that automates youe coffe ordering

print("hello,welcome to coffe corner")

name = input("whats your name::-")

#setting up a bouncer...!!!

if name == "ritwik":            #sorry to myself!
    e = input("are you evil or not::-(yes/no)\n")
    if e == "yes" :
        print("just leave this place , you are not welcomedhere !!")
        exit()
    else :
        print("oh! you are the good one, most welcome to our coffe corner..." + "\n\nok, " + name + " what you would like to order from our menu::-" )
else :
      print("\n\nok, " + name + " what you would like to order from our menu::-")


#setting the menus::-

coffee = 20
biscuit = 5
bread = 25
cake = 35


print("""\n\nmenu::-
      coffee.........rs.20/25
      biscuit........rs.05
      bread..........rs.25
      cake...........rs.35
            one order at a time plese
            thanks for ordering""")

order = input("\n\nyour order plese::-")
quantity = int(input("how many of that you would like::-"))
if order == "coffee":
    m= input("with milk or without milk..? (yes/no)::-\n")
    if m == "yes":
        price = coffee + 5 #adding extra 5 for milk
    else :
        price = coffee
elif order == "biscuit":
    price = biscuit
elif order == "bread":
    price = bread
elif order == "cake":
    price = cake
else:
    print("Invalid order!...or we may not have that item in our menu...!")
    exit()
total = quantity * price

print("\n\nhey, " + name + " your " + order + " of rs." + str(total)  +" will be ready shortly\n" + "\nthanks for visiting us.....")
# this is a simple programme that automates youe coffe ordering               
# it is a part of my python learning journey
# and is not intended for real-world use
