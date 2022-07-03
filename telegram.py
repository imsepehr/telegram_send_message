import telepot

def send_message(token='5569209115:AAGgdW9IA7zh3iShW_UFb3bdATPX-qx2S1E', receiver_id=1169936199, message='texxxxxtt'):
    '''input info of user and send message to user'''
    bot = telepot.Bot(token)
    #send message
    bot.sendMessage(receiver_id,message)
    #bot.sendPhoto(receiver_id,photo=open('03.jpg','rb'))

def main():
    send_message()

if __name__ == '__main__':
    main()
