"""
============================================================
  DAY 6 — NumPy Deep Dive
  Phase 2: Python & Pandas · Practical · Tool
  Author  : Intern Submission
  Purpose : Complete NumPy walkthrough — arrays, indexing,
            math, broadcasting, reshaping, linear algebra,
            and a Student Score Analyzer challenge.
============================================================
"""

import numpy as np


# ────────────────────────────────────────────────────────────
#  HELPER UTILITIES
# ────────────────────────────────────────────────────────────

def section_header(title: str) -> None:
    """Print a decorated section header for readability."""
    width = 60
    print("\n" + "=" * width)
    print(f"  {title}")
    print("=" * width)


def task_header(label: str) -> None:
    """Print a smaller task label."""
    print(f"\n{'─' * 50}")
    print(f"  {label}")
    print(f"{'─' * 50}")


# ============================================================
#  TASK 1 — CREATING ARRAYS
# ============================================================

def task1_creating_arrays() -> None:
    section_header("TASK 1 — CREATING ARRAYS")

    # --- From a Python list ---
    a = np.array([1, 2, 3, 4, 5])
    print("Array from list         :", a)

    # --- All-zeros 1-D array of length 5 ---
    zeros = np.zeros(5)
    print("Zeros (size 5)          :", zeros)

    # --- All-ones 3×3 matrix ---
    ones = np.ones((3, 3))
    print("Ones (3×3):\n", ones)

    # --- Even numbers 0–18 using arange(start, stop, step) ---
    evens = np.arange(0, 20, 2)          # stop=20 is exclusive
    print("Even numbers 0–18       :", evens)

    # --- 5 equally spaced values between 0 and 1 (inclusive) ---
    linsp = np.linspace(0, 1, 5)
    print("Linspace 0→1 (5 pts)    :", linsp)

    # --- 4×4 uniform random values in [0, 1) ---
    rand_uniform = np.random.rand(4, 4)
    print("Random uniform (4×4):\n", rand_uniform.round(3))

    # --- 4×4 standard-normal random values (mean=0, std=1) ---
    rand_normal = np.random.randn(4, 4)
    print("Random normal (4×4):\n", rand_normal.round(3))

    # ── PRACTICE ──────────────────────────────────────────
    # np.random.randint(low, high, size) — high is exclusive,
    # so use 101 to include 100.
    task_header("Practice: 5×5 random integers 1–100")
    rand_int_5x5 = np.random.randint(1, 101, size=(5, 5))
    print("5×5 random int matrix (1–100):\n", rand_int_5x5)


# ============================================================
#  TASK 2 — ARRAY PROPERTIES
# ============================================================

def task2_array_properties() -> None:
    section_header("TASK 2 — ARRAY PROPERTIES")

    # Create a 4×5 array of random integers 1–99
    a = np.random.randint(1, 100, size=(4, 5))
    print("Array:\n", a)

    # .shape   → tuple of dimension sizes
    print("\nShape      (rows, cols) :", a.shape)

    # .ndim    → number of axes / dimensions
    print("Dimensions (ndim)       :", a.ndim)

    # .size    → total number of elements
    print("Total size              :", a.size)

    # .dtype   → data type of stored elements
    print("Data type  (dtype)      :", a.dtype)

    # .itemsize → bytes used per element
    print("Item size  (bytes)      :", a.itemsize)


# ============================================================
#  TASK 3 — INDEXING & SLICING
# ============================================================

def task3_indexing_slicing() -> None:
    section_header("TASK 3 — INDEXING & SLICING")

    a = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
    print("Base array:\n", a)

    # a[row, col] — zero-indexed
    print("\nElement at row-0, col-1          :", a[0, 1])   # → 20

    # a[:, col] — all rows, specific column
    print("Entire column 1 (index 1)        :", a[:, 1])    # → [20 50 80]

    # a[row, :] — all columns of one row
    print("Entire row 1 (index 1)           :", a[1, :])    # → [40 50 60]

    # a[row_start:row_end, col_start:col_end] — slicing a sub-matrix
    print("Top-right 2×2 sub-matrix:\n", a[0:2, 1:3])       # rows 0–1, cols 1–2

    # Boolean mask: returns a 1-D array of elements satisfying the condition
    print("Elements greater than 50         :", a[a > 50])   # → [60 70 80 90]

    # ── PRACTICE ──────────────────────────────────────────
    task_header("Practice: 6×6 random array — values > 0.5")
    arr_6x6 = np.random.rand(6, 6)           # uniform floats in [0, 1)
    print("6×6 array:\n", arr_6x6.round(3))
    print("Values > 0.5:", arr_6x6[arr_6x6 > 0.5].round(3))


