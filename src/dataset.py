import pandas as pd
from PIL import Image
import torch
from torch.utils.data import Dataset


class HouseDataset(Dataset):
    def __init__(self, dataframe, feature_cols):
        self.df = dataframe.reset_index(drop=True)
        self.feature_cols = feature_cols

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.loc[idx]

        tabular = torch.tensor(
            row[self.feature_cols].astype(float).values,
            dtype=torch.float32
        )

        image = Image.open(row["image_path"]).convert("RGB")
        image = torch.tensor(
            list(image.getdata()),
            dtype=torch.float32
        ).view(256, 256, 3).permute(2, 0, 1) / 255.0

        price = torch.tensor(float(row["price"]), dtype=torch.float32)

        return tabular, image, price
