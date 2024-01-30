temp =input(" Enter temperature :")
if not temp.isdigit():
        print("Nan")
else:
        temp = int(temp)        
        if temp >=35:
            print("It's a hot day !!")
        elif temp >= 14 and temp < 35 :
               print("It's a cool day ") 
        else:
               print("it's Cold day")          
