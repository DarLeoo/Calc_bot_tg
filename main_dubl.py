import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
from ui_telegram import auto_in
from save_log import save_logs

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот калькулятор нажми /f выражение или /help")


async def hi(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Привет {update.effective_user.first_name}')


async def help(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="\
пример ввода комплексных /f (-5i)+(5+7i) => 5+2i;   /f (8-8i)*(-5+2i) => -40+16i \n\
пример ввода целых /f -5+9 => 4 \n\
пример ввода рациональных /f -5/6*9/7 => -15/14 \n\
пример объема  /f 0.02*0.01*5 => 0.001 куб. м. или 1.0 литров \n\
пример перевода в двоичную cистему /f 254 => 11111110")

async def c(update: Update, context: CallbackContext.DEFAULT_TYPE):
    msg = update.message.text.replace("/f", '')
    msg = str(auto_in(msg))
    ms_txt = ({update.effective_user.first_name}, {update.message.text}, msg)
    save_logs(str(ms_txt))
    print(msg)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{msg}')

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()

    start_handler = CommandHandler('start', start)
    like_handler = CommandHandler('like', like)
    hi_handler = CommandHandler('hi', hi)
    help_handler = CommandHandler('help', help)
    c_handler = CommandHandler('f', c)

    application.add_handler(start_handler)
    application.add_handler(like_handler)
    application.add_handler(hi_handler)
    application.add_handler(help_handler)
    application.add_handler(c_handler)

    application.run_polling()



