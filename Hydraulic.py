
#! python3
"""
Create a data structure for all units.build a class "Units" to convert unit as required.

"""


import Units from uc

class Dimensionless:

    def Reynolds(density, v, d, vi)  # TODO: add vi(viscosity) to Units class
        re = (density.SI_value * v.SI_value * d.SI_value) / vi.SI_value
        return re
    
    
  
