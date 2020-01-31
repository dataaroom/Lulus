#! python3.7
"""
Relief valve orifice size, in/outlet size, piping clase and dimensions' selection.
"""


class PSV:
    '''
Standard Effective Orifice Areas and Letter Designations.  
From API Standard 526 7th Edition, Sep 2017
    '''
    
    def __init__(self, value = 0.0, unit = 'in2'):    # 默认格式：(0.0, 'in2') 
        self.value = value
        self.unit = unit
        self.type = type
        self.phase = 
        self.setpressure = 
        
    
    
    Code = "API Standard 526"
    
    Rev = 7
# Standard Effective Orifice Areas and Letter Designations       
    Orifice = {'D': 0.11
               'E': 0.196,
               'F': 0.307,
               'G': 0.503,
               'H': 0.785,
               'J': 1.287,
               'K': 1.838,
               'L': 2.853,
               'M': 3.60,
               'N': 4.34,
               'P': 6.38,
               'Q': 11.05,
               'R': 16.00,
               'T': 26.00,
             }

  
  # Orifice selection主函数，输入orifice 面积，Return is the designation "D,E,F,G.......  如果orifice area 大于26.00 ('T' size)， 返回 'Multiple'
    def size(self, area):
        Or = 'Multiple'
        for i in Orifice.item():  #从小到大遍历 'orifice'.
            if area <= i[1]:
                break
            else:
                  Or = i[0]
        return Or
if __name__== "__main__":
   psv1401= PSV.size(3.2)

    unit2 = unit1 / 2


    print(unit1.SI_value)
    print(unit2.value)
