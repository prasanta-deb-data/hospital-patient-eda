import os

PROJECT_NAME = "hospital-patient-eda"

BASE_DIRS = [
    "data/raw",
    "data/processed",
    "notebooks",
    "scripts",
    "src",
    "outputs/figures",
    "outputs/reports",
    "logs",
    "tests"
]

FILES = {
    "notebooks/hospital_patient_eda.ipynb": "",
    "scripts/generate_hospital_data.py": "# Data generation script\n",
    "scripts/data_cleaning.py": "# Data cleaning logic\n",
    "scripts/eda.py": "# EDA logic\n",
    "src/__init__.py": "",
    "src/config.py": "# Project configurations\n",
    "src/utils.py": "# Utility functions\n",
    "run_pipeline.py": "# Main pipeline runner\n",
    "README.md": "# Hospital Patient Data EDA\n",
    "requirements.txt": "pandas\nnumpy\nmatplotlib\nseaborn\nfaker\n",
    ".gitignore": """__pycache__/
*.pyc
*.ipynb_checkpoints
.env
venv/
data/processed/
logs/
"""
}

def create_structure():
    print("📁 Creating project structure...")

    os.makedirs(PROJECT_NAME, exist_ok=True)

    for dir_path in BASE_DIRS:
        full_path = os.path.join(PROJECT_NAME, dir_path)
        os.makedirs(full_path, exist_ok=True)

        # Keep empty folders in GitHub
        gitkeep_path = os.path.join(full_path, ".gitkeep")
        with open(gitkeep_path, "w") as f:
            pass

    for file_path, content in FILES.items():
        full_file_path = os.path.join(PROJECT_NAME, file_path)
        with open(full_file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print("✅ Professional project structure created successfully!")
    print(f"📂 Project location: ./{PROJECT_NAME}")

if __name__ == "__main__":
    create_structure()
