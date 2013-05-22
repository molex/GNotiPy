try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import smtplib
import string
import dateutil.parser
from config import config
from datetime import date, datetime, timedelta



calendar_client = gdata.calendar.client.CalendarClient()
FROM = config['username']

def GetFeed():
    username = config['username']
    visibility = config['visibility']
    projection = 'full'
    feed_uri = calendar_client.GetCalendarEventFeedUri(calendar=username, visibility=visibility, projection=projection)
    return feed_uri

def SendMail(to_address, an_event):
    for a_when in an_event.when:
        start = datetime.strftime(dateutil.parser.parse(a_when.start), "%m/%d/%y %I:%M")
        print start
    SUBJECT = "Tot Spot Duties"    
    text = string.join(("You have signed up for %s" % an_event.title.text,
                        "On %s " % start, "\r\n"))
    secret = config['secret']
    if(to_address != FROM):
        BODY = string.join((
            "From: %s" % FROM,
            "To: %s" % to_address,
            "Subject: %s" % SUBJECT ,
            "",
            text
            ), "\r\n")
        session = smtplib.SMTP('smtp.gmail.com:587')
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(FROM, secret)
        session.sendmail(FROM, to_address, BODY)
        session.quit()

def DateRangeQuery(start_date, end_date):    
    query = gdata.calendar.client.CalendarEventQuery()
    query.start_min = start_date
    query.start_max = end_date
    feed = calendar_client.GetCalendarEventFeed(uri=GetFeed(), q=query)
    for an_event in feed.entry:        
        for a_participant in an_event.who:
            print a_participant.email
            if(a_participant.email != FROM and a_participant.email != "unknownorganizer@calendar.google.com"):
                SendMail(a_participant.email, an_event)
                
def main():
    start_date = date.today()
    end_date = datetime.date(datetime.today() + timedelta(days=7))
    DateRangeQuery(start_date, end_date)
                
main()

    
