## Slicing
#El slicing es una técnica que nos permite obtener subcadenas de una cadena de texto en Python. Se utiliza la sintaxis [inicio:fin:paso], donde:
#inicio: es el índice donde comienza la subcadena (inclusive).
#fin: es el índice donde termina la subcadena (exclusive).
#paso: es el incremento entre los índices (opcional, por defecto es 1).

text = 'Fernando Martinez'
print(text[0:6:2])
print(text[9:])
print(text[::])
print(text[::-1])

text = 'Hola Mundo'
new_text = text[:5] + text[5:].replace('Mundo', 'Python')
print(new_text)

text = 'Python es genial'
parts =  text.split(' ')
partst2 = parts[:2]
parts_revers = parts[::-1]
print(parts)
print(partst2)
print(parts_revers)
text_revers = ' '.join(parts_revers)
print(text_revers)

text = 'Python'
print(text[:2].lower() + text[2:].upper())

text = '     Hola Python    '
print(text)
print(text.strip()[5:])
print(text.strip()[:5])
