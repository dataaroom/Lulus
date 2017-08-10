from uc import Units


type = input('type:')
unit1 = input('the original unit:')
unit2 = input('the unit you want:')
value = float(input('put a number:'))
calc = Units()
print (list(getattr(calc,type).keys()))
print(dir(calc))
print(calc.convert(type, unit1, unit2, value))