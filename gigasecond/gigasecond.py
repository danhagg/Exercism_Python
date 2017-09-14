import datetime
def add_gigasecond(dob):
    """function adds 10^9 seconds to a persons birthday
    default times of day are 00.00.00 but can be added manually"""
    tdelta = datetime.timedelta(seconds=1000000000)
    gigabirthday = dob + tdelta
    return gigabirthday
