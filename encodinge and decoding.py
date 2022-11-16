def encoding(a):
    reshte = ""
    list1 = []
    for i in range (4):
        if i == 0 :
            list1.append(a[2])
        elif i == 1 :
            list1.append(a[3])
        elif i == 2 :
            list1.append(a[0])
        else :
            list1.append(a[1])
    for item in list1 :
        ijadid = (int(item) + 7) % 10
        reshte += str(ijadid)
    return reshte
    

def decoding (b): 
    dic1 = {'8':'1','9':'2','0':'3','1':'4','2':'5','3':'6','4':'7','5':'8','6':'9','7':'0'}
    list1 =[]
    index = 0
    for i in range(4):
        if i == 0 :
            list1.append(b[2])
        elif i == 1 :
            list1.append(b[3])
        elif i == 2 :
            list1.append(b[0])
        else :
            list1.append(b[1])                 
    for item in list1 :
        list1[index]= dic1[item]
        print(list1[index],end ='')
        index += 1


number = str(input())
number2 = encoding(number)
print(number2)
decoding(number2)




