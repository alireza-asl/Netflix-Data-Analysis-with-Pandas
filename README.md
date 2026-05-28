# Netflix Data Analysis with Pandas

A very beginner-friendly data analysis project using **Python**, **Pandas**, and **Matplotlib**.

This project is designed for learning and for a beginner GitHub portfolio.

---

## What this project teaches

- How to load a CSV file with `pd.read_csv()`
- Basic Pandas operations:
  - `shape`
  - `head()`
  - `info()`
  - `isnull()`
  - `dropna()`
  - `unique()`
  - `value_counts()`
  - filtering
  - sorting
- How to do simple missing-value analysis
- How to do simple data cleaning
- How to analyze genres and countries
- How to create basic charts with Matplotlib

---

## Project files

- `main.py` → Main analysis script (heavily commented)
- `requirements.txt` → Python dependencies
- `.gitignore` → Files/folders to ignore in Git
- `README.md` → Project guide

---

## Dataset

Use a Netflix CSV dataset named:

`netflix_titles.csv`

Place it in the **same folder** as `main.py`.

Example columns usually include:
- `type`
- `title`
- `country`
- `release_year`
- `listed_in`

---

## How to run

1. Create and activate a virtual environment (optional but recommended)
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python main.py
```

---

## Charts included

- Number of Movies vs TV Shows
- Top 10 Genres
- Top 10 Countries

---

## Beginner notes

- Read comments in `main.py` step-by-step.
- Try changing filters (for example, different years).
- Try plotting other columns.
- Keep experimenting and learning!
