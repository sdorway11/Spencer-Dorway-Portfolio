from datetime import datetime, timedelta


curdate = datetime.time(datetime.now())

def timezone(zone):
    zoneTime = datetime.now() + timedelta(hours=zone)
    time = datetime.time(zoneTime)
    return time


def OpenOrClosed(cityTime):
    openTime = curdate.replace(hour=9, minute=0,second= 0, microsecond = 0)
    closeTime = curdate.replace(hour=21, minute=0, second=0, microsecond=0)
    if cityTime >  openTime and cityTime < closeTime: 
        return "the branch is open"
    else:
        return "the branch is closed"


def main():
    newYork = timezone(3)
    london = timezone(7)
    print "It is currently", curdate.strftime("%I:%M:%S %p"), " in Portland"
    print "It is", newYork.strftime("%I:%M:%S %p"), "in New York and "+ \
          str(OpenOrClosed(newYork))
    print "It is", london.strftime("%I:%M:%S %p"), "in London and "+ \
          str(OpenOrClosed(london))
 

if __name__ == "__main__": main()
