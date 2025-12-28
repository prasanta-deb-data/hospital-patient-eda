# Main pipeline runner
"""
Main Pipeline Runner
Author: Prasanta Kumar Deb
Project: Hospital Patient Data EDA

This script runs the full pipeline:
1. Data Generation
2. Data Cleaning & Feature Engineering
3. Exploratory Data Analysis (EDA)
"""

# =====================================================
# Fix module import path
# =====================================================
import sys
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# =====================================================
# Imports
# =====================================================
from src.logger import logger

# =====================================================
# Helper function
# =====================================================
def run_script(script_relative_path):
    """
    Runs a Python script using the same Python interpreter
    as the pipeline (important for venv compatibility).
    """
    script_path = os.path.join(BASE_DIR, script_relative_path)

    logger.info(f"Starting script: {script_relative_path}")

    result = subprocess.run(
        [sys.executable, script_path],  # 🔑 THIS IS THE FIX
        text=True,
        capture_output=True
    )

    if result.stdout:
        logger.info(f"STDOUT from {script_relative_path}:\n{result.stdout}")

    if result.returncode != 0:
        logger.error(f"Script failed: {script_relative_path}")
        logger.error(f"STDERR:\n{result.stderr}")
        raise RuntimeError(
            f"Pipeline stopped due to error in {script_relative_path}"
        )

    logger.info(f"Completed script: {script_relative_path}")



# =====================================================
# Main Pipeline
# =====================================================
if __name__ == "__main__":
    logger.info("========== PIPELINE STARTED ==========")

    try:
        run_script("scripts/generate_hospital_data.py")
        run_script("scripts/data_cleaning.py")
        run_script("scripts/eda.py")

        logger.info("========== PIPELINE COMPLETED SUCCESSFULLY ==========")

    except Exception as e:
        logger.exception("Pipeline execution failed")
        raise
