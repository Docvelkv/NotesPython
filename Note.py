import datetime as dt


class Note:
    def __init__(self,
                 title=None,
                 content=None):
        self.title = title
        self.dateTime = dt.datetime.now().strftime("%d.%m.%y %H:%M")
        self.content = content
