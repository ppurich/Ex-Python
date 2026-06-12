import math
d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды):"))
d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы): "))
h = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды): "))
v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час):  "))
n = float(input("Введите коэффициент замедления спасателя при движении в воде,: "))
theta1 = float(input("Введите направление движения спасателя по песку,: "))

mile=5280
yard=3
d1=float(d1*yard/mile)
#print (f"проверка d1 {d1}")
d2=float(d2/mile)
#print (f"проверка d2 {d2}")
h= float(h*yard/mile)
#print (f"проверка h {h}")
degress = theta1
def rad_test():
    radians = float(math.radians(degress))
    return radians 
radians = rad_test()
for rad in range(1,5):
    if radians != 0.687886618088525:
        resoultok = False
        print(f"№ теста {rad}: resoultok = {resoultok}")
    else:
        resoultok = True
        print(f"№ теста {rad}: resoultok = {resoultok}")
    break
#print (f"проверка radians {radians}")
#tangent = round((math.tan(radians)),1)
print(f"{radians}")
def tan_test():
    tangent = float(math.tan(radians))
    return tangent
tangent = tan_test()
print(f"{tangent}")
for tan in range(2,5):
    if radians != 0.8217893117448576:
        resoultok = False
        print(f"№ теста {tan}: resoultok = {resoultok}")
    else:
        resoultok = True
        print(f"№ теста {tan}: resoultok = {resoultok}")
    break

#print (f"проверка tangent {tangent}")
x = float(d1*tangent)
#print (f"проверка x {x}")
def L1_test():
    L1 = float(math.sqrt(pow(x,2)+pow(d1,2)))
    return L1

L1 = L1_test()
for geom1 in range(3,5):
    if L1 != 0.005883401629100235:
        resoultok = False
        print(f"№ теста {geom1}: resoultok = {resoultok}")
    else:
        resoultok = True
        print(f"№ теста {geom1}: resoultok = {resoultok}")
    break

#print (f"проверка l1 {L1}")
def L2_test():
    L2 = float(math.sqrt(pow((h-x),2)+pow(d2,2)))
    return L2
L2= L2_test()
for geom2 in range(4,5):
    if L2 != 0.02474626709774013:
        resoultok = False
        print(f"№ теста {geom2}: resoultok = {resoultok}")
    else:
        resoultok = True
        print(f"№ теста {geom2}: resoultok = {resoultok}")
    break
#print (f"проверка l2 {L2}")

v_swim = v_sand/n
#t = round((1/v_sand * (L1+n*L2))*3600,1)
# функция для вычисления времени
def time_test():
    t = round((1/v_sand * (L1+n*L2))*3600,1)
    return t
t=time_test()

print (f"проверка времени t {t}")
# цикл для тестирования 
for i in range(5,6):
    if t != 39.9:
        resoultok = False
        print(f"№ теста {i}: resoultok = {resoultok}")
    else:
        resoultok = True
        print(f"№ теста {i}: resoultok = {resoultok}")
    break
# def time()
#     result = t
#     t = round((1/v_sand * (L1+n*L2))*3600,1)
#     return t
# print (f"проверка времени t {t}")
# for t in range(5):
#     t1 = round((1/v_sand * (L1+n*L2))*3600,1)
#     if t != 39.9:
#         resoultok = False
#         t1 = round((1/v_sand * (L1+n*L2))*3600,1)
#         t2 = round((1/v_sand * (L1+n*L2))*3600,1)
#         t3 = round((1/v_sand * (L1+n*L2))*3600,1)
#         t4 = round((1/v_sand * (L1+n*L2))*3600,1)
#         print(f"test1 {t1}")
#         print(f"test2 {t2}")
#         print(f"test3 {t3}")
#         print(f"test4 {t4}")
#     else:
#     resoultok = True
#print(f"time")

print(f"угол перемещения {round(tangent,1)}")
print(f"время на спасение {t}")