# ============================================================
#  TASK 4 — RESHAPING & FLATTENING
# ============================================================

def task4_reshaping_flattening() -> None:
    section_header("TASK 4 — RESHAPING & FLATTENING")

    # 1-D array of integers 1–12
    a = np.arange(1, 13)
    print("Original 1-D array      :", a)

    # reshape(rows, cols) — total elements must stay the same (3×4 = 12)
    b = a.reshape(3, 4)
    print("\nReshaped to 3×4:\n", b)

    # 3-D reshape — (2 blocks) × (2 rows) × (3 cols) = 12
    c = a.reshape(2, 2, 3)
    print("\nReshaped to 2×2×3:\n", c)

    # flatten() always returns a *copy* as a 1-D array
    d = b.flatten()
    print("\nFlattened back to 1-D  :", d)

    # .T transposes: rows ↔ columns  →  (3,4) becomes (4,3)
    e = b.T
    print("\nTransposed 3×4 → 4×3:\n", e)


# ============================================================
#  TASK 5 — MATH OPERATIONS
# ============================================================

def task5_math_operations() -> None:
    section_header("TASK 5 — MATH OPERATIONS")

    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    # All arithmetic operations are element-wise (vectorized)
    print("a             :", a)
    print("b             :", b)
    print("\na + b         :", a + b)          # element-wise addition
    print("a * b         :", a * b)          # element-wise multiplication
    print("a ** 2        :", a ** 2)         # element-wise squaring
    print("sqrt(b)       :", np.sqrt(b))     # element-wise square root
    print("log(b)        :", np.log(b).round(4))  # element-wise natural log

    # ── Aggregations (whole array → single number) ─────────
    print("\n--- Aggregations on b ---")
    print("Sum           :", b.sum())        # 10+20+30+40 = 100
    print("Mean          :", b.mean())       # 100/4 = 25.0
    print("Std deviation :", b.std())        # spread around the mean
    print("Min           :", b.min())
    print("Max           :", b.max())


# ============================================================
#  TASK 6 — BROADCASTING
# ============================================================

def task6_broadcasting() -> None:
    section_header("TASK 6 — BROADCASTING")

    matrix = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

    row_vec = np.array([10, 20, 30])   # shape (3,)

    # Broadcasting: NumPy stretches row_vec (shape 3,) across all 3 rows
    # of matrix (shape 3×3).  No extra memory is allocated; it's virtual.
    result = matrix + row_vec
    print("matrix:\n", matrix)
    print("\nrow_vec              :", row_vec)
    print("\nmatrix + row_vec (broadcast):\n", result)

    print("""
How broadcasting works:
  • matrix shape : (3, 3)
  • row_vec shape: (   3)  → treated as (1, 3) → stretched to (3, 3)
  • NumPy adds each row_vec element to the matching column of every row.
  • Rule: dimensions are compatible when they are equal, or one of them is 1.
""")

    # ── PRACTICE ──────────────────────────────────────────
    task_header("Practice: subtract column means from a 4×4 matrix")
    mat4 = np.random.rand(4, 4)
    print("4×4 random matrix:\n", mat4.round(3))

    # axis=0 → compute along rows, giving one mean per column  → shape (4,)
    col_means = mat4.mean(axis=0)
    print("\nColumn means          :", col_means.round(3))

    # Broadcasting subtracts the (4,) vector from every row automatically
    centered = mat4 - col_means
    print("\nColumn-centered matrix (each column mean ≈ 0):\n", centered.round(3))
    print("Verify column means after centering:", centered.mean(axis=0).round(10))


# ============================================================
#  TASK 7 — LINEAR ALGEBRA BASICS
# ============================================================

