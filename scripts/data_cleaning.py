"""
Data Cleaning & Feature Engineering
Author: Prasanta Kumar Deb
Project: Hospital Patient Data EDA
"""

import sys
import os

# -----------------------------------------------------
# Fix module import path
# -----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import pandas as pd
from src.logger import logger
from src.config_loader import load_config



# =====================================================
# Load Configuration
# =====================================================
config = load_config()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, config["paths"]["raw_data"])
PROCESSED_DIR = os.path.join(BASE_DIR, config["paths"]["processed_data"])

os.makedirs(PROCESSED_DIR, exist_ok=True)

logger.info("Data cleaning script started")

# =====================================================
# Load Raw Data
# =====================================================
try:
    patients = pd.read_csv(os.path.join(RAW_DIR, "patients.csv"))
    admissions = pd.read_csv(os.path.join(RAW_DIR, "admissions.csv"))
    diagnosis = pd.read_csv(os.path.join(RAW_DIR, "diagnosis.csv"))
    treatments = pd.read_csv(os.path.join(RAW_DIR, "treatments.csv"))
    outcomes = pd.read_csv(os.path.join(RAW_DIR, "outcomes.csv"))

    logger.info("All raw datasets loaded successfully")

except Exception as e:
    logger.error(f"Error loading raw data: {e}")
    raise

# =====================================================
# Date Conversion
# =====================================================
admissions["admission_date"] = pd.to_datetime(admissions["admission_date"])
admissions["discharge_date"] = pd.to_datetime(admissions["discharge_date"])

logger.info("Date columns converted to datetime")

# =====================================================
# Feature Engineering
# =====================================================
admissions["length_of_stay"] = (
    admissions["discharge_date"] - admissions["admission_date"]
).dt.days

logger.info("Feature created: length_of_stay")

# =====================================================
# Merge Datasets
# =====================================================
df = admissions.merge(patients, on="patient_id", how="left")
df = df.merge(diagnosis, on="admission_id", how="left")
df = df.merge(treatments, on="admission_id", how="left")
df = df.merge(outcomes, on="admission_id", how="left")

logger.info("All datasets merged successfully")

# =====================================================
# Data Cleaning & Validation
# =====================================================
initial_rows = df.shape[0]

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df["severity"] = df["severity"].fillna("Unknown")
df["outcome"] = df["outcome"].fillna("Unknown")

# Remove invalid length of stay
df = df[df["length_of_stay"] >= 0]

final_rows = df.shape[0]

logger.info(f"Rows before cleaning: {initial_rows}")
logger.info(f"Rows after cleaning: {final_rows}")

# =====================================================
# Save Cleaned Dataset
# =====================================================
output_path = os.path.join(PROCESSED_DIR, "hospital_patient_cleaned.csv")
df.to_csv(output_path, index=False)

logger.info("Cleaned dataset saved successfully")
logger.info(f"Output file path: {output_path}")
logger.info(f"Final dataset shape: {df.shape}")

logger.info("Data cleaning script completed successfully")
