PI = 3.141592
raio = float(input().strip())
circunferencia = 2 * PI * raio 
a_circulo = PI * raio * 2 
a_esfera = 4 * PI * raio ** 2 
volume_esfera = 4 / 3 * PI * raio ** 3
print(f'{circunferencia:.6f}')
print(f'{a_circulo:.6f}')
print(f'{a_esfera:.6f}')
print(f'{volume_esfera:.6f}')
