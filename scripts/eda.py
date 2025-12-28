"""
Exploratory Data Analysis (EDA)
Author: Prasanta Kumar Deb
Project: Hospital Patient Data EDA
"""

# =====================================================
# Fix module import path
# =====================================================
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# =====================================================
# Imports
# =====================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.logger import logger
from src.config_loader import load_config

# =====================================================
# Load Config
# =====================================================
config = load_config()

PROCESSED_DIR = os.path.join(BASE_DIR, config["paths"]["processed_data"])
FIGURES_DIR = os.path.join(BASE_DIR, "outputs", "figures")
REPORTS_DIR = os.path.join(BASE_DIR, "outputs", "reports")

os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

FIGSIZE = (
    config["plots"]["figsize"]["width"],
    config["plots"]["figsize"]["height"]
)

logger.info("EDA script started")

# =====================================================
# Load Cleaned Data
# =====================================================
try:
    df = pd.read_csv(
        os.path.join(PROCESSED_DIR, "hospital_patient_cleaned.csv")
    )
    logger.info("Cleaned dataset loaded successfully")
except Exception as e:
    logger.error(f"Failed to load cleaned data: {e}")
    raise

sns.set(style="whitegrid")

# =====================================================
# 1. Age Distribution
# =====================================================
plt.figure(figsize=FIGSIZE)
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Age Distribution of Patients")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "age_distribution.png"))
plt.close()

logger.info("Saved figure: age_distribution.png")

# =====================================================
# 2. Gender Distribution
# =====================================================
plt.figure(figsize=FIGSIZE)
sns.countplot(x="gender", data=df)
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "gender_distribution.png"))
plt.close()

logger.info("Saved figure: gender_distribution.png")

# =====================================================
# 3. Top Diseases
# =====================================================
plt.figure(figsize=FIGSIZE)
df["disease"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Diseases")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "top_diseases.png"))
plt.close()

logger.info("Saved figure: top_diseases.png")

# =====================================================
# 4. Length of Stay by Department
# =====================================================
plt.figure(figsize=FIGSIZE)
sns.boxplot(x="department", y="length_of_stay", data=df)
plt.xticks(rotation=45)
plt.title("Length of Stay by Department")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "length_of_stay_by_department.png"))
plt.close()

logger.info("Saved figure: length_of_stay_by_department.png")

# =====================================================
# 5. Treatment Cost by Outcome
# =====================================================
plt.figure(figsize=FIGSIZE)
sns.boxplot(x="outcome", y="treatment_cost", data=df)
plt.title("Treatment Cost by Outcome")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "treatment_cost_by_outcome.png"))
plt.close()

logger.info("Saved figure: treatment_cost_by_outcome.png")

# =====================================================
# 6. Admission Type vs Outcome (REPORT + FIGURE)
# =====================================================
admission_outcome = pd.crosstab(
    df["admission_type"],
    df["outcome"],
    normalize="index"
)

# Save report
admission_outcome.to_csv(
    os.path.join(REPORTS_DIR, "admission_type_vs_outcome.csv")
)

# Plot
admission_outcome.plot(
    kind="bar",
    stacked=True,
    figsize=FIGSIZE
)
plt.title("Admission Type vs Outcome")
plt.ylabel("Proportion")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "admission_type_vs_outcome.png"))
plt.close()

logger.info("Saved report & figure: admission_type_vs_outcome")

# =====================================================
# 7. Correlation Heatmap (REPORT + FIGURE)
# =====================================================
numeric_cols = ["age", "length_of_stay", "treatment_cost"]

correlation_df = df[numeric_cols].corr()
correlation_df.to_csv(
    os.path.join(REPORTS_DIR, "correlation_matrix.csv")
)

plt.figure(figsize=FIGSIZE)
sns.heatmap(correlation_df, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "correlation_heatmap.png"))
plt.close()

logger.info("Saved report & figure: correlation_matrix")

# =====================================================
# 8. Department Summary Report
# =====================================================
department_summary = df.groupby("department").agg(
    total_patients=("patient_id", "count"),
    avg_length_of_stay=("length_of_stay", "mean"),
    avg_treatment_cost=("treatment_cost", "mean")
).round(2)

department_summary.to_csv(
    os.path.join(REPORTS_DIR, "department_summary.csv")
)

logger.info("Saved report: department_summary.csv")

logger.info("EDA script completed successfully")
