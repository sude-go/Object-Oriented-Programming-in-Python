import datetime


class Date:
    """
    Date class to represent a date in numerical and text format.
    It also supports computing the next day of the year.
    """

    def __init__(self, month: int, day: int, year: int):
        """
        Constructor for the Date class.
        :param month: int, the month of the year.
        :param day: int, the day of the month.
        :param year: int, the year.
        """
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        """
        Return a string representation of the date in numerical format.
        :return: str, the string representation of the date.
        """
        return f"{self.month}/{self.day}/{self.year}"

    def computeNext(self):
        """
        Compute the next day of the year.
        :return: Date, the next day of the year.
        """
        next_date = datetime.date(self.year, self.month, self.day) + datetime.timedelta(days=1)
        return Date(next_date.month, next_date.day, next_date.year)
