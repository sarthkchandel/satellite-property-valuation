import os
import requests
import pandas as pd

DATA_PATH = "data/raw/train.xlsx"
IMAGE_DIR = "data/images/train"

os.makedirs(IMAGE_DIR, exist_ok=True)


def download_image(lat, lon, save_path, zoom=18):
    url = (
        f"https://maps.wikimedia.org/img/osm-intl,"
        f"{zoom},{lat},{lon},256x256.png"
    )
    r = requests.get(url)
    if r.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(r.content)
        return True
    return False


def main():
    df = pd.read_excel(DATA_PATH).head(5)
    for idx, row in df.iterrows():
        lat = row["lat"]
        lon = row["long"]
        path = os.path.join(IMAGE_DIR, f"house_{idx}.png")
        if download_image(lat, lon, path):
            print(f"Downloaded image {idx}")
        else:
            print(f"Failed image {idx}")


if __name__ == "__main__":
    main()
