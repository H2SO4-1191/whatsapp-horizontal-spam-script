import random
import pywhatkit as pwk
import time

def main():
    input("Press Enter to start process...")
    message_asset = "https://google.com" #An asset that is included in all messages, could be a link, an invitation or left blank if not needed
    messages = [
        "Hello",
        "World",

        #Add different messages here to avoid spam ban
    ]
    phone_numbers = [
        "+964xxxxxxxxxx",
        "+964xxxxxxxxxx",

        #Add numbers here, preferably less than 40 each sitting if sending to non-contacts numbers to avoid spam ban
    ]
    successfuly_sent = 0
    message_index = 0
    for number in phone_numbers:
        try:
            message = messages[message_index] + "\n" + message_asset
            message_index += 1
            if message_index >= len(messages): message_index = 0
            print(f"Sending message to {number}")
            pwk.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=True)
            successfuly_sent += 1
        except Exception as e:
            print("Failed to send message to " + number + ": \n " + str(e))
        time.sleep(random.randint(70, 100)) #Adjust random time between messages as you want, preferably 1-2 minutes to avoid spam ban
    print("Message had been successfully sent to " + str(successfuly_sent) + " phone numbers.")
    input("Press Enter to exit...")

if __name__ == "__main__": 
    main()
