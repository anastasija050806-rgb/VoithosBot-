# VoithosBot

Telegram-бот для компании **Voithos** — маркетинговый инструмент для представления услуг разработки ботов и ИИ-консультантов.

## 🚀 Возможности

- 🤖 Информация о типах ботов
- 💡 Описание как работают ИИ-консультанты
- 📈 Преимущества для бизнеса
- 📩 Форма для заказа бота
- ⬅️ Удобная навигация по меню

## 📋 Требования

- Python 3.8+
- Telegram Bot Token (получить от [@BotFather](https://t.me/botfather))

## 🔧 Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/ilashofficial17-cmd/voithosbot.git
   cd voithosbot
   ```

2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл `.env`:**
   ```bash
   cp .env.example .env
   ```

5. **Заполните `.env` вашими данными:**
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   CONTACT_LINK=https://t.me/your_username
   ```

## ▶️ Запуск

```bash
python bot.py
```

Бот начнет работать и слушать обновления от Telegram API.

## 📂 Структура файлов

```
voithosbot/
├── bot.py              # Основной код бота
├── requirements.txt    # Python зависимости
├── Procfile           # Конфиг для развертывания (Heroku)
├── .env.example       # Пример конфигурации
├── .gitignore         # Файлы для игнорирования Git
└── README.md          # Этот файл
```

## 🌐 Развертывание на Heroku

1. Создайте приложение на Heroku
2. Добавьте переменные окружения в Settings:
   - `TELEGRAM_BOT_TOKEN`
   - `CONTACT_LINK`
3. Разверните код:
   ```bash
   git push heroku main
   ```

## 📝 Лицензия

Проект Voithos © 2025

## 📧 Контакты

Свяжитесь с нами через Telegram: [@voithos](https://t.me/voithos)
