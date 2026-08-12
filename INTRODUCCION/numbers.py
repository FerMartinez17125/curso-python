# En python existen diferentes tipos de datos, entre ellos los números. Los números pueden ser enteros, flotantes o complejos.
#No existe como tal un tipo de dato para los números, ya que python es un lenguaje de tipado dinámico, lo que significa que no es necesario declarar el tipo de dato de una variable, ya que python lo infiere automáticamente.
#Tampoco hay límite en el tamaño de los números enteros, ya que python los maneja automáticamente como enteros largos si es necesario. Asi se evita el desbordamiento también conocido como overflow, que es cuando un número es demasiado grande para ser representado en la memoria de la computadora y se produce un error.

age = 22
big_int = 1234567890123456789012345678901234567890 
decimal = 3.1415

print(age)
print(type(age))

print(big_int)
print(type(big_int)) #type se usa para poder ver el tipo de dato que es la variable
print(decimal)
print(type(decimal))
