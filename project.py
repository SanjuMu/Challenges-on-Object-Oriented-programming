Num = int(input("Enter an integer: "))
class RomanNumber:
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
roman_numeral = ""
i = 0

while Num > 0:
    for _ in range(Num // RomanNumber.val[i]):
        roman_numeral += RomanNumber.syms[i]
        Num -= RomanNumber.val[i]
    i += 1

print("The Roman numeral is:",roman_numeral)