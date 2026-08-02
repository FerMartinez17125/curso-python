#Este código convierte un texto a Mayúsculas y minúsculas

text1 = 'Hola Fernando'
text1_upper = text1.upper()
text1_lower = text1.lower()
print("Texto original: ", text1)
print("Texto en mayúsculas: ", text1_upper)
print("Texto en minúsculas: ", text1_lower)

#Uso de find e index
print()
text = 'Hola Fernando, como estas?'
print(text.find('Fernando'))
print(text.index('Fernando'))
#La diferencia entre find e index es que find devuelve -1 si no encuentra el texto, mientras que index lanza un error.
print()
#Startwith y endswith
print(text.startswith('Hola'))
print(text.endswith('estas?'))

print()
number = '1234'
decimal = '1234.56'
mix = 'Python3'

print(number.isnumeric())
print(decimal.isdigit())
print(mix.isalnum())