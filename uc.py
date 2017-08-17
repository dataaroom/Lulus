#! python3
"""
Create a data structure for all units.
build a class "Units" to convert unit as required.
"""


class Units:
    
    
    def __init__(self, value, unit, type):
        self.value = value
        self.unit = unit
        self.type = type

# 两个相同单位相加，返回值的单位和第一个相同。  比如:  2 in + 2.54 cm = 3 in
    def __add__(self, other):
        sum = self.value + Units.convert(other, self.unit)
        result = Units(sum, self.unit, self.type)
        return result

# 两个单位相减，返回值的单位和第一个相同。  比如:  22 in - 2.54 cm = 21 in
    def __sub__(self, other):
        sub = self.value - Units.convert(other, self.unit)
        result = Units(sub, self.unit, self.type)
        return result

# 两个单位相乘， 生成新的单位。遍历dir(Units), 如果找到新的单位，将其归入已有类别，如果没有找到， 建立一个临时type "intern" TODO: 何时删除？ 待定。。。
    def __mul__(self, other):
        mul = self.value * Units.convert(other, self.unit)
        unit = self.unit + '*' + other.unit
        type = 'intern'
        for i in dir(self):
            for a, b in getattr(self,i).items():
                if unit == a:
                    type = i
                    break
        result = Units(mul, unit, type)

# 两个单位相除， 生成新的单位。遍历dir(Units), 如果找到新的单位，将其归入已有类别，如果没有找到， 建立一个临时type "intern" TODO: 何时删除？ 待定。。。
    def __truediv__(self, other):
        mul = self.value / Units.convert(other, self.unit)
        unit = self.unit + '/' + other.unit
        type = 'intern'
        for i in dir(self):
            for a, b in getattr(self,i).items():
                if unit == a:
                    type = i
                    break
        result = Units(mul, unit, type)
        return result

#单位主列表, 在单位转换时使用。
    def __dir__(self):
        return ['L', 'M', 'A','V','P','W','Q','v','p','density','t','T','mol']


# length
    L = {'m': [1.0, 1],
     'km': [1e-3, 1],
     'cm': [100, 1],
     'mm': [1e3, 1],
     'ft': [3.2808399, 2],
     'in': [39.3700788, 2],
     'yard': [1.093613298, 2]
     }

# mass
    M = {'kg': [1.0, 1],
     'g': [1e3, 1],
     'pound': [2.20462262, 2],
     'ounce': [35.27396192, 2],
     'ton-SI': [0.001, 1],
     'ton-US': [0.001102311, 2],
     'ton-UK': [0.000984207, 3]
     }

# area
    A = {'m2': [1.0, 1],
     'km2': [1e-6, 1],
     'cm2': [1e4, 1],
     'mm2': [1e6, 1],
     'ft2': [10.76391045, 2],
     'in2': [1550.003105, 2],
     'acre': [0.000247105, 2],
     'are': [0.01, 1]
     }

# volume
    V = {'m3': [1.0, 1],
     'km3': [1e-9, 1],
     'liter': [1e3, 1],
     'cm3': [1e6, 1],
     'mm3': [1e9, 1],
     'ft3': [35.31466672,2],
     'in3':[61023.74437,2],
     'bbl': [0.158987295, 2],
     'gallon-US liquid': [264.172524, 2],
     'gallon-US dry': [227.0207446, 2],
     'quart-US liquid': [1056.688209, 2],
     'quart-US dry': [908.0829783,2]
     }

# pressure
    p = {'Pa': [1.0, 1],
     'kPa': [1e-3, 1],
     'MPa': [1e-6, 1],
     'psi': [1.45037738e-4, 2],
     'bar': [1e-5, 1],
     'mmHg(°C)': [7.500615613e-3, 1],
     'mmH2O(4°C)': [1.019716213e-1, 1]
     }

# mass_flow_rate
    W = {'kg/s': [1.0, 1],
     'kg/m': [60, 1],
     'kg/hr': [3600, 1],
     'lbs/s': [2.20462262, 1],
     'lbs/hr': [7936.641432, 2],
     'ton/day': [216, 1]
     }

