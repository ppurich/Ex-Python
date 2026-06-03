import math
d1 = float(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды): "))
d2 = float(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы): "))
h = float(input("Введите боковое смещение между спасателем и утопающим, h (ярды): "))
v_sand = float(input("Введите скорость движения спасателя по песку, v_sand (мили в час): "))
n = float(input("Введите коэффициент замедления спасателя при движении в воде,: "))
theta1 = float(input("Введите направление движения спасателя по песку,: "))

mile=5280
yard=3
d1=d1*yard/mile
d2=d2/mile
h= h*yard/mile
degress = theta1
radians = math.radians(degress)
tangent = round((math.tan(radians)),1)
x = d1*tangent
L1 = math.sqrt(pow(x,2)*pow(d1,2))
L2 = math.sqrt(pow((h-x),2)+pow(d2,2))
v_swim = v_sand/n
t = round((1/v_sand * (L1+n*L2))*3600,1)


print(f"угол перемещения {tangent}")
print(f"время на спасение {t}")