
# Учебный калькулятор

Учебный проект для практических работ.

## Состав

- `utils.py` - арифметические функции: add, sub, mul, div, neg, sqr, power
- `main.py` - пример использования функций
- `test_*.py` - модульные тесты (unittest)

## Запуск

    python main.py
    python -m unittest discover -p "test_*.py"

## Документация

API-документация генерируется автоматически из docstring функций
с помощью pdoc при каждом изменении кода в ветви main
и публикуется на GitHub Pages.
