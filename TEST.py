from uc import Units


calc = Units()
name = input('What is your name?')
print(dir(calc))

while True:
    print(name, ', What kind of unit you want to convert?')
    type = input('see the list above:')
    print (list(getattr(calc,type).keys()))
    unit1 = input('the original unit:')
    unit2 = input('the unit you want to convert:')
    value = float(input('put a number:'))
    print('%s %s = %s %s' %(value, unit1, calc.convert(type, unit1, unit2, value), unit2))
    again = input('Convert another unit? Y/N?')
    if again.upper() == 'N':
        break

