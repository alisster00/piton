# 2. Concatenar dos tuplas y contar cuántas veces aparece un número específico.

coord_1 = (100, 60, 300)
coord_2 = (200, 60, 400)

coord_3 = coord_1 + coord_2

print(coord_3)

cuenta = coord_3.count(60)

print(cuenta)
