

"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

"""

print("*** Sayı çarpım uygulaması ***")

a = int(input ("İlk sayıyı giriniz lütfen :"))
b = int(input ("İkinci sayıyı giriniz lütfen :"))
c = int(input ("üçüncü sayıyı giriniz lütfen :"))

print("{} x {} x {} = {}".format(a,b,c,a*b*c))
