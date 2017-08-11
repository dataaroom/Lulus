# python3



def stdconvert(self, value, inputUnit,category)    # # 将输入单位转换成国际标准单位。
    if type == 'T':
        result = Units.convert_t(inputUnit,'K', value)            
        return result        
    else:
        in_factor = 1.0            
        out_factor = 1.0         # 假设单位库的标准单位的系数等于1.0.      
        catg = getattr(Units,type).items() #  catg is a dict. 调取用户所选的单位参数表，搜索输入和输出，并进行计算。返回计算结果。
             
        for i,j in catg:
            if inputUnit == i:          
                in_factor = j[0]       
        result = value * out_factor / in_factor            
        return result
