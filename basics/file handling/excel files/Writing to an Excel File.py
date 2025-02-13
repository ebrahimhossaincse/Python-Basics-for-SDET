import pandas as pd

# Writing DataFrame to an Excel file
data = {
    'Name': ['Ebrahim', 'Hossain', 'Jewel'],
    'Age': [25, 26, 28]
}

df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)
