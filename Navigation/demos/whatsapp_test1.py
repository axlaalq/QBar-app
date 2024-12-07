import pywhatkit

phone_number = '+52 618 2301355'
group_id = 'Documentos'
message = 'Prueba'
time_hour = 10
time_minute = 52
waiting_time_to_send = 10
close_tab=True
waiting_time_to_close = 2

mode='group'

if mode == 'contact':
    pywhatkit.sendwhatmsg(phone_number, message,time_hour,time_minute,waiting_time_to_send,close_tab,waiting_time_to_close)
elif mode == 'group':
    pywhatkit.sendwhatmsg_to_group(phone_number, message,time_hour,time_minute,waiting_time_to_send,close_tab,waiting_time_to_close)
else:
    print ('error')
