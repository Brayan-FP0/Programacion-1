#operadores logicos
#AND
num1 = 5
num2 = 10
print(num1 < 10 and num2 > 5)# 1 1 = 1
print(num1 < 10 and num2 < 5)#
print(num1 > 10 and num2 > 5)#
print(num1 > 10 and num2 < 5)#

#inicio de secion 
usuario = "brayanzzz" 
contraseña = "123456"
#solicitar nombre de usuario y contraseña
input_usuario = input("ingrése su nombre de usuario")
input_contraseña = input("ingrése su contraseña")
print(input_usuario == usuario and input_contraseña == contraseña)