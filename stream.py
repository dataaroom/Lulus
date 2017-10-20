#! python3
"""
Create a data structure for streams.

"""
from uc import Units


class Streams:   

"""
Define a data structure for flow streams. define all pareteters with a proper unit. 
"""

  def __init__(self, stream, 
               Description = "Please add a description, like 'Feed Gas to HP Chiller'." 
               Phase = 'Vapor', 
               Fraction_V = 1.0, 
               Mole_Flow = Units(), 
               Mass_Flow = Units(), 
               Temperature = Units(), 
               Pressure = Units(), 
               Mass_Density = Units(), 
               MW = 0.0, 
               Enthalpy = Units(), 
               Heat_Flow = Units(), 
               Critial_Temperature = Units(), 
               Critical_Pressure = Units(), 
               Mass_Flow_L = Units(), 
               Mole_Flow_L = Units(),
               A_Liquid_Flow = Units(), 
               Specific_Gravity = 0.0, 
               MW_L = 0.0
               Density_L = Units(), 
               Enthalpy_L = Units(), 
               Mass_Heat_Capacity_L = Units(),
               Surface_Tension = Units(),
               Thermal_Conductivity_L = Units(),
               Viscosity_L = Units(),
               Mass_Flow_V = Units(),
               Mole_Flow_V = Units(),
               Std_Vapor_Flow = Units(),
               MW_V = 0.0
               Density_V = Units(),
               Enthalpy_V = Units(),
               Mass_Heat_Capacity_V = Units(),
               Thermal_Conductivity_V = Units(),
               Viscosity_V = Units(),
               cp_cv = 1.0               
              ):
      self.stream = stream
      self.Description = Description
      self.Phase = Phase
      self.Fraction_V = Fraction_V
      self.Mole_Flow = Mole_Flow
      self.Mass_Flow = Mass_Flow
      self.Temperature = Temperature
      self.Pressure = Pressure
      self.Mass_Density = Mass_Density
      self.MW = MW
      self.Enthalpy = Enthalpy
      self.Heat_Flow = Heat_Flow
      self.Critial_Temperature = Critial_Temperature
      self.Critical_Pressure = Critical_Pressure
      self.Mass_Flow_L = Mass_Flow_L
      self.Mole_Flow_L = Mole_Flow_L
      self.A_Liquid_Flow = A_Liquid_Flow
      self.Specific_Gravity = Specific_Gravity
      self.MW_L = MW_L
      self.Density_L = Density_L
      self.Enthalpy_L = Enthalpy_L
      self.Mass_Heat_Capacity_L = Mass_Heat_Capacity_L
      self.Surface_Tension = Surface_Tension
      self.Thermal_Conductivity_L = Thermal_Conductivity_L
      self.Viscosity_L = Viscosity_L
      self.Mass_Flow_V = Mass_Flow_V
      self.Mole_Flow_V = Mole_Flow_V
      self.Std_Vapor_Flow = Std_Vapor_Flow
      self.MW_V = MW_V
      self.Density_V = Density_V
      self.Enthalpy_V = Enthalpy_V
      self.Mass_Heat_Capacity_V = Mass_Heat_Capacity_V
      self.Thermal_Conductivity_V = Thermal_Conductivity_V
      self.Viscosity_V = Viscosity_V
      self.cp_cv = cp_cv
      
      
      
    
    
