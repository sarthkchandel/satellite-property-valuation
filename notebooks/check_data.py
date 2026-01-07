import pandas as pd

train_path = "data/raw/train.xlsx"
test_path = "data/raw/test.xlsx"

train_df = pd.read_excel(train_path)
test_df = pd.read_excel(test_path)

print("Train shape:", train_df.shape)
print("Test shape:", test_df.shape)

print("\nTrain columns:")
print(train_df.columns)