def task7_linear_algebra() -> None:
    section_header("TASK 7 — LINEAR ALGEBRA BASICS")

    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[5, 6],
                  [7, 8]])

    print("Matrix A:\n", A)
    print("\nMatrix B:\n", B)

    # np.dot(A, B) — standard matrix multiplication (NOT element-wise)
    dot_result = np.dot(A, B)
    print("\nnp.dot(A, B) — matrix multiplication:\n", dot_result)

    # @ operator — Python 3.5+ shorthand for np.dot on 2-D arrays
    at_result = A @ B
    print("\nA @ B  (identical result):\n", at_result)

    # Determinant: scalar that encodes how the matrix scales area/volume.
    # det ≠ 0 means the matrix is invertible.
    det_A = np.linalg.det(A)
    print(f"\nDeterminant of A       : {det_A:.4f}")
    print("  (1×4 − 2×3 = 4−6 = −2 ✓)")

    # Inverse: A_inv such that A @ A_inv = Identity matrix
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
    print("\nVerification A @ inv(A) ≈ Identity:\n",
          (A @ inv_A).round(10))


# ============================================================
#  DAILY CHALLENGE — STUDENT SCORE ANALYZER
# ============================================================

def challenge_student_score_analyzer() -> None:
    section_header("DAILY CHALLENGE — STUDENT SCORE ANALYZER")

    # ── Step 1 ─────────────────────────────────────────────
    # 30 students × 5 subjects; scores are integers 0–100
    np.random.seed(42)   # seed for reproducibility
    scores = np.random.randint(0, 101, size=(30, 5))
    subjects = ["Math", "Science", "English", "History", "CS"]

    print("Score matrix (30 students × 5 subjects):")
    print(scores)

    # ── Step 2 — Per-student average ───────────────────────
    # axis=1 → average across the 5 columns for each of the 30 rows
    student_avg = scores.mean(axis=1)   # shape (30,)
    print("\nPer-student average scores (first 5 shown):")
    print(student_avg[:5].round(2))

    # ── Step 3 — Highest & lowest scoring students ─────────
    # np.argmax / np.argmin return the *index* of the extreme value
    top_idx    = np.argmax(student_avg)
    bottom_idx = np.argmin(student_avg)
    print(f"\nHighest scoring student → Student #{top_idx}"
          f"  (avg = {student_avg[top_idx]:.2f})")
    print(f"Lowest  scoring student → Student #{bottom_idx}"
          f"  (avg = {student_avg[bottom_idx]:.2f})")

    # ── Step 4 — Students scoring > 75 in ALL subjects ─────
    # scores > 75  gives a (30,5) boolean array.
    # .all(axis=1) is True only when every subject is > 75 → shape (30,)
    above_75_all = (scores > 75).all(axis=1)
    count_above_75 = above_75_all.sum()   # True counts as 1
    print(f"\nStudents who scored > 75 in ALL subjects: {count_above_75}")

    # ── Step 5 — Min–Max normalisation to [0, 1] ───────────
    score_min = scores.min()
    score_max = scores.max()
    normalized = (scores - score_min) / (score_max - score_min)
    print("\nNormalized score matrix (first 3 rows, rounded):")
    print(normalized[:3].round(3))

    # ── Step 6 — Summary ───────────────────────────────────
    class_average = student_avg.mean()

    # Pass = average ≥ 50 (a simple threshold)
    pass_count = (student_avg >= 50).sum()
    pass_rate  = (pass_count / 30) * 100

    print("\n" + "━" * 45)
    print("  📊  CLASS SUMMARY")
    print("━" * 45)
    print(f"  Class average score          : {class_average:.2f}")
    print(f"  Top student index            : {top_idx}  "
          f"(avg {student_avg[top_idx]:.2f})")
    print(f"  Lowest student index         : {bottom_idx}  "
          f"(avg {student_avg[bottom_idx]:.2f})")
    print(f"  Pass rate (avg ≥ 50)         : {pass_rate:.1f}%")
    print(f"  Students >75 in all subjects : {count_above_75}")
    print("━" * 45)


# ============================================================
#  CONCEPT GLOSSARY
# ============================================================

