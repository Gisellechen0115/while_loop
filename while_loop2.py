#WHIHE LOOP

while True :
    mode = input('請輸入名子:')   # input會把後面的東西存進去變數
    if mode == 'q':
        break
    elif mode != 'q':
        print(mode)
   
#印出abc各一次
i = 0
while i < 100:
    print('a')
    break
j = 0
while j < 100:
    print('b')
    break
print('c')       
 
#i印10次，J100次,C一次
i = 0
while i < 10:
    print('a')
    j = 0
    while j < 10:
        print('b')
        j = j + 1
    i = i + 1
print('c')   


  