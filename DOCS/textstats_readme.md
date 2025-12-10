# textstats

A tiny demo package for teaching Python packaging.

Example:

```python
from textstats import word_count, top_words
text = "Hello world, hello Python"
print(word_count(text))
print(top_words(text))
```

Nice, this is exactly the kind of thing that makes “Python basics” feel real, not abstract.

Here’s a concrete mini-project that works great for:

* showing **modules и пакеты**,
* **установку через pip** (локальный пакет),
* использование **в Jupyter как внешней библиотеки**.

---

## Idea: tiny `textstats` package

Task:
Сделать маленькую библиотеку `textstats`, которая:

* считает количество слов и символов;
* даёт топ наиболее частых слов;
* оценивает примерное “время чтения” текста (например, при 200 слов/мин).

Потом ставим её в окружение и показываем, как в ноутбуке сделать:

```python
from textstats import basic

text = "Some sample text ..."
basic.word_count(text)
basic.top_words(text, n=5)
basic.estimate_reading_time(text, wpm=200)
```

### 1. Проектная структура

Минимальный вариант:

```text
textstats-demo/
    textstats/
        __init__.py
        basic.py
        io_utils.py
    pyproject.toml
    README.md
```

Где:

* `textstats/` — пакет;
* `basic.py` — основная логика;
* `io_utils.py` — загрузка текста из файлов (показать модули);
* `pyproject.toml` — чтобы `pip install -e .` работало как у взрослых.

---

### 2. Код пакета

`textstats/__init__.py`:
Main entry point for the package. Exports the public API so users can import functions directly from `textstats` without needing to know about internal module structure. Makes functions like `word_count`, `top_words`, etc. available at the package level.

`textstats/basic.py`:
Core functionality for text analysis. Contains the main functions:
- `word_count(text)` — counts the number of words in text
- `char_count(text, with_spaces=True)` — counts characters with optional space exclusion
- `top_words(text, n=5)` — returns the most frequent words and their counts
- `estimate_reading_time(text, wpm=200)` — estimates how long it takes to read text based on words per minute

`textstats/io_utils.py`:
File input/output utilities. Handles reading text from files and other I/O operations:
- `read_text_file(filepath)` — reads a text file and returns its content
- Helper functions for working with external text sources
Separates I/O concerns from the core text analysis logic, making the code more modular and testable.

### 3. Минимальный `pyproject.toml`

Чтобы показать “это *реальный* пакет”, даём современный, но минимальный конфиг:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "textstats"
version = "0.1.0"
description = "Tiny text statistics helper for demo purposes"
authors = [{ name = "Mikhail", email = "you@example.com" }]
readme = "README.md"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest"]
```

Этого достаточно, чтобы:

```bash
python -m venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows

pip install -e .
```

После этого `textstats` становится “внешней библиотекой” в этом окружении.

---

### 4. Демонстрация в Jupyter Notebook

В ноутбуке (с тем же активированным venv):

```python
from textstats import word_count, char_count, top_words, estimate_reading_time
from textstats.io_utils import read_text_file

sample = """
Python is an interpreted, high-level programming language.
Python is great for teaching and rapid prototyping.
"""

word_count(sample)
```

```python
char_count(sample, with_spaces=False)
```

```python
top_words(sample, n=5)
```

```python
estimate_reading_time(sample, wpm=200)
```

```python
text = read_text_file("some_article.txt")
print("Words:", word_count(text))
print("Top 10:", top_words(text, n=10))
print("Estimated reading time (min):", round(estimate_reading_time(text), 2))
```

Тут наглядно видно:

* импорт из **собственного пакета** (как будто это `numpy`);
* чистое разделение логики (`basic.py`) и I/O (`io_utils.py`);
* использование всего этого в интерактивном режиме.

