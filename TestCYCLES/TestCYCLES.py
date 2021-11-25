# 1
#n = 0
#while type(n)!=int or (n>9 or n<1):
#    try:
#        n = int(input("Введите колличество животных вы хотите увидеть? 1-9 "))
#    except: ValueError
#for i in range(1):
#    for a in range(n): print(" ^---^ ",end=" ")
#    print()
#    for s in range(n): print("( o o )",end=" ")
#    print()
#    for d in range(n): print(" ! = ! ",end=" ")
#    print()
# 2
#p=0
#n=0
#i=1
#while type(p)!=float or p<=0:
#    try:
#        p = float(input("Write degree: "))
#    except: ValueError
#while type(n)!=float or n<=0:
#    try:
#        n = float(input("Предел: "))
#    except: ValueError
#while i**p <= n:
#    print(i,end=", ")
#    i+=1
#print("в степени ",p," меньше предела")
# 3
#from random import*
#s = randint(1,30)
#m = 0
#max = 0
#min = 6
#for i in range(s):
#    m = randint(1,5)
#    if m>max:
#        max = m
#    elif m<min:
#        min = m
#print("Минимальная оценка ",min,", а максимальная ",max)
# 4
#ameba = 1
#l=0
#for i in range(8):
#    ameba*=2
#    l+=1
#    print("Через",l,"ч будет",ameba,"клетки")
# 5
#K=0
#M=0
#score=0
#while type(K)!=int or K<1:
#    try:
#        K=int(input("Сколько у тебя котлет? "))
#    except: ValueError
#while type(M)!=int or M<1:
#    try:
#        M=int(input("Сколько на одну сковородку помещается котлет? "))
#    except: ValueError
#while K>=M:
#    K-=M
#    score+=1
#print(score,"полные сковородки надо пожарить и",K,"котлет останется")