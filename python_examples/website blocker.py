# import datetime
# import time
# date = datetime.datetime(2025,2,1)
# website_block = ['']
# host_path = 'C:/Windows/System32/drivers/etc/hosts'
# redirect = '127.0.0.1'

# #main functional workflow
# while True:
#     if datetime.datetime.now()<date:
#         print('site blocking')
#         with open(host_path,'r+') as file:
#             data = file.read()
#             for website in website_block:
#                 if website not in data:
#                     file.write(redirect+' '+website+'\n')
#                 else:
#                     pass
#     else:
#         with open(host_path,'r+') as file:
#             data = file.readlines()
#             file.seek(0)  #get the cursor in the first word of first line
#             for line in data:
#                 if not any(website in line for website in website_block):  #reset the whole file
#                     file.write(line)
#             file.truncate()
#         time.sleep(5)
