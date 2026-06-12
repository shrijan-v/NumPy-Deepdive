# 📊 30-Day Data Analytics Internship — Python & Pandas

> A structured, hands-on curriculum covering Python, NumPy, Pandas, Data Visualization,
> SQL, and Machine Learning fundamentals — one focused task per day.

---

## 🗂️ Repository Structure

```
30-day-data-analytics/
├── README.md
├── day01/
├── day02/
├── ...
├── day06/
│   └── day6_numpy.py       ← NumPy Deep Dive
└── day07/
```

---

## 📅 Day 6 — NumPy Deep Dive

**Phase:** 2 — Python & Pandas
**Type:** Practical · Tool
**File:** `day06/day6_numpy.py`

### 🎯 Objective

Learn NumPy inside-out — arrays, indexing, math operations, broadcasting, and
reshaping. By end of day, be comfortable using NumPy as the backbone of
data computation.

---

### ✅ Tasks Completed

| # | Task | Key Concepts |
|---|------|--------------|
| 1 | Creating Arrays | `np.array`, `zeros`, `ones`, `arange`, `linspace`, `random` |
| 2 | Array Properties | `shape`, `ndim`, `size`, `dtype`, `itemsize` |
| 3 | Indexing & Slicing | Row/column access, sub-matrix, boolean masking |
| 4 | Reshaping & Flattening | `reshape`, `flatten`, `transpose` |
| 5 | Math Operations | Vectorized ops, aggregations (`sum`, `mean`, `std`) |
| 6 | Broadcasting | Shape alignment, column-mean centering |
| 7 | Linear Algebra | `np.dot`, `@`, `linalg.det`, `linalg.inv` |
| 🏆 | Student Score Analyzer | Full challenge using all concepts |

---

### 🏆 Daily Challenge — Student Score Analyzer

Built a complete score analysis system using **NumPy only** (no Pandas):

- 30 students × 5 subjects, random scores 0–100
- Per-student average using `axis=1`
- Highest and lowest scoring student via `np.argmax` / `np.argmin`
- Count of students scoring above 75 in **all** subjects
- Min–Max normalization: `(x - min) / (max - min)`
- Summary: class average, top student, pass rate %

---

### 🧠 Key NumPy Concepts Covered

| Concept | Description |
|---------|-------------|
| `ndarray` | Core N-dimensional array — homogeneous, contiguous memory |
| `shape` | Tuple of dimension sizes e.g. `(30, 5)` |
| `dtype` | Element data type: `int64`, `float64`, `bool` etc. |
| Indexing | `a[row, col]` — zero-based multi-dimensional access |
| Slicing | `a[start:stop]` — returns a memory-efficient view |
| Broadcasting | Operations on arrays with compatible but different shapes |
| `reshape` | Change dimensions without copying data |
| `transpose` | Swap axes via `.T` |
| `flatten` | Collapse N-D array to 1-D copy |
| Vectorized ops | Element-wise math at C speed — no Python loops |
| Aggregation | `sum`, `mean`, `std`, `min`, `max` across axes |
| Linear algebra | `np.linalg` — `det`, `inv`, `dot` backed by LAPACK/BLAS |

---

### ⚙️ Setup & Usage

**Requirements**

- Python 3.8+
- NumPy

**Install dependencies**

```bash
pip install numpy
```

**Run the script**

```bash
python day06/day6_numpy.py
```

**Run in Jupyter (recommended)**

```bash
pip install jupyter
jupyter notebook
```

Then open or create `day06/day6_numpy.ipynb` and paste the functions cell by cell.

---

### 📦 Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243?style=flat&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=flat&logo=visual-studio-code&logoColor=white)

---

### 📈 Progress Tracker

| Day | Topic | Status |
|-----|-------|--------|
| 01 | Python Basics | ⬜ |
| 02 | Control Flow & Functions | ⬜ |
| 03 | OOP in Python | ⬜ |
| 04 | File Handling & Exceptions | ⬜ |
| 05 | Python for Data — Intro | ⬜ |
| **06** | **NumPy Deep Dive** | ✅ **Done** |
| 07 | Pandas Basics | ⬜ |
| 08 | Data Visualization | ⬜ |
| 09 | Exploratory Data Analysis | ⬜ |
| 10 | Data Cleaning | ⬜ |
| 11–30 | SQL, ML, Projects... | ⬜ |

---

### 📁 What's Inside `day6_numpy.py`

```
day6_numpy.py
│
├── section_header()          — utility: prints section banners
├── task_header()             — utility: prints task labels
│
├── task1_creating_arrays()   — 7 array creation methods + practice
├── task2_array_properties()  — shape, ndim, size, dtype, itemsize
├── task3_indexing_slicing()  — indexing, slicing, boolean mask + practice
├── task4_reshaping()         — reshape 1D→3D, flatten, transpose
├── task5_math_operations()   — vectorized math + aggregations
├── task6_broadcasting()      — broadcast add + column centering + practice
├── task7_linear_algebra()    — dot, @, det, inv + identity verification
│
├── challenge_student_score_analyzer()  — full daily challenge
├── print_concept_glossary()            — 12-concept plain-English glossary
├── print_lessons_learned()             — task-by-task takeaways
│
└── main()                    — entry point, calls all functions
```

---

### 🔗 Resources

- [NumPy Official Docs](https://numpy.org/doc/stable/)
- [NumPy Cheat Sheet — DataCamp](https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python)
- [Python PEP-8 Style Guide](https://peps.python.org/pep-0008/)

---

### 👤 Author

**Your Name**
Data Analytics Intern · 30-Day Curriculum
[GitHub](https://github.com/your-username) · [LinkedIn](https://linkedin.com/in/your-profile)

---

*Part of the 30-Day Data Analytics Internship Curriculum — Phase 2: Python & Pandas*
