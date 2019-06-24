from pandas import DataFrame
import pandas as pd
import numpy as np


#data={
    #'date':pd.date_range('20000101',periods=10),
    #'gender':np.random.randint(0,2,size=10),
    #'height':np.random.randint(40,50,size=10),
    #'weight':np.random.randint(150,180,size=10)
#}
#a=DataFrame(data)
#print(a)

#print(a.groupby('gender').sum())
#print(a.groupby('gender').size())
data = [
('Tokyo', 'JP', 36.933,(35.234,139.23)),
('Delhi NCR', 'IN', 21.4,(28.14,77.29)),
('Mexico City','MX', 20.1,(19.332, -99.12)),
('New York-Neawark', 'US', 20.12,(40.42,-74.2)),
('Sao Paulo', 'BR', 19.42,(-23.523, -46.5))
]
a = DataFrame(data)
print(a)
print("^"*30)
from operator import itemgetter
for city in sorted(data, key=itemgetter(1,2)):
    print(city)
