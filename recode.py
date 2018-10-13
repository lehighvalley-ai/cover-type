import pandas as pd

df = pd.read_csv('cover_type.csv')

df['cover_type'] = df['cover_type'].map({
    1: 'Spruce/Fir',
    2: 'Lodgepole Pine',
    3: 'Ponderosa Pine',
    4: 'Cottonwood/Willow',
    5: 'Aspen',
    6: 'Douglas-fir',
    7: 'Krummholz'
})

df.to_csv('recoded.csv', index=False)
