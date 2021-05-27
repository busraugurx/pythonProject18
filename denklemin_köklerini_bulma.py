print("2. dereceden 1 bilinmeyenli denklemin köklerini hesaplama")

"denklem= a*x^2 + bx + c"
"delta= b*b-4*a*c"

a=int(input("a değerini giriniz:"))
b=int(input("b değerini giriniz:"))
c=int(input("c değerini giriniz:"))

delta= b * b - 4 * a * c

x1= (-b - delta ** 0.5) / (2 * a)
x2= (-b + delta ** 0.5) / (2 * a)

print("1. kök: {}, ikinci kök: {}" .format(x1,x2))

