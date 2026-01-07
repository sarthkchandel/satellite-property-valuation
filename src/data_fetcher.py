"""
data_fetcher.py

This module is responsible for fetching satellite imagery for each property
using latitude and longitude coordinates.

NOTE:
During development, direct access to external satellite imagery APIs
(Google Maps, Mapbox, Sentinel Hub) was restricted due to billing
and access limitations.

To ensure reproducibility and pipeline completeness, this script
demonstrates the intended image-fetching interface while local
static images are used for experimentation.

The pipeline is API-agnostic and can be extended by replacing
the placeholder logic with a real API call.
"""

import os
import shutil


def fetch_image(lat, lon, save_path):
    """
    Placeholder function for satellite image fetching.

    Parameters:
    - lat (float): Latitude of the property
    - lon (float): Longitude of the property
    - save_path (str): Destination path to save the image

    Returns:
    - bool: True if image is successfully assigned
    """

    # Placeholder logic:
    # Instead of calling a paid API, we copy a local static image.
    # This keeps the multimodal pipeline functional and reproducible.

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    placeholder_image = "data/images/train/house_0.png"

    if not os.path.exists(placeholder_image):
        return False

    shutil.copy(placeholder_image, save_path)
    return True


def main():
    """
    Example usage of the image fetching interface.
    """

    lat, lon = 47.6062, -122.3321
    save_path = "data/images/train/example.png"

    success = fetch_image(lat, lon, save_path)

    if success:
        print("Image assigned successfully")
    else:
        print("Image assignment failed")


if __name__ == "__main__":
    main()
