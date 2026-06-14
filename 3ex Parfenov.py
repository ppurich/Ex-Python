import math

temp = 10 

def find_time(d1, d2, h, v_sand, n, theta1_deg):
      # Конвертация единиц измерения (мили в футы и т.д.)
    mile = 5280
    yard = 3
        # Конвертируем входные параметры
    d1 = float(d1 * yard / mile)
    d2= float(d2 / mile)
    h_= float(h * yard / mile)
    
    # Расчет для заданного угла
    radians = float(math.radians(theta1_deg))
    tangent = float(math.tan(radians))
    x = float(d1 * tangent)
    L1 = float(math.sqrt(pow(x, 2) + pow(d1, 2)))
    L2 = float(math.sqrt(pow((h - x), 2) + pow(d2, 2)))
    v_swim = v_sand / n
    t = round((1/v_sand * (L1 + n * L2)) * 3600, 1)
    return t

def idx1():
    print(f'idx() из модуля Life_guard_final видит значение time1 как {time1}')

time1 = 5.5

# Первая часть тестов (для find_time)
if __name__ == '__main__':
    total_tests = 0 
    passed_tests = 0
    input_data = [[8, 10, 50, 5, 2, 39.413], [40, 100, 42, 12, 2, 30]] 
    expected_time = [39.9, 20.9] 
    
    for idx in range(len(input_data)):
        actual_time = find_time(input_data[idx][0], input_data[idx][1], 
                               input_data[idx][2], input_data[idx][3], 
                               input_data[idx][4], input_data[idx][5])
        total_tests += 1
        print(f'actual: {actual_time}, expected: {expected_time[idx]}')
        if abs(actual_time - expected_time[idx]) <= 0.1:
            passed_tests += 1
    
    print(f'всего тестов {total_tests} из них успешно {passed_tests}')
    print(f'вычисленное время {time1}')
    print(f'вычисленное время после модификации {time1}') 
    print(f'индекс равен {idx1()}')  # ВАЖНО: добавлены скобки

def find_opt_time(d1, d2, h, v_sand, n):
  
    times = []
    angles = [] 
    
    theta1_deg = 0.0  # начальный угол
    
    # Цикл от 0 до 90 градусов с шагом 0.1
    while theta1_deg <= 90.0:
        time1 = find_time(d1, d2, h, v_sand, n, theta1_deg)
        times.append(time1)
        angles.append(theta1_deg)
        
        
        if len(times) % 100 == 0:  # Выводим каждые 100 итераций
            print(f'Угол {theta1_deg:.1f}°, время: {time1}')
        
        theta1_deg += 0.1  # увеличиваем угол
    
    # Находим минимальное время и соответствующий угол
    min_time = min(times)
    min_index = times.index(min_time)
    opt_angle = angles[min_index]
    
    print(f'\nОптимальный угол: {opt_angle:.1f}°')
    print(f'Минимальное время: {min_time:.1f} секунд')
    
    return min_time

# Вторая часть тестов (для find_opt_time)
if __name__ == '__main__':
    total_tests = 0 
    passed_tests = 0
    input_data = [[8, 10, 50, 5, 2], [40, 100, 42, 12, 2]] 
    expected_time = [39.9, 20.9] 
    
    for idx in range(len(input_data)):
        actual_time = find_opt_time(input_data[idx][0], input_data[idx][1], 
                                   input_data[idx][2], input_data[idx][3], 
                                   input_data[idx][4])
        total_tests += 1
        print(f'actual: {actual_time}, expected: {expected_time[idx]}')
        if abs(actual_time - expected_time[idx]) <= 0.1:
            passed_tests += 1
    
    print(f'всего тестов {total_tests} из них успешно {passed_tests}')