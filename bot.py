import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ─────────────────────────────────────────
#  Настройки
# ─────────────────────────────────────────
TOKEN = "ВАШ_ТОКЕН_СЮДА"  # Вставьте токен от @BotFather

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

CONTACT_LINK = "https://t.me/ВАШ_ЮЗЕРНЕЙМ"  # Замените на ваш контакт/группу


# ─────────────────────────────────────────
#  Главное меню
# ─────────────────────────────────────────
def main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        # Большая кнопка — занимает всю строку
        [
            InlineKeyboardButton(
                "🚀 Заказать бота", callback_data="order_bot"
            )
        ],
        # Три маленькие кнопки
        [
            InlineKeyboardButton("🤖 Виды ботов", callback_data="bot_types"),
        ],
        [
            InlineKeyboardButton(
                "💡 Как работают ИИ-Консультанты", callback_data="how_ai_works"
            ),
        ],
        [
            InlineKeyboardButton(
                "📈 Как это поможет вашему бизнесу?", callback_data="business_help"
            ),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


WELCOME_TEXT = (
    "👋 *Добро пожаловать в Voithos!*\n\n"
    "Мы разрабатываем Telegram-ботов и ИИ-консультантов для бизнеса.\n\n"
    "Выберите интересующий вас раздел 👇"
)


# ─────────────────────────────────────────
#  Команда /start
# ─────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )


# ─────────────────────────────────────────
#  Команда /menu — показать главное меню
# ─────────────────────────────────────────
async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(),
    )


# ─────────────────────────────────────────
#  Обработчик кнопок
# ─────────────────────────────────────────
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # убираем «часики» у кнопки

    data = query.data

    # ── Кнопка «Назад» — возвращает главное меню ──────────────────────────
    if data == "back_to_menu":
        await query.edit_message_text(
            text=WELCOME_TEXT,
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard(),
        )
        return

    back_button = [[InlineKeyboardButton("⬅️ Назад в меню", callback_data="back_to_menu")]]

    # ── Заказать бота ─────────────────────────────────────────────────────
    if data == "order_bot":
        text = (
            "📩 *Заказать бота*\n\n"
            "Мы готовы разработать бота под любую задачу вашего бизнеса!\n\n"
            "Свяжитесь с нами — расскажите о своей идее, "
            "и мы предложим оптимальное решение.\n\n"
            f"👉 [Написать нам]({CONTACT_LINK})"
        )
        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button),
            disable_web_page_preview=True,
        )

    # ── Виды возможных ботов ──────────────────────────────────────────────
    elif data == "bot_types":
        text = (
            "🤖 *Виды ботов, которые мы разрабатываем*\n\n"
            "• *ИИ-консультант* — отвечает на вопросы клиентов 24/7\n"
            "• *Бот для записи* — принимает заявки и бронирования\n"
            "• *Интернет-магазин* — продаёт товары прямо в Telegram\n"
            "• *CRM-бот* — управляет клиентской базой\n"
            "• *Рассылки и уведомления* — держит клиентов в курсе\n"
            "• *Бот для HR* — автоматизирует найм и онбординг\n\n"
            "_Нет нужного? Мы разработаем под ваши задачи!_"
        )
        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button),
        )

    # ── Как работают ИИ-консультанты ─────────────────────────────────────
    elif data == "how_ai_works":
        text = (
            "💡 *Как работают ИИ-Консультанты?*\n\n"
            "1️⃣ *Обучение на вашей базе знаний*\n"
            "   Загружаем информацию о вашем бизнесе, товарах и услугах.\n\n"
            "2️⃣ *Понимание естественного языка*\n"
            "   Клиент пишет свободным текстом — бот понимает суть вопроса.\n\n"
            "3️⃣ *Мгновенные ответы*\n"
            "   Бот отвечает за секунды, без ожидания оператора.\n\n"
            "4️⃣ *Передача сложных вопросов менеджеру*\n"
            "   Если бот не знает ответа — он уведомит живого сотрудника.\n\n"
            "5️⃣ *Постоянное улучшение*\n"
            "   Бот учится на новых вопросах и становится умнее."
        )
        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button),
        )

    # ── Как это может помочь бизнесу ─────────────────────────────────────
    elif data == "business_help":
        text = (
            "📈 *Как это поможет вашему бизнесу?*\n\n"
            "✅ *Экономия времени* — бот обрабатывает сотни запросов одновременно\n\n"
            "✅ *Снижение затрат* — меньше операторов на рутинных задачах\n\n"
            "✅ *Работа 24/7* — клиенты получают ответы в любое время\n\n"
            "✅ *Рост конверсии* — мгновенный отклик удерживает клиента\n\n"
            "✅ *Сбор данных* — аналитика по вопросам и поведению клиентов\n\n"
            "✅ *Масштабируемость* — бот справляется с любым объёмом запросов\n\n"
            "_Средний ROI от внедрения бота — окупаемость за 1–3 месяца._"
        )
        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button),
        )


# ─────────────────────────────────────────
#  Обработчик любого текста (не команды)
# ─────────────────────────────────────────
async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Воспользуйтесь меню ниже 👇",
        reply_markup=main_menu_keyboard(),
    )


# ─────────────────────────────────────────
#  Запуск
# ─────────────────────────────────────────
def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    logger.info("Voithos Bot запущен ✅")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
