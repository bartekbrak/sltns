import datetime
my_birthday = datetime.datetime(1985, 4, 15)
now =  datetime.datetime.now()
result = now - my_birthday
print 'days: %s' % result.days
print 'hours: %s' % int(result.total_seconds() / (60*60))
in_1000_days = datetime.datetime.now() + datetime.timedelta(days=1000)
print 'in 1000 days: %s' % in_1000_days.strftime('%Y-%m-%d')