# volume flow rate
    Q = {'m3/s': [1.0, 1],
     'm3/min': [60, 1],
     'm3/hr': [3600, 1],
     'liter/s': [1000, 1],
     'gpm': [15850.32314,2,'gallon per minutes']
     }

     # velocity
    v = {'m/s': [1.0, 1, 'Meter per Second'],
     'km/hr': [3.6, 1],
     'ft/s': [3.280839895, 2],
     'mph': [2.236936292, 2, 'Miles per Hour'],
     'in/s': [39.37007874, 2],
     'knot': [1.943844493, 2]
     }
# power
    P = {'kw': [1.0, 1, 'Kilowatt'],
     'w': [1000, 1],
     'hp': [1.34102, 2, 'Horsepower']
     }

# density
    density = {'kg/m3': [1.0, 1],
           'g/mm3': [1e-6, 1],
           'water(4°C)': [0.001, 1],
          'lbs/gallon':[0.008345404, 2]
           }

# time
    t = {'s': [1.0, 1, 'Seconds'],
     'min.': [0.01666667, 1, 'Minutes'],
     'hr.': [0.000277778, 1, 'Hours'],
     'd': [4.62963e-6, 1, 'Days']
     }

# temperature
    T = {'°C': [1.0, 1, 'degree Centigrade'],
     '°F': [1.6, 2, 'degree Fahrenheit'],
     'K': [1.0, 1, 'Kelvin degree']
     }
# Amount of substance
    mol = {'mol': [1.0, 1, 'Mole'],
           'kmol': [0.001, 1, 'KiloMole']
          }
   
# electric current
    A = {'A': [1.0, 1, 'ampere'],
         'mA': [1000.0, 1, 'microampere'],
         'kA': [0.001,1, 'kiloampere']
        }
    
# luminous intensity
    I = {'cd': [1.0, 1, 'candela']
        }

# 单位换算主函数，根据输入的单位，数值　计算要求单位下的值。返回值是浮点数。
    def convert(known, outUnit):
        if known.type == 'T':
            return Units.convert_t(known, outUnit)
        else:
            in_factor = 1.0
            out_factor = 1.0
            catg = getattr(known, known.type).items()
            for i,j in catg:  #  调取用户所选的单位参数表，搜索输入和输出，并进行计算。返回计算结果。
                if known.unit == i:
                    in_factor = j[0]
                if outUnit == i:
                    out_factor = j[0]
            result = known.value * out_factor / in_factor
            return result

# 温度转换公式。 温度单位不成线性比例，公式计算不同，单独设置函数计算。TODO: 以后有时间思考是否可以合并成一个函数。
    def convert_t(known, outputUnit):
        if known.unit == '°F' and outputUnit == '°C':
            output = (known.value - 32) * (5 / 9)
            return output
        elif known.unit == '°C' and outputUnit == '°F':
            output = (known.value * 1.8) + 32
            return output
        elif known.unit == '°C' and outputUnit == 'K':
            output = known.value + 273.15
            return (output)
        elif known.unit == 'K' and outputUnit == '°C':
            output = known.value - 273.15
            return output
        elif known.unit == '°F' and outputUnit == 'K':
            output = (known.value + 459.67) * (5 / 9)
            return output
        elif known.unit == 'K' and outputUnit == '°F':
            output = (known.value * 1.8) - 459.67
            return output
        else:
            return known.value

# 将输入转换成标准单位 - SI unit.
    def standard_unit(known):  # input is a instance of the Unit class.
        for i, j in getattr(known,known.type).items():
            if j[0] == 1.0:
                SIunit = i
            if known.unit == i:
                in_factor = j[0]

        value = known.value / in_factor
        output = Units(value, SIunit, known.type)
        return output


unit= Units(2,'m', 'L')
unit1 = Units(2.54,'in', 'L')
unit3 = Units(22, 'cm', 'L')
print(unit.type)
print(unit.unit)
print(len(dir(unit)))
print(list(getattr(unit, unit.type).items()))
unit2 = unit1 - unit + unit3
print(unit2.value, unit2.unit, unit2.type)

