# python_intro_materials

## Guide to Python in textual form

- [Initial Guide and Install](DOCS/INITIAL_GUIDE_AND_INSTALL.md)
- [Python Applications](DOCS/Python_applications.md)
- [Project Structure and Modules](DOCS/project_structure.md)
- [Working with Jupyter Notebooks](DOCS/ipynb.md)
- [Growth Areas: Where to Go Next](DOCS/extra.md)

## textstats: Практический пример

[textstats](DOCS/textstats_readme.md) — это небольшой демонстрационный пакет, который показывает реальные концепции упаковки Python. Это утилита для анализа текста, которая:

- Считает количество слов и символов в тексте
- Определяет самые частые слова
- Оценивает время чтения на основе скорости чтения (слов в минуту)

Этот проект служит практическим введением в:
- Создание Python пакетов с правильной структурой
- Использование `pyproject.toml` для современной конфигурации пакетов
- Установку локальных пакетов через `pip install -e .`
- Модульную организацию кода (разделение логики на `basic.py` и `io_utils.py`)
- Использование пакетов в Jupyter Notebooks

Идеально для понимания того, как работают Python пакеты изнутри!

