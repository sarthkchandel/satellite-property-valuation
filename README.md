# Satellite Imagery-Based Property Valuation

## Overview

This project builds a **multimodal regression pipeline** to predict residential property prices by combining **tabular housing attributes** with **satellite-style imagery**. The objective is to capture both structural factors (size, rooms, construction quality) and environmental context (neighborhood patterns) to improve valuation accuracy.

The project was developed as part of the **CDC × YHills Open Projects 2025–2026**.

---

## Objectives

- Predict house prices using structured (tabular) data
- Integrate visual context via satellite-style images
- Compare tabular-only vs multimodal models
- Demonstrate multimodal data fusion using deep learning
- Build a clean, reproducible machine learning pipeline

---

## Dataset

### Tabular Data

- Source: House Sales dataset (Excel format)
- Key features:
  - `price` (target)
  - `bedrooms`, `bathrooms`
  - `sqft_living`, `sqft_lot`
  - `floors`, `grade`, `condition`
  - `waterfront`, `view`
  - `lat`, `long`

### Image Data

- Images are stored locally in `data/images/train/`
- Each property row is linked to a corresponding image via file paths
- Due to API billing and access constraints, **local static imagery** was used during experimentation
- The pipeline is **API-agnostic** and can be extended to:
  - Google Maps Static API
  - Mapbox Static Images API
  - Sentinel Hub

---

## Project Structure

satellite-property-valuation/
│
├── README.md
├── data/
│ ├── raw/
│ │ ├── train.xlsx
│ │ └── test.xlsx
│ └── images/
│ └── train/
│ ├── house_0.png
│ ├── house_1.png
│ └── ...
│
├── notebooks/
│ ├── preprocessing.ipynb
│ ├── model_training.ipynb
│
├── src/
│ ├── dataset.py
│ ├── data_fetcher.py
│ ├── model.py
│ └── create_images.py
│
├── outputs/
│ └── 23411033_final.csv
│
└── venv/

---

## Models

### 1. Tabular Baseline Model

- Algorithm: **Random Forest Regressor**
- Input: Structured housing features
- Performance:
  - RMSE ≈ **126,000**
  - R² ≈ **0.87**

This model serves as a strong baseline for comparison.

---

### 2. Multimodal Model

- **Tabular branch**: Multi-layer Perceptron (MLP)
- **Image branch**: Convolutional Neural Network (CNN)
- **Fusion**: Concatenation of learned embeddings
- **Output**: Predicted house price

The multimodal model was trained end-to-end on a small subset to validate the multimodal pipeline.

---

## Results

- The tabular-only model achieves strong predictive performance
- The multimodal architecture successfully integrates image and tabular data
- End-to-end training confirms the feasibility of multimodal regression

---

## How to Run

### 1. Set up environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

```

### 2. Run baseline & multimodal pipeline

Open and run the notebooks in the following order in VS Code:

```
1. notebooks/preprocessing.ipynb
2. notebooks/model_training.ipynb
```

The original `tabular_baseline.ipynb` is retained as a reference
baseline and development notebook.

This notebook includes:

- Tabular baseline model training
- Multimodal dataset creation
- Multimodal neural network definition
- End-to-end multimodal training
- Prediction generation

---

## Submission File

The final prediction file is generated at:

```
outputs/23411033_final.csv
```

### Required format

```
id,predicted_price
```

## Notes

- Satellite imagery was simulated locally due to API billing and access constraints
- The image pipeline is modular and **API-agnostic**
- The pipeline can be extended to:
  - Google Maps Static API
  - Mapbox Static Images API
  - Sentinel Hub
- The project emphasizes **multimodal learning**, **engineering clarity**, and **reproducibility**

---

## Author

**Sarthak Chandel**  
CDC × YHills Open Projects (2025–2026)
