#密碼重試程式:
#先設定好密碼 password = 'a123456'
#讓使用者最多輸入3次
#不對的話印出'密碼錯誤,還有幾次機會'

##1
x=3
while x >0 :
    password = input('請輸入密碼:')   # input會把後面的東西存進去變數
    if password == 'a123456': 
        print('登入成功')
        break
    elif password != 'a123456' and x >1:
        print('密碼錯誤,還有',x-1,'次機會')
        x = x-1
    else :
        print('密碼輸入錯誤三次')
        break 
    
##2   
password = "a123456"
i = 3 #剩餘機會
while True:
 pwb = input('請輸入密碼')
 if pwb == password:
  print('登入成功')
  break #逃出迴圈
 else :
  i = i - 1 
  print('密碼錯誤! 還有' , i, '次機會')
  if i == 0:
   break    


##3     
password = "a123456"
i = 3 #剩餘機會
while i > 0:
    pwb = input('請輸入密碼')
    if pwb == password:
        print('登入成功')
        break
    else:
        i = i - 1 
        print('密碼錯誤! 還有' , i, '次機會')
        
          

##4
password = "a123456"
i = 3 #剩餘機會
while i > 0:
    i = i -1
    pwb = input('請輸入密碼')
    if pwb == password:
        print('登入成功')
        break
    else:
        if i > 0:
            print('密碼錯誤! 還有' , i, '次機會') 
        else:
            print('密碼輸入錯誤三次')
            break
        
    



    