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
radians = float(math.radians(degress))
#print (f"проверка radians {radians}")
#tangent = round((math.tan(radians)),1)
tangent = float(math.tan(radians))
#print (f"проверка tangent {tangent}")
x = float(d1*tangent)
#print (f"проверка x {x}")
L1 = float(math.sqrt(pow(x,2)+pow(d1,2)))
#print (f"проверка l1 {L1}")
L2 = float(math.sqrt(pow((h-x),2)+pow(d2,2)))
#print (f"проверка l2 {L2}")

v_swim = v_sand/n
#t = round((1/v_sand * (L1+n*L2))*3600,1)
t = round((1/v_sand * (L1+n*L2))*3600,1)
#print (f"проверка времени t {t}")

if t != 39.9:
   resoultok = False
   t1 = round((1/v_sand * (L1+n*L2))*3600,1)
   t2 = round((1/v_sand * (L1+n*L2))*3600,1)
   t3 = round((1/v_sand * (L1+n*L2))*3600,1)
   t4 = round((1/v_sand * (L1+n*L2))*3600,1)
   print(f"test1 {t1}")
   print(f"test2 {t2}")
   print(f"test3 {t3}")
   print(f"test4 {t4}")
else:
   resoultok = True
   
#print(f"time")
print(f"{resoultok}")
print(f"угол перемещения {round(tangent,1)}")
print(f"время на спасение {t}")