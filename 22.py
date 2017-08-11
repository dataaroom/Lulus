# python3



def unitstarnd(value, unit,category)    # # 将输入单位转换成国际标准单位。
#TODO: 
    if unit in i.keys():
            out = convert(i,unit,getattr(i,unit)[0],value)     #调用convert函数。
            return out
     
