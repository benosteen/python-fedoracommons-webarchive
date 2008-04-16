from heapsort import HeapSort
from date_event import *

import bisect, os

from cStringIO import StringIO

import vobject

import uuid, datetime

import logging

# For Timeline XML output:

from xml.dom import minidom

class Events(object):
    def __init__(self, fedoraClient = None):
        """
        Initialise the ical object with a blank iCalendar object
        """
        # Holds a vobject.iCalendar() instance
        self.ical = None
        # Holds the pid of this calendar
        self.pid = None
        # Create an instance of the sort algorithm
        self.sort = HeapSort()
        
        self.fedoraClient = fedoraClient
        # Set the calendar to blank initially
        self.setCalendar()
    
    def setCalendar(self, ical_text=None, pid=None):
        # Set self.pid to whatever was passed
        if pid != None:
            self.pid = pid
            
        if not ical_text:
            if self.pid != None and self.fedoraClient != None:
                ical_text = self.fedoraClient.getDatastream(self.pid, 'EVENT')
                if not (isinstance(ical_text, int) or ical_text.startswith('no path in db registry for [') or ical_text.startswith('[DefaulAccess] No datastream could be returned')):
                    self.ical = vobject.readOne(ical_text)
                else:
                    # set the event object to a blank calendar
                    self.ical = vobject.iCalendar()
            else:
                # set the event object to a blank calendar
                self.ical = vobject.iCalendar()
        else:
            # load the event object to a 
            self.ical = vobject.readOne(ical_text)
            
    def store(self, store='/tmp/'):
        if self.pid != None and self.fedoraClient != None:
            filename = os.path.join('/tmp/', str(uuid.uuid4())+'.ics')
            permanent_file = open(filename, 'w')
            permanent_file.write(self.toString())
            permanent_file.close()
            response = self.fedoraClient.putFile(self.pid, 'EVENT', filename, params={'dsLabel':'Events'})
            try:
                os.remove(filename)
            except OSError:
                pass
                
            return response
            
    def getAlarms(self, from_date=None, to_date=None):
        alarms = []
        if self.ical == None:
            return []
        for event in self.ical.contents.get('vevents', []):
            for alarm in event.content.get('valarm', []):
                trigger_dates = alarm.__getattr__('trigger')
                if trigger_dates != None:
                    alarms.append(Date_Event(trigger_dates[0].value, event))
        #Sort the list of dates, if there are any
        if len(alarms>1):
            self.sort.HeapSort(alarms)
            
        if isinstance(from_date, datetime.date) and isinstance(to_date, datetime.date) and from_date < to_date:
            alarms = self.getRange(alarms, from_date, to_date)
        
        return alarms
    
    def getEvents(self, datefield='dtstart', from_date=None, to_date=None):
        allowed_datefields = ['dtstart',
                              'dtend',
                              'dtstamp']
        if allowed_datefields.__contains__(datefield) != True:
            datefield = allowed_datefields[0]
            
        events = []
        if self.ical == None:
            return events
           
        for event in self.ical.contents.get('vevent', []):
            try:
                date = event.__getattr__(datefield)
                events.append(Date_Event(date.value, event))
            except AttributeError:
                # This event doesn't have the requisite date field
                # Ignore the error and continue
                pass

        #Sort the list of dates, if there are any
        if len(events)>1:
            self.sort.HeapSort(events)
            
        if isinstance(from_date, datetime.date) and isinstance(to_date, datetime.date) and from_date < to_date:
            events = self.getRange(events, from_date, to_date)
        
        return events

    def getJournalNotes(self, from_date=None, to_date=None):
        events = []
        if self.ical == None:
            return events
           
        for event in self.ical.contents.get('vjournal', []):
            try:
                date = event.__getattr__('dtstamp')
                events.append(Date_Event(date.value, event))
            except AttributeError:
                # This event doesn't have the requisite date field
                # Ignore the error and continue
                pass

        #Sort the list of dates, if there are any
        if len(events)>1:
            self.sort.HeapSort(events)
            
        if isinstance(from_date, datetime.date) and isinstance(to_date, datetime.date) and from_date < to_date:
            events = self.getRange(events, from_date, to_date)
        
        return events
     
    def addJournalNote(self, description, utcdate=None, category='action'):
        if self.ical == None or description == None or description == '':
            return False
            
        journal_event = self.ical.add('vjournal')
        # Get some boiler plate items, like a uuid and current time
        # Whilst the iCal RFC recommends an email-like UID, the text of the RFC states that
        # this is to provide a globally persistant ID. The format of this compontent is defined:
        # uid        = "UID" uidparam ":" text CRLF
        # http://tools.ietf.org/html/rfc2445#section-4.8.4.7
        # The UUID scheme seems to be a perfect fit here instead, and this is what this shall
        # use initially.
        
        # Generate a random uuid
        uid = str(uuid.uuid4())

        # Get the current date and time
        now = datetime.datetime.now()
        
        if utcdate:
            try:
                now = datetime.datetime.strptime(utcdate.split('.')[0], "%Y-%m-%dT%H:%M:%S")
            except ValueError:
                # Not a valid date. Retain today's date
                logging.error("Not a valid date. Retain today's date for this journal entry")
                pass
        
        journal_event.add('dtstamp').value = now
        journal_event.add('uid').value = uid
        
        journal_event.add('category').value = category
        journal_event.add('description').value = description
        
        return True

        
        
    def getRange(self, date_event_list, from_date, to_date):
        # Sort list to be sure
        self.sort.HeapSort(date_event_list)
        
        # To make sure that the bisect algo is comparing apples to apples:
        to_date_for_comparison = Date_Event(to_date, None)
        from_date_for_comparison = Date_Event(from_date, None)
        
        lowest_index = bisect.bisect_left(date_event_list, from_date_for_comparison)
        highest_index = bisect.bisect_right(date_event_list, to_date_for_comparison)
        
        # Sanity check: the earliest index is less that the more recent index
        # If not, the list may not be ordered properly
        if lowest_index < highest_index:
            return date_event_list[lowest_index:highest_index]
        # Else, if the lowest index is the same as the highest, make sure that one
        # result satifies both boundaries
        elif lowest_index == highest_index and date_event_list[lowest_index] > from_date_for_comparison and date_event_list[lowest_index] < to_date_for_comparison:
            return [date_event_list[lowest_index]]
        # Otherwise, return an empty list
        else:
            return []

    ######################################################################
    # Output options:
    ######################################################################
                
    def print_list(self,date_event_list):
        """
        Convienience function to 'pretty print' a list comprising of
        Date_Event objects, such as what the response from .getEvents() would be
        """
        for date_event in date_event_list:
            print '='*30
            print date_event.datetime.ctime()
            try:
                print date_event.vevent.summary.value
            except AttributeError:
                pass
            try:
                print date_event.vevent.description.value
            except AttributeError:
                pass
    
    def print_list_to_HTML(self,date_event_list):
        """
        Convienience function to 'pretty print' a list comprising of
        Date_Event objects, such as what the response from .getEvents() would be.
        Outputs in the following format:
        <div id='events'>
            <div class="event_list_item">
                <div class="event_date">date.ctime()</div>
                <div class="event_description">Description from event</div>
            </div>
            <div class="event_list_item">
            ... etc
        </div>
        """
        
        html = u"<div id='events'> <p class='events_title'>Events:</p>\n"
        
        date_event_list.reverse()
        
        for date_event in date_event_list:
            html += u"  <div class='event_list_item'>\n    <div class='event_date'><p>"
            try: 
                html += date_event.datetime.ctime()
            except:
                pass
            html += u"</p>\n    </div>\n"
            html += u"    <div class='event_description'><p>"
            try: 
                html += date_event.vevent.description.value
            except AttributeError:
                pass
            html += u"</p>\n    </div>\n  </div>\n"
            
        html+= u"</div>"
        
        return html
            
    def toSimileTimeline(self):
        events = self.getJournalNotes()
        events.extend(self.getEvents())
        
        # It turns out that a very simple XML file is all that is needed:
        template =  u"""<data></data>"""
        
        timeline_doc = minidom.parseString(template)
        
        for date_event in events:
            try:
                event_node = timeline_doc.createElement('event')
                
                event_node.setAttribute('start', self.datetime_to_timeline_format(date_event.datetime) )
                
                desc = date_event.vevent.description.value
                event_node.setAttribute('title', desc[:15]+'...')
                
                desc_node = timeline_doc.createTextNode(desc)
                event_node.appendChild(desc_node)
                timeline_doc.documentElement.appendChild(event_node)
            except AttributeError:
                pass
        
        return timeline_doc.toxml()
        
    def datetime_to_timeline_format(self, date_event):
        # Silly Simile Timeline, you no seem to support iso8601 properly...
        # Tsk, tsk.
        # Therefore we need to fudge around the date to get something you
        # do understand:
        months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        # Get the date as a tuple: 21 August - 11am is equivalent to:
        # (2007, 8, 21, 11, 0, 11, 1, 233, 0)
        # We are only interested in the first 6 values
        
        # Timeline's magic format is in the form of:
        # "Jun 28 2006 00:00:00 GMT"
        if isinstance(date_event, datetime.datetime):
            datetime_tuple = date_event.utctimetuple()
            
            date_list = []
            
            # Month as a 3 letter abbrev.
            date_list.append(months[datetime_tuple[1]-1])
            
            # Date of month.
            date_list.append(datetime_tuple[2])
            
            # Year
            date_list.append(datetime_tuple[0])
            
            # Time:
            date_list.append("%02d:%02d:%02d" % datetime_tuple[3:6])
            
            # GMT
            date_list.append('GMT')

            return ' '.join(map(str, date_list))
        else:
            return ''
    
    def toString(self):
        """
        Returns an iCal encoded calendar file. On a failure of some kind, it will return ''
        """
        if self.ical != None:
            return self.ical.serialize()
        else:
            return ''
