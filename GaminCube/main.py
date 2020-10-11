import os
import time
from datetime import date 
from datetime import datetime

def send_messages(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

def get_today():
    return datetime.today().strftime('%A')

def get_hour():
    return datetime.now().strftime("%H:%M")

now = get_hour()
day = get_today()
phone = "3232715672"

send_messages(phone, "Hello, This is TheGamingCube's Bot")
send_messages(phone, "This will be a bot that notifies you when you have class!")

for i in range(1440):
    time.sleep(60)
    now = get_hour()
    day = get_today()
    print("now =", now)
    print("today = ", day)
    if day == "Monday" or day == "Wednesday":
        if now == "7:55":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "7:59":
            send_messages(phone, "One Minute Till AP Bio!")
            send_messages(phone, "https://us02web.zoom.us/j/96182082414?pwd=eUc0SXpsS09ndmhhVWRzamtIcmRrQT09")
        elif now == "9:25":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "9:29":
            send_messages(phone, "One Minute Till AP Calculus BC!")
            send_messages(phone, "https://zoom.us/j/95979662195?pwd=d1RKRDFsaUR2ZUFMemowRVNGUTcxUT09")
        elif now == "10:55":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "10:59":
            send_messages(phone, "One Minute Till Digital Photo!")
            send_messages(phone, "https://meet.google.com/lookup/edzlr67rei?authuser=1&hs=179")
        elif now == "14:30":
            send_messages(phone,"Attendence Forms")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=1")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=2")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=3")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=7")
        if day == "Monday" and now == "14:59":
            send_messages(phone, "One Minute Till XC Google Meets")
            send_messages(phone, "https://meet.google.com/lookup/edzlr67rei?authuser=1&hs=179")

    elif day == "Tuesday" or day == "Thursday":
        if now == "7:55":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "7:59":
            send_messages(phone, "One Minute Till AP Gov!")
            send_messages(phone, "https://us02web.zoom.us/j/89078038414?pwd=M3VUc1pyU1FWQlI5QS9ySGFjZ0pjQT09")
        elif now == "9:25":
            send_messages(phone, "You Have Class in 5 Minutes, get ready to join")
        elif now == "9:29":
            send_messages(phone, "One Minute Till ERWC(English)!")
            send_messages(phone, "https://us02web.zoom.us/j/82412177292?pwd=UXpIWmVhKzJmb296WWt2eG1WV2s5Zz09")
        elif now == "14:30":
            send_messages(phone,"Attendence Forms")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=4")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=5")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=7")
    if day == "Friday":
        if now == "15:00":
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=1")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=2")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=3")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=4")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=5")
            send_messages(phone,"https://docs.google.com/forms/d/e/1FAIpQLScs81tH_SGnpBdnfYlYtWQqSzB-zYz15Azon99WuRO_kKyk7Q/viewform?entry.1828733646=Cody&entry.761704581=Lin&entry.1242183593=7")