# UI language tests (Selenium + PyTest)

Автотест для проверки наличия кнопки "Добавить в корзину" на странице товара.

## Установка и запуск

pip install -r requirements.txt
pytest --language=es -v

Для проверки французского языка (кнопка должна быть "Ajouter au panier"):
1. В `test_items.py` раскомментируйте `time.sleep(30)`.
2. Запустите

pytest --language=fr -v
```
