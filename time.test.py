import datetime

now = datetime.datetime.now()
t = now.strftime('%Y-%m-%d %H:%M:%S')
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print('%s' % t)

i = datetime.datetime.now()
print ('%s' % i.isoformat())