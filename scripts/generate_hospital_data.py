"""
Generate Synthetic Hospital Patient Data
Author: Prasanta Kumar Deb
Project: Hospital Patient Data EDA
"""

# =====================================================
# Fix module import path (CRITICAL)
# =====================================================
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# =====================================================
# Imports
# =====================================================
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta

from src.logger import logger
from src.config_loader import load_config

# =====================================================
# Load Configuration
# =====================================================
config = load_config()

RAW_DATA_DIR = os.path.join(BASE_DIR, config["paths"]["raw_data"])
os.makedirs(RAW_DATA_DIR, exist_ok=True)

NUM_PATIENTS = config["data"]["num_patients"]

fake = Faker("en_IN")
random.seed(42)
np.random.seed(42)

logger.info("Data generation script started")

# =====================================================
# 1. Patients Dataset
# =====================================================
patients = []
for i in range(1, NUM_PATIENTS + 1):
    patients.append({
        "patient_id": f"P{i:05d}",
        "name": fake.name(),
        "age": random.randint(1, 90),
        "gender": random.choice(["Male", "Female"]),
        "blood_group": random.choice(
            ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        ),
        "city": random.choice(
            ["Guwahati", "Silchar", "Kolkata", "Delhi", "Mumbai", "Bangalore"]
        )
    })

patients_df = pd.DataFrame(patients)
logger.info("Patients dataset created")

# =====================================================
# 2. Admissions Dataset
# =====================================================
departments = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Gynecology",
    "General Medicine"
]

admission_types = ["Emergency", "Planned"]

admissions = []
for i, patient_id in enumerate(patients_df["patient_id"], start=1):
    admission_date = fake.date_between(start_date="-1y", end_date="today")
    stay_days = random.randint(1, 20)

    admissions.append({
        "admission_id": f"A{i:05d}",
        "patient_id": patient_id,
        "admission_date": admission_date,
        "discharge_date": admission_date + timedelta(days=stay_days),
        "department": random.choice(departments),
        "admission_type": random.choice(admission_types)
    })

admissions_df = pd.DataFrame(admissions)
logger.info("Admissions dataset created")

# =====================================================
# 3. Diagnosis Dataset
# =====================================================
disease_map = {
    "Cardiology": ["Heart Attack", "Hypertension"],
    "Neurology": ["Stroke", "Migraine"],
    "Orthopedics": ["Fracture", "Arthritis"],
    "Gynecology": ["Ovarian Cyst", "Pregnancy Complication"],
    "General Medicine": ["Fever", "Diabetes"]
}

diagnosis = []
for i, row in admissions_df.iterrows():
    diagnosis.append({
        "diagnosis_id": f"D{i+1:05d}",
        "admission_id": row["admission_id"],
        "disease": random.choice(disease_map[row["department"]]),
        "severity": random.choice(["Mild", "Moderate", "Critical"])
    })

diagnosis_df = pd.DataFrame(diagnosis)
logger.info("Diagnosis dataset created")

# =====================================================
# 4. Treatments Dataset
# =====================================================
treatments = []
for i, row in admissions_df.iterrows():
    treatments.append({
        "treatment_id": f"T{i+1:05d}",
        "admission_id": row["admission_id"],
        "doctor_name": fake.name(),
        "treatment_type": random.choice(
            ["Medication", "Surgery", "ICU Care"]
        ),
        "treatment_cost": random.randint(5000, 400000)
    })

treatments_df = pd.DataFrame(treatments)
logger.info("Treatments dataset created")

# =====================================================
# 5. Outcomes Dataset
# =====================================================
outcomes = []
for i, row in diagnosis_df.iterrows():
    outcome = random.choices(
        ["Recovered", "Referred", "Deceased"],
        weights=[0.75, 0.15, 0.10]
    )[0]

    outcomes.append({
        "outcome_id": f"O{i+1:05d}",
        "admission_id": row["admission_id"],
        "outcome": outcome,
        "follow_up_required": (
            "Yes" if outcome == "Recovered" and random.random() > 0.5 else "No"
        )
    })

outcomes_df = pd.DataFrame(outcomes)
logger.info("Outcomes dataset created")

# =====================================================
# Save CSV Files
# =====================================================
patients_df.to_csv(os.path.join(RAW_DATA_DIR, "patients.csv"), index=False)
admissions_df.to_csv(os.path.join(RAW_DATA_DIR, "admissions.csv"), index=False)
diagnosis_df.to_csv(os.path.join(RAW_DATA_DIR, "diagnosis.csv"), index=False)
treatments_df.to_csv(os.path.join(RAW_DATA_DIR, "treatments.csv"), index=False)
outcomes_df.to_csv(os.path.join(RAW_DATA_DIR, "outcomes.csv"), index=False)

logger.info("All hospital datasets generated successfully")
logger.info(f"Raw data location: {RAW_DATA_DIR}")
logger.info("Data generation script completed successfully")
