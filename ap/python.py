# Load your dataset
df = pd.read_csv("train data.csv") 
# Identify unique product combinations
unique_combinations = df.groupby(['ProductType', 'Manufacturer', 'Area Code', 'Sourcing Channel', 'Product Size', 'Product Type']).size().reset_index().rename(columns={0:'NumUnits'})

# Display the unique combinations and the number of units for each combination
print(unique_combinations)
