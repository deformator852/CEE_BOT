# Початок роботи:

Переконайтеся, що у вас встановлено Python на вашому комп'ютері. Додатково встановіть необхідні бібліотеки за допомогою pip:
pip3 install aiogram

# Налаштування:

Отримайте токен бота Telegram від BotFather на платформі Telegram.
Як отримати токен:https://gerabot.com/article/yak_otrimati_token_telegram_ta_stvoriti_bota

Після отримання токену відкрийте файл create_bot.py та в поле "TOKEN" введіть токен який ви отримали від BotFather

Щоб запустити бота введіть команду python3 main.py &

# Інструкція для того щоб бот сам себе підіймав після перезавантаження:
Створіть файл з розширенням .service, наприклад, bot.service:
/etc/systemd/system/bot.service
[Unit]
Description=My Telegram Bot

[Service]
Type=simple
ExecStart=/usr/bin/python3 /повний/шлях/до/вашого/файлу/main.py
Restart=always
RestartSec=5
User=ваш_користувач
WorkingDirectory=/повний/шлях/до/вашого/файлу/

[Install]
WantedBy=multi-user.target

Після створення файлу служби використайте наступні команди для оновлення конфігурації:

sudo systemctl daemon-reload

Запуск та активація служби:

sudo systemctl start bot
sudo systemctl enable bot

Тепер ваш бот буде запускатися автоматично при перезавантаженні сервера.

Перевірка стану служби:

sudo systemctl status bot
