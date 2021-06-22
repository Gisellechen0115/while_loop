#WHIHE LOOP

x = 5
while x < 10 :
    print( x )
    x = x + 1
while True :
   print('NO EN')
   break
print('MY GOD') 
    
#True就會一直成立
while True :
    mode = input('請輸入遊戲模式:')   # input會把後面的東西存進去變數
    if mode == 'q': #quit
        break
    elif mode == '1':
        print('啟動模式一')
    elif mode == '2':
        print('啟動模式二')
    else:
        print('只能輸入1/2/q')
    