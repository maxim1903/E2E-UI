# E2E и API тестирование

Этот проект содержит автоматизированные тесты для проверки функциональности веб-сайта saucedemo.com.

## Структура проекта

- `tests/` - содержит тесты для e2e UI и API.
  - `test_purchase_flow.py` - тестовый сценарий покупки товара на сайте saucedemo.com.
  - `test_github_api.py` - тесты для GitHub API.

- `pages/` - содержит классы для страниц, используемых в тестах.
  - `login_page.py` - страница авторизации на сайте saucedemo.com.
  - `product_page.py` - страница выбора товара.
  - `cart_page.py` - страница корзины.
  - `checkout_page.py` - страница оформления заказа.
  - `checkout_complete_page.py` - страница завершения заказа.

- `.env` - файл с переменными окружения для конфигурации GitHub API.
- `requirements.txt` - файл с зависимостями проекта.
- `README.md` - инструкция по установке и запуску тестов.

## Установка зависимостей

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/maxim1903/E2E-UI.git
    cd e2e-saucedemo-test

    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск тестов

### E2E тесты для saucedemo.com

1. Убедитесь, что ChromeDriver установлен и доступен в PATH.

2. Запустите тесты:

    ```
    pytest tests/test_purchase_flow.py
    ```

## Примечания

- Убедитесь, что вы используете совместимую версию Python (Python 3.11.x рекомендуется).
