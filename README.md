
# Data Cleaning & Reporting Automation (Power BI & Python — Week 4 Task)

An automated data preprocessing and reporting workflow built with Python (`pandas`) and Power BI. The pipeline ingests messy transactional datasets, automatically cleans missing values, handles duplicates, standardizes date formats and text strings, and loads structured outputs into Power BI for automated executive reporting.

---

## 📌 Features & Automated Workflow

- **Automated Data Quality Audit:** Detects and drops duplicate entries automatically.
- **Text & Category Normalization:** Trims whitespace and unifies inconsistent casing across columns[cite: 22].
- **Missing Value Imputation:** Fills null numerical fields using statistical median imputation[cite: 22].
- **Datetime Standardization:** Converts mixed date string formats into standard ISO date types[cite: 22].
- **Power BI Executive Summary:** Interactive visuals reporting cleaned sales performance by category and region[cite: 22].

---

## 🚀 How to Run

1. **Execute Python Automated Cleaning Pipeline:**
   ```bash
   python automate_data_cleaning.py
   ```
