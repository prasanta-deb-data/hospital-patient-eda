# Data cleaning logic
"""
Data Cleaning & Feature Engineering
Author: Prasanta Kumar Deb
Project: Hospital Patient Data EDA
"""

import pandas as pd
import os

# =====================================================
# Resolve Project Root
# =====================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

os.makedirs(PROCESSED_DIR, exist_ok=True)

# =====================================================
# Load Raw Data
# =====================================================
patients = pd.read_csv(os.path.join(RAW_DIR, "patients.csv"))
admissions = pd.read_csv(os.path.join(RAW_DIR, "admissions.csv"))
diagnosis = pd.read_csv(os.path.join(RAW_DIR, "diagnosis.csv"))
treatments = pd.read_csv(os.path.join(RAW_DIR, "treatments.csv"))
outcomes = pd.read_csv(os.path.join(RAW_DIR, "outcomes.csv"))

print("✅ Raw data loaded successfully")

# =====================================================
# Convert Date Columns
# =====================================================
admissions["admission_date"] = pd.to_datetime(admissions["admission_date"])
admissions["discharge_date"] = pd.to_datetime(admissions["discharge_date"])

# =====================================================
# Feature Engineering
# =====================================================
admissions["length_of_stay"] = (
    admissions["discharge_date"] - admissions["admission_date"]
).dt.days

# =====================================================
# Merge Datasets
# =====================================================
df = admissions.merge(patients, on="patient_id", how="left")
df = df.merge(diagnosis, on="admission_id", how="left")
df = df.merge(treatments, on="admission_id", how="left")
df = df.merge(outcomes, on="admission_id", how="left")

print("✅ Datasets merged successfully")

# =====================================================
# Data Cleaning
# =====================================================
# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (if any)
df["severity"].fillna("Unknown", inplace=True)
df["outcome"].fillna("Unknown", inplace=True)

# Validate length_of_stay
df = df[df["length_of_stay"] >= 0]

# =====================================================
# Save Cleaned Data
# =====================================================
output_file = os.path.join(PROCESSED_DIR, "hospital_patient_cleaned.csv")
df.to_csv(output_file, index=False)

print("✅ Cleaned dataset saved successfully")
print(f"📂 Location: {output_file}")
print(f"📊 Final dataset shape: {df.shape}")
