try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time
import smtplib
import string
from config import config

calendar_client = gdata.calendar.client.CalendarClient()
username = config['username']
visibility = config['visibility']
secret = config['secret']
projection = 'full'
feed_uri = calendar_client.GetCalendarEventFeedUri(calendar=username, visibility=visibility, projection=projection)
SUBJECT = "Test email from Python"
FROM = username
text = "blah blah blah"

def DateRangeQuery(calendar_client, feed_uri, start_date='2012-12-01', end_date='2013-05-22'):
    print 'Date range query for events on Primary Calendar: %s to %s' % (start_date, end_date,)
    query = gdata.calendar.client.CalendarEventQuery()
    query.start_min = start_date
    query.start_max = end_date
    feed = calendar_client.GetCalendarEventFeed(uri=feed_uri, q=query)
    for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
        print '\t%s. %s' % (i, an_event.title.text,)
        for p, a_participant in zip(xrange(len(an_event.who)), an_event.who):
            print '\t\t%s. %s' % (p, a_participant.email,)
            print '\t\t\t%s' % (a_participant.value,)
            if(a_participant.email != FROM and a_participant.email != "unknownorganizer@calendar.google.com"):
                TO = a_participant.email
                BODY = string.join((
                                    "From: %s" % FROM,
                                    "To: %s" % TO,
                                    "Subject: %s" % SUBJECT ,
                                    "",
                                    text
                                    ), "\r\n")
                session = smtplib.SMTP('smtp.gmail.com', 587)
                session.ehlo()
                session.starttls()
                session.ehlo
                session.login(FROM, secret)
                session.sendmail(FROM, [TO], BODY)
                session.quit()
                if a_participant.attendee_status:
                    print '\t\t\t%s' % (a_participant.attendee_status.value,)

DateRangeQuery(calendar_client, feed_uri)

    



