# UI Course Automation Tests

This project implements automated tests for
the [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login). The
tests are written using **Python**, **Pytest**, **Allure** and **Playwright**. The test application’s source code is available
on [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Project Overview

The goal of this project is to automate the testing of the UI Course application. The automated tests verify various
functionalities of the application to ensure its stability and correctness. The project structure follows best practices
for organizing test code with clear, maintainable scripts.

## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/DorianQA-WEB/autotests-ui.git
cd autotests-ui
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Additional Playwright Setup (if needed)

If you're running Playwright for the first time, you might need to install the required browsers:

```bash
playwright install
```

### Running the Tests with Allure Report Generation

To run the tests and generate an Allure report, use the following command:

```bash
pytest -m "regression" --alluredir=./allure-results
```

This will execute all tests in the project and display the results in the terminal.

### Viewing the Allure Report

After the tests have been executed, you can generate and view the Allure report with:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser.


# Автоматизированные тесты для UI Course

Этот проект реализует автоматизированные тесты для:
[учебного приложения UI Course](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login).
Тесты написаны с использованием **Python**, **Pytest**, **Allure** и **Playwright**.
Исходный код тестового приложения доступен на [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Обзор проекта

Цель проекта — автоматизировать тестирование приложения UI Course. Автоматизированные тесты проверяют различные функции приложения, чтобы обеспечить его стабильность и корректность. Структура проекта соответствует лучшим практикам организации тестового кода: чёткая, удобная в сопровождении и масштабируемая.

## Начало работы

### Клонирование репозитория

Чтобы начать, склонируйте репозиторий проекта с помощью Git:
```bash
git clone https://github.com/DorianQA-WEB/autotests-ui.git
cd autotests-ui
```


### Создание виртуального окружения

Рекомендуется использовать виртуальное окружение для управления зависимостями проекта. Выполните команды в зависимости от вашей операционной системы:

#### Linux / MacOS

```bash
python3 -m venv venv source venv/bin/activate
```

#### Windows

```bash
python -m venv venv venv\Scripts\activate
```

### Установка зависимостей

После активации виртуального окружения установите зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Дополнительная настройка Playwright (при необходимости)

Если вы используете Playwright впервые, возможно, потребуется установить необходимые браузеры:

```bash
playwright install
```

### Запуск тестов с генерацией отчёта Allure

Чтобы запустить тесты и сгенерировать отчёт в Allure, выполните команду:

```bash
pytest -m "regression" --alluredir=./allure-results
```

Это запустит все тесты проекта и выведет результаты в терминал.

### Просмотр отчёта Allure

После выполнения тестов вы можете сгенерировать и открыть отчёт Allure:

```bash
allure serve allure-results
```
w
Эта команда откроет отчёт Allure в вашем браузере по умолчанию.