from view import View
from crontab import dummy_cronjobs

if __name__ == '__main__':
    view = View("540x570")
    view.runView(dummy_cronjobs)
    view.app.mainloop()
