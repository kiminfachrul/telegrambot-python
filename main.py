import telebot
import threading
from ss_jadwal import open_chrome_and_screenshot

# Masukkan TOKEN bot Telegram Anda
API_TOKEN = '74'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello World! gunakan /schedule untuk penjadwalan screenshot dan gunakan /screenshot_now untuk ss sekarang")

@bot.message_handler(commands=['schedule'])
def handle_schedule(message):
    msg = bot.reply_to(message, "Send the time for the screenshot (format: HH:MM):")
    bot.register_next_step_handler(msg, process_time_step)

def process_time_step(message):
    schedule_time = message.text
    save_path = "screenshot.png"  # Anda bisa mengganti nama dan path file screenshot sesuai kebutuhan
    
    # Jalankan fungsi penjadwalan screenshot di thread terpisah
    threading.Thread(target=open_chrome_and_screenshot, args=(save_path, schedule_time)).start()
    
    bot.reply_to(message, f"Screenshot dijadwalkan setiap hari pada {schedule_time}")

@bot.message_handler(commands=['screenshot_now'])
def handle_screenshot_now(message):
    save_path = "screenshot_now.png"
    
    # Ambil screenshot secara langsung
    open_chrome_and_screenshot(save_path)
    
    # Kirim screenshot kepada pengguna
    with open(save_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    
    bot.reply_to(message, "Screenshot diambil dan dikirim.")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
