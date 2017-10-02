#! python3
"""
Create a data structure for streams.

"""
from uc import Units


class streams:   

"""
Define a data structure for flow streams. define all pareteters with a proper unit. 
"""
  def __init__(self,  name, Phase = None, V_Fraction = None, Mole_Flow = None, Mass_Flow = None, 
               Mass_Flow = None, Temp = None, Pressure = None, Mass_Density = None, MW = None, 
              Enthalpy = None, Heat Flow = None, Critial Temperature = None, Critical Pressure = None):
    if Phase == None:
      Phase = 'Vapor'
    if V_Fraction = None:
      V_Fraction = 1.0
    if Mole_Flow = None:
      Mole_Flow = 
    
