# Autocorrect System

A simple Python-based autocorrect system using Levenshtein distance to suggest corrections for misspelled words.

---

## Features
- Checks if a word is spelled correctly
- Suggests top 5 closest matches if the word is misspelled
- Easy to use and extend

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Manolis8/autocorrect-system.git
cd autocorrect-system
```

Install dependencies:

pip install python-Levenshtein

Usage

Run the program:

python autocorrect.py


Then type words to check their spelling. Type exit to quit.

Files

autocorrect.py: Main Python script for autocorrect functionality

nltk_words.csv: List of valid words used for spell checking

README.md: This documentation

Example
Enter a word (or type 'exit' to quit): appl
'appl' is not spelled correctly. Did you mean: apple, apply, app, ample, April?
