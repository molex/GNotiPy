GNotiPy
=======

Python script that generates reminder e-mails based on Google Calendar events

In order for this program to work properly, you will need to create a config file named config.py 
in the src folder that looks like this:
```python
config = {
    'username': 'yourGoogleAccount@gmail.com',
    'visibility': 'private-randomlettersandnumbersobtainedfromaccountcalendar',
    'secret': 'passwordForGoogleAccount'
}
```

This program uses magic cookie authentication.
The appropriate value for a magic cookie can be obtained through the 
'Calendar details' page in the UI for each of your calendars. It is labeled as a 'Private Address'.
You will need the portion that is like 'private-abc123'
