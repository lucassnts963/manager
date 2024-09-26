import telebot

class TelegramAssistantBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.setup_handlers()

    def setup_handlers(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.bot.reply_to(message, "Olá! Eu sou seu assistente.")

        # Outros handlers e comandos

    def start(self):
        print("Bot rodando...")
        self.bot.infinity_polling()

# Inicializando o bot
if __name__ == "__main__":
    from config import API_TOKEN
    bot = TelegramAssistantBot(API_TOKEN)
    bot.start()