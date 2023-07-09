from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os, time

# import algorithms as algos

# moving_average_signal = algos.price_actions.main.moving_average()

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def watch(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    while True:
        await update.message.reply_text(f"Watching")
        time.sleep(2)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("watch", watch))

# Update.message.reply_text(f"Hello {Update.effective_user.first_name}")

app.run_polling()
