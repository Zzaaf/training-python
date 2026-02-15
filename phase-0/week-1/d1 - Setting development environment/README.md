# Настройка среды разработки на Python

Краткое руководство по установке инструментов и базовым командам.

---

## 1. Установка инструментов

### Python

- **Windows:** скачать установщик с [python.org](https://www.python.org/downloads/). При установке включить опцию **Add Python to PATH**.
- **macOS:** `brew install python` или установщик с python.org.
- **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install python3 python3-pip`

Проверка:
```bash
python --version
# или
python3 --version
pip --version
```

### Git

- **Windows:** [git-scm.com](https://git-scm.com/download/win) — установщик, далее следовать шагам (по умолчанию достаточно).
- **macOS:** `brew install git`
- **Linux:** `sudo apt install git`

Проверка:
```bash
git --version
```

### Docker

- **Windows/macOS:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) — скачать и установить.
- **Linux (Ubuntu):**
  ```bash
  sudo apt update && sudo apt install docker.io docker-compose
  sudo usermod -aG docker $USER
  ```
  После этого выйти из сессии и зайти снова.

Проверка:
```bash
docker --version
docker run hello-world
```

### VSCode

- Скачать с [code.visualstudio.com](https://code.visualstudio.com/).
- Рекомендуемые расширения: **Python**, **Jupyter**, **Pylance**, **GitLens**.

---

## 2. Базовые команды Git

| Действие | Команда | Пример |
|----------|---------|--------|
| Инициализация репозитория | `git init` | `git init` |
| Добавить файлы в индекс | `git add <файл\|.>` | `git add .` или `git add main.py` |
| Создать коммит | `git commit -m "сообщение"` | `git commit -m "Add main script"` |
| Отправить в удалённый репозиторий | `git push [remote] [branch]` | `git push origin main` |
| Создать ветку | `git branch <имя>` | `git branch feature-auth` |
| Показать ветки | `git branch` | `git branch -a` (все, включая remote) |
| История коммитов | `git log` | `git log --oneline -10` |
| Переключиться на ветку/коммит | `git checkout <ветка\|хеш>` | `git checkout main` |
| Временно спрятать изменения | `git stash` | `git stash` или `git stash push -m "WIP"` |
| Вернуть из stash | — | `git stash pop` или `git stash list` |

Типичный цикл:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <url>
git push -u origin main
```

---

## 3. Файлы .ipynb (Jupyter Notebook)

**Формат:** JSON-файл с ячейками двух типов — **code** и **markdown**. В каждой ячейке хранится исходный код или текст, а также вывод (output).

### Использование в VSCode

1. Установить расширения **Python** и **Jupyter**.
2. Открыть `.ipynb` — откроется интерфейс с ячейками.
3. Запуск ячейки: `Shift+Enter` (выполнить и перейти к следующей) или кнопка ▶.
4. Создать новый notebook: Command Palette (`Ctrl+Shift+P`) → **Jupyter: Create New Jupyter Notebook**.

### Использование в JupyterLab

1. Установка: `pip install jupyterlab`
2. Запуск: `jupyter lab` — откроется в браузере.
3. File → New → Notebook, выбрать ядро (например, Python 3).
4. Ячейки: Code / Markdown; запуск — `Shift+Enter`.

### Полезные сочетания (Jupyter / VSCode)

- `Shift+Enter` — выполнить ячейку
- `Ctrl+Enter` — выполнить ячейку (остаться на ней)
- `A` / `B` — новая ячейка выше/ниже (в JupyterLab)
- `M` / `Y` — переключить ячейку в Markdown / Code

---

## 4. Базовые команды терминала

| Команда | Назначение | Примеры |
|---------|------------|---------|
| `cd` | Сменить каталог | `cd project`, `cd ..`, `cd ~` |
| `touch` | Создать пустой файл (или обновить время) | `touch readme.md`, `touch a.txt b.txt` |
| `mkdir` | Создать каталог | `mkdir docs`, `mkdir -p a/b/c` |
| `ls` | Список файлов и папок | `ls`, `ls -la`, `ls -lt` |
| `rm` | Удалить файл/каталог | `rm file.txt`, `rm -r dir`, `rm -rf dir` |
| `mv` | Переименовать или переместить | `mv old.txt new.txt`, `mv file.txt backup/` |
| `cp` | Копировать | `cp a.txt b.txt`, `cp -r src/ dest/` |

### Частые флаги

- **ls:** `-l` (длинный список), `-a` (включая скрытые), `-t` (по времени), `-h` (человекочитаемые размеры).
  ```bash
  ls -la
  ls -lth
  ```
- **mkdir:** `-p` — создать вложенные каталоги, не ругаться если часть пути уже есть.
  ```bash
  mkdir -p phase-0/week-1/notes
  ```
- **rm:** `-r` (рекурсивно, для каталогов), `-f` (не спрашивать подтверждение). Осторожно с `rm -rf`.
  ```bash
  rm -r old_folder
  rm -f log.txt
  ```
- **cp:** `-r` — копировать каталог рекурсивно.
  ```bash
  cp -r my_project my_project_backup
  ```
- **mv:** флаги редко нужны; для перезаписи иногда используется `-f` (force).

---

*Краткая шпаргалка — для деталей смотри официальную документацию каждого инструмента.*
