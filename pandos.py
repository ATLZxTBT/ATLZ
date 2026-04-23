import pandas as pd

data = {"Mês": [1,2,3,4,5,6,7,8,9,10,11,12],
        "Entregas": [1,2,3,4,5,6,7,8,9,10,11,12]
        }

df = pd.DataFrame(data)
print(df)