def print_concept_glossary() -> None:
    section_header("KEY NumPy CONCEPTS — GLOSSARY")

    glossary = {
        "ndarray": (
            "N-dimensional array — NumPy's core data structure. "
            "Stores homogeneous (same dtype) elements in contiguous memory, "
            "making operations orders of magnitude faster than Python lists."
        ),
        "shape": (
            "Tuple describing the size of each dimension. "
            "E.g. (30, 5) means 30 rows and 5 columns."
        ),
        "dtype": (
            "Data type of array elements (int32, float64, bool, …). "
            "Operations only happen between compatible dtypes."
        ),
        "indexing": (
            "Accessing individual elements with a[row, col] syntax. "
            "Zero-based, like Python lists."
        ),
        "slicing": (
            "Selecting sub-arrays with start:stop syntax. "
            "Returns a *view* (no copy), so edits affect the original."
        ),
        "broadcasting": (
            "Implicit stretching of smaller arrays to match a larger shape "
            "during operations — no extra memory used. "
            "Rule: dims are compatible if equal or one of them is 1."
        ),
        "reshape": (
            "Change array dimensions without copying data. "
            "Total element count must stay the same."
        ),
        "transpose": (
            "Swap axes — rows become columns and vice versa. "
            "Accessed via .T attribute or np.transpose()."
        ),
        "flatten": (
            "Collapse any N-D array into a 1-D copy. "
            "Unlike ravel(), always returns an independent copy."
        ),
        "vectorized ops": (
            "Operations applied to every element simultaneously at C speed — "
            "no Python for-loops needed. The key performance advantage of NumPy."
        ),
        "aggregation": (
            "Reduction functions (sum, mean, std, min, max) that collapse "
            "an axis or the whole array to a scalar or smaller array."
        ),
        "linear algebra": (
            "Matrix operations available in np.linalg — "
            "dot product, determinant, inverse, eigenvalues, SVD, etc."
        ),
    }

    for concept, explanation in glossary.items():
        print(f"\n  ▸ {concept.upper()}")
        # Wrap explanation at 70 chars for readability
        words = explanation.split()
        line, lines = [], []
        for word in words:
            line.append(word)
            if len(" ".join(line)) > 65:
                lines.append("    " + " ".join(line[:-1]))
                line = [word]
        lines.append("    " + " ".join(line))
        print("\n".join(lines))


# ============================================================
#  LESSONS LEARNED
# ============================================================

def print_lessons_learned() -> None:
    section_header("LESSONS LEARNED — TASK BY TASK")

    lessons = [
        ("Task 1 — Creating Arrays",
         "NumPy offers multiple factory functions (zeros, ones, arange, "
         "linspace, random) that are far faster than building lists manually."),
        ("Task 2 — Array Properties",
         "shape, ndim, size, dtype, and itemsize give instant structural "
         "insight — essential before any computation."),
        ("Task 3 — Indexing & Slicing",
         "Multi-dimensional indexing [row, col] and boolean masks let you "
         "extract exactly the data you need without loops."),
        ("Task 4 — Reshaping & Flattening",
         "Reshape / transpose / flatten manipulate array layout in O(1) time "
         "because they reuse the same memory buffer."),
        ("Task 5 — Math Operations",
         "Vectorized arithmetic and aggregations replace explicit Python loops, "
         "cutting runtimes from seconds to milliseconds."),
        ("Task 6 — Broadcasting",
         "Broadcasting elegantly handles operations on arrays with different "
         "but compatible shapes — a cornerstone of clean data science code."),
        ("Task 7 — Linear Algebra",
         "np.linalg provides production-quality matrix math (dot, det, inv) "
         "backed by LAPACK/BLAS — the same libraries used in MATLAB."),
        ("Daily Challenge",
         "Combining all concepts (slicing, axis operations, boolean masks, "
         "normalisation) in one realistic problem reinforces how they interplay."),
    ]

    for title, lesson in lessons:
        print(f"\n  ✅  {title}")
        print(f"     {lesson}")


# ============================================================
#  MAIN
# ============================================================

def main() -> None:
    print("\n" + "█" * 60)
    print("   DAY 6 — NumPy Deep Dive  |  Internship Submission")
    print("█" * 60)

    task1_creating_arrays()
    task2_array_properties()
    task3_indexing_slicing()
    task4_reshaping_flattening()
    task5_math_operations()
    task6_broadcasting()
    task7_linear_algebra()
    challenge_student_score_analyzer()
    print_concept_glossary()
    print_lessons_learned()

    print("\n" + "=" * 60)
    print("  ✅  All Day 6 tasks completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
