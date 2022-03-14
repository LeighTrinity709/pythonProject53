#LeighTrinity
#March 13 2022

import random
import termcolor



letters = ['a', 'b','c','d','e','f', 'g','h','i','j','k','l', 'm','n','o','p','q','r','s','t','u',
           'v','w','x', 'y','z', 'A' 'B', 'C', 'D,','E','F','G','H', 'I', 'J','K','L','M','N','O', 'P', 'Q','R','S','T','U','V',
           'W', 'X', 'Y','Z',]

numbers = [ '0','1','2','3','4','5','6','7','8','9',]

symbols = ['!','@',"#",'$','%','^','*','&','(',')',]

print(termcolor.colored('''

8b       dbd8,ad  PPYYba1,  8 b,dPPYba,    49      ++  
"b       d8         d8    ' "              Y8      8#      
8b       d8'`8bd    8'    ,ad      tPPPPy  P89rde7888          
8b       `8         88,    ,8        5x    8y      yf
YP`"8bb  dP"Y888  pdp"pba    p   R$#s^+    8g      ws
''', 'green'))
print(termcolor.colored('''                                             
                   88              YT                               
  ,d               ""              88      88      W        uW
  88                                       88       N      xY
MM88MMM 8b,dPPYba, 88  8b,dPPYba,  ,a  dPPYba,88,    P    "5
  88    88P'   "Y8 88  88P'   "Y8  dP      ""         T  "8  
  88    88         88  88      W2  YT      8b          88    
  88,   88         88  88,    ,88  88      `"          "8   
  "Y888 88         88  88      `"  NB      `"Ybbd      8"   
''', "magenta"))

print(termcolor.colored( 'Welcome to the Python password generator', 'red'))

x_letters= int(input("How many letters for the password?") )
x_numbers = int(input("How many numbers do you want?"))
x_symbols= int(input("Enter # of symbols"))

password_list = []
for char in range (1, x_letters +1):
    password_list.append(random.choice(letters))


for char in range (1,x_numbers +1):
    random_num =random.choice(numbers)
    password_list.append(random.choice(numbers))



for char in range (1, x_symbols +1):
    random_sym =random.choice(symbols)
    password_list.append(random.choice(symbols))

print(password_list)

random.shuffle(password_list)

print(password_list)