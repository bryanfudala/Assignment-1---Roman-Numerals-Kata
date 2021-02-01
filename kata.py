#BRYAN FUDALA CIDM 6330 ASSIGNMENT 1
#CONVERT INTEGER TO ROMAN NUMERAL
def integer_into_roman(x):
    integer_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_list = [
        'I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M'
    ]
    i = 12
    roman_numeral = ""
    while x > 0:
        if integer_list[i] <= x:
            roman_numeral += roman_list[i]
            x = x - integer_list[i]
        else:
            i -= 1
    return roman_numeral


entry_number = int(
    input("Please enter in an integer to convert to roman numeral: "))
print(integer_into_roman(entry_number))
