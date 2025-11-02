import collections

mobile=collections.namedtuple('Mobile','Brand Model Price Colors')

mobileList=[]

mobile1=mobile('iphon','15ProMax',85000000,['Black','White'])
mobile2=mobile('iphon','13ProMax',55000000,['Blue','Gold','Gray'])
mobile3=mobile('Samsung','GalexyS23',55000000,['Purple','Green','Black']) 
mobile4=mobile('Samsung','GalexyS24',64000000,['Black','Yellow','Gray','Purple'])
mobile5=mobile('Samsung','GalexyA55',22000000,['Navy blue','Ice blue'])
mobile6=mobile('Samsung','GalexyA54',18000000,['Black','White','Yellow'])
mobile7=mobile('Samsung','GalexyA25',13000000,['Yellow','Navy blue']) 
mobile8=mobile('xiaomi','RedmiNote13',11000000,['Black','Green','Blue'])
mobile9=mobile('xiaomi','PocoX6',18000000,['Yellow','Gray'])                                  
mobile10=mobile('xiaomi','13TPro',34000000,['Black','Blue'])  

mobileList.append(mobile1)
mobileList.append(mobile2)
mobileList.append(mobile3)
mobileList.append(mobile4)
mobileList.append(mobile5)
mobileList.append(mobile6)
mobileList.append(mobile7)
mobileList.append(mobile8)
mobileList.append(mobile9)
mobileList.append(mobile10)

for item in mobileList:
    print(item._asdict())
 

                                                                                                                                                                                                                                             