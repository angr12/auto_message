import pywhatkit as kit

def test():
    try:
        kit.sendwhatmsg_to_group("", "Hello World", 00, 40, 30, True, 5)
        print("Message Sent")
        
    except:
        print("An Unexpected Error!")
        
def send_message(group_id:str, message:str, hour:int, minute:int, wait_time:int, tab_close:bool):
    try:
        kit.sendwhatmsg_to_group(group_id, message, hour, minute, wait_time, tab_close)
        print("Message Sent")
        
    except:
        print("An Unexpected Error!")

if __name__ == '__main__':
    test()