# Stripe Shop

Этот проект - интернет-магазин с интеграцией платежной системы Stripe.

## Возможности
- Просмотр списка товаров
- Покупка товара через Stripe

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Mityashka/Stripe-Shop
   cd Stripe-Shop
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Примените миграции:
   ```bash
   python manage.py migrate
   ```
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

## Пути (URL-ы) в проекте

### Основные пути:
- `/shopapp/` - - Главная страница магазина(index)
### Пути в `shopapp.urls`:
- `/item/<int:pk>/` - Детальная информация о товаре
- `/buy/<int:pk>/` - Покупка товара через Stripe
- `/success/` - Страница успешной оплаты
- `/cancel/` - Страница отмененной оплаты

### Админка Django:
- `/admin/` - Панель администратора Django
- Логин - admin1
- Пароль - admin1


