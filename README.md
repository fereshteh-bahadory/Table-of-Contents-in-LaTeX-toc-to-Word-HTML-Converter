# -In progress
# Table-of-Contents-in-LaTeX-toc-to-Word-HTML-Converter

A lightweight, pure Python script designed to parse and convert LaTeX Table of Contents (`.toc`) files into a perfectly formatted, aligned layout. The output is generated as an HTML/Word-ready file, making it incredibly easy to copy and paste or import directly into **Microsoft Word** without losing text structure, mathematical formulas, or indentation.

---

## Key Features

* **Zero Dependencies:** Built entirely using Python's native modules (no external libraries like `pandas` or `beautifulsoup` required).
* **Smart Section Demultiplexing:** Automatically detects and handles the structural differences between numbered sections and starred/unnumbered sections (`section*`, `chapter*`) to extract titles and page numbers flawlessly.
* **Mathematical Formula Preservation:** Uses regex logic to isolate LaTeX math environments (text wrapped in `$`) so they maintain their original formatting and inline directionality.
* **Structured Indentation:** Implements a strict hierarchical cascading indentation system for sub-levels (`subsection` and `subsubsection`).
* **Zero-Width Non-Joiner (ZWNJ) Support:** Automatically replaces Unicode escape characters like `\u200c` with the actual invisible character (`chr(8204)`) to perfectly render Persian semi-spaces (نیم‌فاصله).

---

## Code Logic & Indentation Priority

To prevent keyword collision (e.g., matching `section` inside `subsection`), the script evaluates the LaTeX layout block in a reversed hierarchical order:

1. `subsubsection` ➔ 3rd level indentation (deepest nested block)
2. `subsection` ➔ 2nd level indentation
3. `section` ➔ 1st level indentation
4. `chapter` / `section*` / `chapter*` ➔ 0 level indentation (flushed to the margin)

---

## How to Use

### 1. Configuration
Open the Python script (or Jupyter Notebook cell) and update the input/output file paths to match your local directory setup:

```python
input_file_path = r"C:/path/to/your/main.toc"
output_file_path = r"C:/path/to/your/content_list_pr.html (or content_list_en.html)"
