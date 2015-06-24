import datetime
import sys

def days_from_now(days):
    return (datetime.datetime.now() + datetime.timedelta(days=int(days)))

def days_since(year, month, day):
    then = datetime.datetime(year, month, day)
    now = datetime.datetime.now()
    return now - then

if __name__ == '__main__':
    sys.argv.pop(0)
    if len(sys.argv) == 1:
        print 'date in %s days %s' % (sys.argv[0], days_from_now(sys.argv[0])) 
    elif len(sys.argv) == 3:
        print 'days since then: %s' % days_since(int(sys.argv[0]), int(sys.argv[1]), int(sys.argv[2])).days

# Now, this code is dirty, make it beautiful:
# - assign sys.argv calls to variables
# - split one liners into more readable flow
# - defend yourself from a different number of arguments than 1 or 3
# - pretty print the date in 1st case
# - is that pop really necessary?
# - is this code completely pep8 valid?
