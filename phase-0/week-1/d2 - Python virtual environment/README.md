# Виртуальное окружение Python

Краткое руководство по настройке venv, работе с pip и связанным инструментам.

---

## 1. Зачем нужно виртуальное окружение

- **Изоляция зависимостей** — пакеты проекта не смешиваются с системным Python и другими проектами.
- **Воспроизводимость** — на другой машине можно установить те же версии по `requirements.txt`.
- **Безопасность** — не требуется `sudo` для установки пакетов.

### Файл requirements.txt

Список зависимостей проекта. Используется для установки окружения «одной командой» и для фиксации версий.

| Действие | Команда |
|----------|---------|
| Сохранить установленные пакеты в файл | `pip freeze > requirements.txt` |
| Установить все из файла | `pip install -r requirements.txt` |

Пример содержимого:
```
requests==2.31.0
beautifulsoup4==4.12.2
```

---

## 2. Создание и активация окружения (.venv)

### Варианты папки для окружения

Обычно используют папку **`.venv`** в корне проекта (скрытая, по соглашению не коммитится). Альтернативы: `venv`, `env` — принцип тот же.

### Windows

```bash
# Создать окружение в папке .venv
python -m venv .venv

# Активация (PowerShell)
.venv\Scripts\Activate.ps1

# Активация (CMD)
.venv\Scripts\activate.bat
```

После активации в начале строки появится `(.venv)`.

### Linux / macOS

```bash
# Создать окружение
python3 -m venv .venv

# Активация (bash/zsh)
source .venv/bin/activate
```

### Деактивация (все ОС)

```bash
deactivate
```

### Типичный цикл

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1          # Windows PowerShell
# source .venv/bin/activate         # Linux/macOS
pip install -r requirements.txt
# работа в проекте
pip freeze > requirements.txt       # обновить список после изменений
```

---

## 3. Базовые команды pip

| Действие | Команда | Пример |
|----------|---------|--------|
| Установить пакет | `pip install <пакет>` | `pip install requests` |
| Установить версию | `pip install <пакет>==<версия>` | `pip install django==4.2` |
| Удалить пакет | `pip uninstall <пакет>` | `pip uninstall flask` |
| Список установленных | `pip list` | `pip list` |
| Информация о пакете | `pip show <пакет>` | `pip show requests` |
| Обновить pip | `python -m pip install --upgrade pip` | — |

**Важно:** выполняйте `pip install` только при **активированном** виртуальном окружении, чтобы пакеты ставились в `.venv`, а не в систему.

---

## 4. Популярные пакеты (top-5 по pip)

| Пакет | Установка | Импорт | Назначение |
|-------|-----------|--------|------------|
| requests | `pip install requests` | `import requests` | HTTP-запросы |
| django | `pip install django` | `import django` | Веб-фреймворк |
| flask | `pip install flask` | `import flask` | Микро-веб-фреймворк |
| numpy | `pip install numpy` | `import numpy` | Численные вычисления |
| beautifulsoup4 | `pip install beautifulsoup4` | `from bs4 import BeautifulSoup` | Парсинг HTML/XML |

### Частая ошибка: имя пакета ≠ имя при импорте

В коде пишут `from bs4 import BeautifulSoup`, но в PyPI пакет называется **beautifulsoup4**. Если поставить `pip install bs4`, получите другой (устаревший/пустой) пакет. Всегда ставьте:

```bash
pip install beautifulsoup4
```

Аналогично: `pip install pillow` (импорт: `from PIL import Image`), `pip install scikit-learn` (импорт: `import sklearn`).

---

## 5. Инструменты для работы с окружением

### uv

Быстрый менеджер пакетов и окружений от Astral (создатели ruff). Может создавать venv и ставить пакеты без классического pip.

```bash
# Установка (Windows PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Установка (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Создать .venv и установить зависимости из requirements.txt
uv venv
uv pip install -r requirements.txt
# или: uv sync  (если есть pyproject.toml)
```

### Conda

Менеджер окружений и пакетов (часто для данных и ML). Окружения живут отдельно от папки проекта, управляются через `conda`.

```bash
# Создать окружение с версией Python
conda create -n myenv python=3.11

# Активация
conda activate myenv   # Windows/Linux/macOS одинаково

# Установка пакетов
conda install numpy pandas
# или через pip внутри окружения: pip install -r requirements.txt

# Деактивация
conda deactivate
```

Для обычной разработки часто достаточно **venv + pip**; **uv** — если нужна скорость; **conda** — если проект завязан на conda-пакеты или несколько версий Python.

---

## 6. .gitignore для Python-проекта

Чтобы не коммитить виртуальное окружение и служебные файлы, добавьте в репозиторий `.gitignore`:

```bash
# Создать файл .gitignore с типичными правилами для Python
echo ".venv/
venv/
env/
__pycache__/
*.py[cod]
*.egg-info/
.eggs/
dist/
build/
.pytest_cache/
.coverage
htmlcov/
*.egg
.env
.env.local" > .gitignore
```

Или вручную создайте файл `.gitignore` в корне проекта и вставьте в него эти строки. После этого:

```bash
git add .gitignore
git commit -m "Add Python .gitignore"
```

---

*Краткая шпаргалка — для деталей смотри документацию [pip](https://pip.pypa.io/), [venv](https://docs.python.org/3/library/venv.html), [uv](https://docs.astral.sh/uv/), [conda](https://docs.conda.io/).*
