import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom.data
import time


calendar_client = gdata.calendar.client.CalendarClient()
username = 'yourusername@gmail.com'
visibility = 'private-someNumbersandletters'
projection = 'full'
feed_uri = calendar_client.GetCalendarEventFeedUri(calendar=username, visibility=visibility, projection=projection)

def DateRangeQuery(calendar_client,feed_uri, start_date='2012-12-01', end_date='2013-05-01'):
  print 'Date range query for events on Primary Calendar: %s to %s' % (start_date, end_date,)
  query = gdata.calendar.client.CalendarEventQuery()
  query.start_min = start_date
  query.start_max = end_date
  feed = calendar_client.GetCalendarEventFeed(uri=feed_uri,q=query)
  for i, an_event in enumerate(feed.entry):
    print '\t%s. %s' % (i, an_event.title.text,)
    for a_when in an_event.when:
      print '\t\tStart time: %s' % (a_when.start,)
      print '\t\tEnd time:   %s' % (a_when.end,)
      
def GetOwnCalendars(calendar_client):
  feed = calendar_client.GetOwnCalendarsFeed()
  print feed.title.text
  for i, a_calendar in enumerate(feed.entry):
    print '\t%s. %s' % (i, a_calendar.title.text,)

DateRangeQuery(calendar_client,feed_uri)
