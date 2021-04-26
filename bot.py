import telebot
from telebot import TeleBot
import pcinfoforhack
import sshconn


bot: TeleBot = telebot.TeleBot('TOKEN')
gpu = pcinfoforhack.gpu_name()
cpu = pcinfoforhack.proc_load()


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == "info":
        ram = pcinfoforhack.ram_size()
        if gpu[1] == "OK":
            stat_err = "✅"
        else:
            stat_err = "🚫"

        total_ram = round(ram[0] / 1024 / 1024 / 1024, 1)
        used_ram = round(ram[1] / 1024 / 1024 / 1024, 1)
        fin_text = '{} GPU: {}\n\nProcess load: {}%\n\n {} / {}Gb ({}%)'.format(stat_err, gpu[0], cpu,
                                                                                total_ram, used_ram, ram[2])
        bot.send_message(message.chat.id, fin_text)
    else:
        try:
            bot.send_message(message.chat.id, sshconn.ssh_connect(message.text))
        except:
            bot.send_message(message.chat.id, "Complete")


bot.polling()
