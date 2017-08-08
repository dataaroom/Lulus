#! python3
"""
Create a data structure for all units.
build a class "Units" to convert unit as required.
"""


class Units:

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
    v = {'m/s': [1.0, 1, 'meter per second'],
     'km/hr': [3.6, 1],
     'ft/s': [3.280839895, 2],
     'mph': [2.236936292, 2, 'miles per hour'],
     'in/s': [39.37007874, 2],
     'knot': [1.943844493, 2]
     }
# power
    P = {'kw': [1.0, 1, 'kilowatt'],
     'w': [1000, 1],
     'hp': [1.34102, 2, 'horsepower']
     }

# density
    density = {'kg/m3': [1.0, 1],
           'g/mm3': [1e-6, 1],
           'water(4°C)': [0.001, 1],
          'lbs/gallon':[0.008345404, 2]
           }

# time
    t = {'s': [1.0, 1, 'seconds'],
     'min.': [0.01666667, 1, 'minutes'],
     'hr.': [0.000277778, 1, 'hours'],
     'd': [4.62963e-6, 1, 'days']
     }

# temperature
    T = {'°C': [1.0, 1, 'degree centigrade'],
     '°F': [1.6, 2, 'degree Fahrenheit'],
     'K': [1.0, 1, 'kelvin degree']
     }


    def convert(self, type, inputUnit, output, value):
      in_factor = 1.0
      out_factor = 1.0
      if type == 'L':
        for i, j in Units.L.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'A':
        for i, j in Units.A.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'W':
        for i, j in Units.W.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'M':
        for i, j in Units.M.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'Q':
        for i, j in Units.Q.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'v':
        for i, j in Units.v.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'p':
        for i, j in Units.p.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'P':
        for i, j in Units.P.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'T':

          result = Units.convert_t(inputUnit,output, value)
          return result
      elif type == 'density':
        for i, j in Units.density.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      elif type == 'V':
        for i, j in Units.V.items():
            if inputUnit == i:
                in_factor = j[0]
            if output == i:
                out_factor = j[0]
        result = value * out_factor / in_factor
        return result
      else:
        return None


    def convert_t(inputUnit, outputUnit, value):

        output = value
        if inputUnit == '°F' and outputUnit == '°C':
            output = (value - 32) * (5 / 9)
            return output
        elif inputUnit == '°C' and outputUnit == '°F':
            output = (value * 1.8) + 32
            return output
        elif inputUnit == '°C' and outputUnit == 'K':
            output = value + 273.15
            return (output)
        elif inputUnit == 'K' and outputUnit == '°C':
            output = value - 273.15
            return output
        elif inputUnit == '°F' and outputUnit == 'K':
            output = (value + 459.67) * (5 / 9)
            return output
        elif inputUnit == 'K' and outputUnit == '°F':
            output = (value * 1.8) - 459.67
            return output
        else:
            return output



