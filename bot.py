import telebot

API_TOKEN = '5671558124:AAFa4zJQDAfcP02L4wCUKGWl4vZgKxg6nAg'

bot = telebot.TeleBot(API_TOKEN)
    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# command /se_emitir_boleto ↓↓↓↓↓↓↓
@bot.message_handler(commands=['se_emitir_boleto'])
def cliente1(message):
    texto = "aqui você consegue verificar se emite o boleto ou não!!"
    bot.reply_to(message, "TESTE: {}".format(texto))

# command /verificar_saldo ↓↓↓↓↓↓↓
@bot.message_handler(commands=['verificar_saldo'])
def cliente1(message):
    texto = "aqui você consegue verificar o saldo do cliente!!"
    bot.reply_to(message, texto)

# command cliente_1 ↓↓↓↓↓↓↓
@bot.message_handler(commands=['cliente_1'])
def cliente1(message):
    texto = "Você deseja saber /se_emitir_boleto ? ou /verificar_saldo ? \n \n *** Digite ou clique em uma das opções! ***"
    bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

@bot.message_handler(func=lambda message: True)
def initial_menssage(message):
    texto = """
            Escolha uma opção para continuar (clique no item):

            /cliente_1 - Baby Fashion & Fun

            /cliente_2 - BeniShop

            /cliente_3 - Casa Campos

            /cliente_4 - FDTE [Indisponível]

            /cliente_5 - Jornada do Consultor

            /cliente_6 - Loretto Distribuidor

            /cliente_7 - Mega Safe

            /cliente_8 - Minas Banheiras

            /cliente_9 - Minas Banheiras (Mercado Shops)

            /cliente_10 - Missinclof

            /cliente_11 - Motta

            /cliente_12 - Nutrição Total

            /cliente_13 - SPS Energy

            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                *** Os itens com "[Indisponível]" 
                não tem campanha rodando ***
            -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

            Desenvolvido por: Victor Rodrigues
            """
    bot.reply_to(message,texto)
bot.infinity_polling()
