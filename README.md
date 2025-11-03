# Hexlet Code – Генератор различий (Gendiff)


[![hexlet-check](https://github.com/Cybertourist/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cybertourist/python-project-50/actions/workflows/hexlet-check.yml)
[![GitHub Actions](https://github.com/Cybertourist/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/Cybertourist/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Cybertourist_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Cybertourist_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Cybertourist_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Cybertourist_python-project-50)

---

## Описание

**Gendiff** — утилита для сравнения двух конфигурационных файлов (JSON и YAML) и отображения различий между ними.  
Поддерживает несколько форматов вывода:

- **Stylish** (по умолчанию) — древовидное отображение;
- **Plain** — текстовый вывод с описанием изменений;
- **JSON** — структурированный вывод в формате JSON.

---

## Установка и запуск

```bash
# Установка зависимостей и проекта
make install

# Запуск утилиты
gendiff file1.json file2.json

# Пример выбора формата
gendiff --format plain file1.yml file2.yml
gendiff --format json file1.json file2.json
```

---

## Демонстрации работы

### 1. Вызов справки
[![Справка](https://asciinema.org/a/FTsYPXHMj4ofmyQeLK5NZDCx.svg)](https://asciinema.org/a/FTsYPXHMj4ofmyQeLK5NZDCx)  
Показывает список доступных аргументов и опций утилиты.

### 2. Сравнение простых файлов (JSON)
[![JSON](https://asciinema.org/a/sFsQJK9FKZ7YZGakmKthDxzfM.svg)](https://asciinema.org/a/sFsQJK9FKZ7YZGakmKthDxzfM)  
Отображает различия между двумя простыми JSON-файлами.

### 3. Поддержка формата YAML
[![YAML](https://asciinema.org/a/X2bHObVyWBPjRBzw6KW0aMMPM.svg)](https://asciinema.org/a/X2bHObVyWBPjRBzw6KW0aMMPM)  
Утилита корректно парсит и сравнивает YAML-файлы.

### 4. Древовидный вывод (Stylish)
[![Stylish](https://asciinema.org/a/6nKU5kmnt6pL119k86Kyz45ys.svg)](https://asciinema.org/a/6nKU5kmnt6pL119k86Kyz45ys)  
Выводит разницу в виде красивого вложенного дерева (формат по умолчанию).

### 5. Плоский вывод (Plain)
[![Plain](https://asciinema.org/a/3XUUIBZZUTqBE6EwpcQdPY3Hu.svg)](https://asciinema.org/a/3XUUIBZZUTqBE6EwpcQdPY3Hu)  
Показывает разницу в виде списка изменений с полным путем к свойству.

### 6. Вывод в формате JSON
[![JSON output](https://asciinema.org/a/t6ccHlj9tgcMzQsXHndVE5c5J.svg)](https://asciinema.org/a/t6ccHlj9tgcMzQsXHndVE5c5J)  
Структурированный вывод в формате JSON для интеграции с другими программами.

---

## Тестирование

```bash
# Запуск всех тестов
pytest

# Запуск линтера
make lint
```

---

## Пример использования в коде

```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json', format_name='plain')
print(diff)
```

---
