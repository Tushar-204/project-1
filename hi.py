
# Num=0
# sum=0
# def name(Num,sum):
#  for i in range(0,2):
#   print(i)
# for a in range(0,13):
#   print(a)
# name(Num,sum)








# for a in range(0,14):
#   if(a<=1):
#     print(a)

# num=0
# sum=0
# while(sum<13):
#   num+=1
#   sum+=num
  
#   print(sum)





# x=int(input("Enter a number: "))
# for a in range(x):
#     w=""
#     for b in range(x):
#         w+= str(a)
#         w+= ","  
#         w+= str(b)
#         w+= "  "

#     print(w)



# x=int(input("Enter a number: "))
# for a in range(x):
#     w=""
#     for b in range(x):       
#         if  a==0 :
#             w+="*"
#         else:
#             w+="#"
#     print(w)















# def hello():
#     num = int(input("Enter a number: "))
#     a=0
#     b=1
#     c=0
#     for i in range(num):
#         c=b+a
#         print(a)
#         a=b
#         b=c
# hello()
        












# num =  int(input("Enter a number: "))
# i=0
# a=0
# b=1
# c=0
# def hello(a,b,c,i):
#     i+=1
#     c=a+b
#     print(a)
#     a=b
#     b=c
#     if(i==num):
#         return
#     hello(a,b,c,i)
# hello(a,b,c,i)
        





# num = int(input("Enter a number : "))
# i=0
# a=0
# multi=1
# def multipli(num,i,a,multi):
#     i+=1
#     a+=1
#     multi=multi*i
    
#     if (a==num):
#         print(multi)
#         return
#     multipli(num,i,a,multi)
# multipli(num,i,a,multi)





# num = int(input("Enter a number: "))
# b=0
# c=1
# for a in range(num):
#     b+=1
#     c=c*b
# print(c)


# input=int(input("Enter a number : "))
# for i in range(input):
#     a=""
#     for j in range (input):
#         a+=str(i)
#         a+=","
#         a+=str(j)
#         a+=" "
#     print(a)
    





# input=int(input("Enter a number : "))
# for i in range(input):
#     a=""
#     for j in range (input):
#         a+="* "
#     print(a)






# input=int(input("Enter a number : "))
# for i in range(input):
#     w=""
#     for j in range (input):
#         w+="*"
#     print(w)











input=int(input("Enter a number : "))
for row in range(input,0,-1):
    w=""
    for colom in range(row):
        w+=" "
    for colom in range(input-row+1):
        w+=str(colom)
    print(w)


