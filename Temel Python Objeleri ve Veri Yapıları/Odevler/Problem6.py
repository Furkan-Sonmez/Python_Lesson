"""
Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2
"""

print("üçgenin hipotenüsünü bulan uygulama")

a=float(input ("Birci kenarı gürüniz:"))
b=float(input ("ikinci kenarı gürüniz:"))

print("hipotenüs: {}".format((a**2+b**2)**0.5))