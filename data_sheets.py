from __future__ import print_function
from updatedb import updatedb
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# updatedb()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SAMPLE_SPREADSHEET_ID = '1pc5zRc73gT-Xz02ikBbdh2ftVIcVrffeK2ELKWwD4-0'
SAMPLE_RANGE_NAME = 'Página1!A2:F'


def main():

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()

        
        valores = result['values']
        valores = sorted(valores)

        values = result.get('values', [])
        if not values:
            print('No data found.')
            return
    except HttpError as err:
        print(err)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente1_nome = valores[0][0]
    cliente1_gasto_diario = valores[0][1]
    cliente1_saldo_atual = valores[0][2]
    cliente1_emitir_boleto = valores[0][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente2_nome = valores[1][0]
    cliente2_gasto_diario = valores[1][1]
    cliente2_saldo_atual = valores[1][2]
    cliente2_emitir_boleto = valores[1][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente3_nome = valores[2][0]
    cliente3_gasto_diario = valores[2][1]
    cliente3_saldo_atual = valores[2][2]
    cliente3_emitir_boleto = valores[2][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente4_nome = valores[3][0]
    cliente4_gasto_diario = valores[3][1]
    cliente4_saldo_atual = valores[3][2]
    cliente4_emitir_boleto = valores[3][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente5_nome = valores[4][0]
    cliente5_gasto_diario = valores[4][1]
    cliente5_saldo_atual = valores[4][2]
    cliente5_emitir_boleto = valores[4][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente6_nome = valores[5][0]
    cliente6_gasto_diario = valores[5][1]
    cliente6_saldo_atual = valores[5][2]
    cliente6_emitir_boleto = valores[5][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente7_nome = valores[6][0]
    cliente7_gasto_diario = valores[6][1]
    cliente7_saldo_atual = valores[6][2]
    cliente7_emitir_boleto = valores[6][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente8_nome = valores[7][0]
    cliente8_gasto_diario = valores[7][1]
    cliente8_saldo_atual = valores[7][2]
    cliente8_emitir_boleto = valores[7][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente9_nome = valores[8][0]
    cliente9_gasto_diario = valores[8][1]
    cliente9_saldo_atual = valores[8][2]
    cliente9_emitir_boleto = valores[8][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente10_nome = valores[9][0]
    cliente10_gasto_diario = valores[9][1]
    cliente10_saldo_atual = valores[9][2]
    cliente10_emitir_boleto = valores[9][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente11_nome = valores[10][0]
    cliente11_gasto_diario = valores[10][1]
    cliente11_saldo_atual = valores[10][2]
    cliente11_emitir_boleto = valores[10][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente12_nome = valores[11][0]
    cliente12_gasto_diario = valores[11][1]
    cliente12_saldo_atual = valores[11][2]
    cliente12_emitir_boleto = valores[11][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente13_nome = valores[12][0]
    cliente13_gasto_diario = valores[12][1]
    cliente13_saldo_atual = valores[12][2]
    cliente13_emitir_boleto = valores[12][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente14_nome = valores[13][0]
    cliente14_gasto_diario = valores[13][1]
    cliente14_saldo_atual = valores[13][2]
    cliente14_emitir_boleto = valores[13][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente15_nome = valores[14][0]
    cliente15_gasto_diario = valores[14][1]
    cliente15_saldo_atual = valores[14][2]
    cliente15_emitir_boleto = valores[14][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente16_nome = valores[15][0]
    cliente16_gasto_diario = valores[15][1]
    cliente16_saldo_atual = valores[15][2]
    cliente16_emitir_boleto = valores[15][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente17_nome = valores[16][0]
    cliente17_gasto_diario = valores[16][1]
    cliente17_saldo_atual = valores[16][2]
    cliente17_emitir_boleto = valores[16][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    cliente18_nome = valores[17][0]
    cliente18_gasto_diario = valores[17][1]
    cliente18_saldo_atual = valores[17][2]
    cliente18_emitir_boleto = valores[17][4]
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente19_nome = valores[18][0]
#     cliente19_gasto_diario = valores[18][1]
#     cliente19_saldo_atual = valores[18][2]
#     cliente19_emitir_boleto = valores[18][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente20_nome = valores[19][0]
#     cliente20_gasto_diario = valores[19][1]
#     cliente20_saldo_atual = valores[19][2]
#     cliente20_emitir_boleto = valores[19][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente21_nome = valores[20][0]
#     cliente21_gasto_diario = valores[20][1]
#     cliente21_saldo_atual = valores[20][2]
#     cliente21_emitir_boleto = valores[20][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente22_nome = valores[21][0]
#     cliente22_gasto_diario = valores[21][1]
#     cliente22_saldo_atual = valores[21][2]
#     cliente22_emitir_boleto = valores[21][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente23_nome = valores[22][0]
#     cliente23_gasto_diario = valores[22][1]
#     cliente23_saldo_atual = valores[22][2]
#     cliente23_emitir_boleto = valores[22][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente24_nome = valores[23][0]
#     cliente24_gasto_diario = valores[23][1]
#     cliente24_saldo_atual = valores[23][2]
#     cliente24_emitir_boleto = valores[23][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente25_nome = valores[24][0]
#     cliente25_gasto_diario = valores[24][1]
#     cliente25_saldo_atual = valores[24][2]
#     cliente25_emitir_boleto = valores[24][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente26_nome = valores[25][0]
#     cliente26_gasto_diario = valores[25][1]
#     cliente26_saldo_atual = valores[25][2]
#     cliente26_emitir_boleto = valores[25][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente27_nome = valores[26][0]
#     cliente27_gasto_diario = valores[26][1]
#     cliente27_saldo_atual = valores[26][2]
#     cliente27_emitir_boleto = valores[26][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente28_nome = valores[27][0]
#     cliente28_gasto_diario = valores[27][1]
#     cliente28_saldo_atual = valores[27][2]
#     cliente28_emitir_boleto = valores[27][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#     cliente29_nome = valores[28][0]
#     cliente29_gasto_diario = valores[28][1]
#     cliente29_saldo_atual = valores[28][2]
#     cliente29_emitir_boleto = valores[28][4]
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

    import telebot

    API_TOKEN = '5671558124:AAFa4zJQDAfcP02L4wCUKGWl4vZgKxg6nAg'

    bot = telebot.TeleBot(API_TOKEN)
        
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_1'])
    def cliente1(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente1_nome,cliente1_gasto_diario,
        cliente1_saldo_atual,cliente1_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_2'])
    def cliente2(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente2_nome,cliente2_gasto_diario,
        cliente2_saldo_atual,cliente2_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_3'])
    def cliente3(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente3_nome,cliente3_gasto_diario,
        cliente3_saldo_atual,cliente3_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_4'])
    def cliente4(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente4_nome,cliente4_gasto_diario,
        cliente4_saldo_atual,cliente4_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_5'])
    def cliente5(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente5_nome,cliente5_gasto_diario,
        cliente5_saldo_atual,cliente5_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_6'])
    def cliente6(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente6_nome,cliente6_gasto_diario,
        cliente6_saldo_atual,cliente6_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_7'])
    def cliente7(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente7_nome,cliente7_gasto_diario,
        cliente7_saldo_atual,cliente7_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_8'])
    def cliente8(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente8_nome,cliente8_gasto_diario,
        cliente8_saldo_atual,cliente8_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_9'])
    def cliente9(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente9_nome,cliente9_gasto_diario,
        cliente9_saldo_atual,cliente9_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_10'])
    def cliente10(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente10_nome,cliente10_gasto_diario,
        cliente10_saldo_atual,cliente10_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_11'])
    def cliente11(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente11_nome,cliente11_gasto_diario,
        cliente11_saldo_atual,cliente11_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_12'])
    def cliente12(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente12_nome,cliente12_gasto_diario,
        cliente12_saldo_atual,cliente12_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_13'])
    def cliente13(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente13_nome,cliente13_gasto_diario,
        cliente13_saldo_atual,cliente13_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_14'])
    def cliente14(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente14_nome,cliente14_gasto_diario,
        cliente14_saldo_atual,cliente14_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_15'])
    def cliente15(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente15_nome,cliente15_gasto_diario,
        cliente15_saldo_atual,cliente15_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_16'])
    def cliente16(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente16_nome,cliente16_gasto_diario,
        cliente16_saldo_atual,cliente16_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_17'])
    def cliente17(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente17_nome,cliente17_gasto_diario,
        cliente17_saldo_atual,cliente17_emitir_boleto)
        bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['cliente_18'])
    def cliente18(message):
        texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente18_nome,cliente18_gasto_diario,
        cliente18_saldo_atual,cliente18_emitir_boleto)
        bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_19'])
#     def cliente19(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente19_nome,cliente19_gasto_diario,
#         cliente19_saldo_atual,cliente19_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_20'])
#     def cliente20(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente20_nome,cliente20_gasto_diario,
#         cliente20_saldo_atual,cliente20_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_21'])
#     def cliente21(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente21_nome,cliente21_gasto_diario,
#         cliente21_saldo_atual,cliente21_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_22'])
#     def cliente22(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente22_nome,cliente22_gasto_diario,
#         cliente22_saldo_atual,cliente22_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_23'])
#     def cliente23(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente23_nome,cliente23_gasto_diario,
#         cliente23_saldo_atual,cliente23_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_24'])
#     def cliente24(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente24_nome,cliente24_gasto_diario,
#         cliente24_saldo_atual,cliente24_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_25'])
#     def cliente25(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente25_nome,cliente25_gasto_diario,
#         cliente25_saldo_atual,cliente25_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_26'])
#     def cliente26(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente26_nome,cliente26_gasto_diario,
#         cliente26_saldo_atual,cliente26_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_27'])
#     def cliente27(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente27_nome,cliente27_gasto_diario,
#         cliente27_saldo_atual,cliente27_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_28'])
#     def cliente28(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente28_nome,cliente28_gasto_diario,
#         cliente28_saldo_atual,cliente28_emitir_boleto)
#         bot.reply_to(message, texto)
# #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#     @bot.message_handler(commands=['cliente_29'])
#     def cliente29(message):
#         texto = "Nome do cliente:  {}\nO Gasto Diário desse cliente é:  R$ {}\nO Saldo desse cliente é:  R$ {}\nEmitir Boleto(?):  {}".format(cliente29_nome,cliente29_gasto_diario,
#         cliente29_saldo_atual,cliente29_emitir_boleto)
#         bot.reply_to(message, texto)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(func=lambda message: True)
    def initial_menssage(message):
        texto = """
Escolha uma opção para continuar (clique no item):

/cliente_1 - {}

/cliente_2 - {}

/cliente_3 - {}

/cliente_4 - {}

/cliente_5 - {}

/cliente_6 - {}

/cliente_7 - {}

/cliente_8 - {}

/cliente_9 - {}

/cliente_10 - {}

/cliente_11 - {}

/cliente_12 - {}

/cliente_13 - {}

/cliente_14 - {}

/cliente_15 - {}

/cliente_16 - {}

/cliente_17 - {}

/cliente_18 - {}

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Desenvolvido por: Victor Rodrigues
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

"""
        bot.reply_to(message,texto.format(cliente1_nome,cliente2_nome,cliente3_nome,cliente4_nome,cliente5_nome,cliente6_nome,cliente7_nome,cliente8_nome,cliente9_nome,cliente10_nome,cliente11_nome,cliente12_nome,cliente13_nome,cliente14_nome,cliente15_nome,cliente16_nome,cliente17_nome,cliente18_nome))

# cliente1_nome,cliente2_nome,cliente3_nome,cliente4_nome,cliente5_nome,cliente6_nome,cliente7_nome,cliente8_nome,cliente9_nome,cliente10_nome,cliente11_nome,cliente12_nome,cliente13_nome,cliente14_nome,cliente15_nome,cliente16_nome,cliente17_nome,cliente18_nome,cliente19_nome,cliente20_nome,cliente21_nome,cliente22_nome,cliente23_nome,cliente24_nome,cliente25_nome,cliente26_nome,cliente27_nome,cliente28_nome,cliente29_nome
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    @bot.message_handler(commands=['start','help'])
    def initial_menssage(message):
        texto = """
Escolha uma opção para continuar (clique no item):

/cliente_1 - {}

/cliente_2 - {}

/cliente_3 - {}

/cliente_4 - {}

/cliente_5 - {}

/cliente_6 - {}

/cliente_7 - {}

/cliente_8 - {}

/cliente_9 - {}

/cliente_10 - {}

/cliente_11 - {}

/cliente_12 - {}

/cliente_13 - {}

/cliente_14 - {}

/cliente_15 - {}

/cliente_16 - {}

/cliente_17 - {}

/cliente_18 - {}


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Desenvolvido por: Victor Rodrigues
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

"""
        bot.reply_to(message,texto.format(cliente1_nome,cliente2_nome,cliente3_nome,cliente4_nome,cliente5_nome,cliente6_nome,cliente7_nome,cliente8_nome,cliente9_nome,cliente10_nome,cliente11_nome,cliente12_nome,cliente13_nome,cliente14_nome,cliente15_nome,cliente16_nome,cliente17_nome,cliente18_nome))
    bot.infinity_polling()

print('bot iniciado!!!')
if __name__ == '__main__':
    main()