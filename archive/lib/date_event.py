"""
Creates a wrapper class for a datetime object, such that it has an additional attribute of 
a vevent. This is to retain __gt__(date1,date2) comparison type inbuilt methods.
"""

import datetime

class Date_Event(object):
    def __init__(self, datetime, vevent):
        self.datetime = datetime
        self.vevent = vevent
    
    def __lt__(self, other):
        if isinstance(other, Date_Event):
            return datetime.datetime.__lt__(self.datetime, other.datetime)
        else:
            return datetime.datetime.__lt__(self.datetime, other)
    
    def __le__(self, other):
        if isinstance(other, Date_Event):
            return datetime.datetime.__le__(self.datetime, other.datetime)
        else:
            return datetime.datetime.__le__(self.datetime, other)
    
    def __gt__(self, other):
        if isinstance(other, Date_Event):
            return datetime.datetime.__gt__(self.datetime, other.datetime)
        else:
            return datetime.datetime.__gt__(self.datetime, other)
    
    def __ge__(self, other):
        if isinstance(other, Date_Event):
            return datetime.datetime.__ge__(self.datetime, other.datetime)
        else:
            return datetime.datetime.__ge__(self.datetime, other)
    
    def __eq__(self, other):
        if isinstance(other, Date_Event):
            return datetime.datetime.__eq__(self.datetime, other.datetime)
        else:
            return datetime.datetime.__eq__(self.datetime, other)
    
    def __ne__(self, other):
        if isinstance(other, Date_Event):
            return datetime.datetime.__ne__(self.datetime, other.datetime)
        else:
            return datetime.datetime.__ne__(self.datetime, other)
