#Este es un ejemplo de f-string en Python
name = 'Fernando'
age = 22
text = f'Mi nombre es {name} y tengo {age} años'
print(text)

a = 5
b = 3
print(f'El resultado de {a} y {b} es {a+b}')

price = 50
txt = f'El precio del producto es {a*b} { "CARO" if price > 50 else "BARATO" }'
print(txt)

