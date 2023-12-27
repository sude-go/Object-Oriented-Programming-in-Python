class Date:
    monthNames = ('January', 'February', 'March',
                  'April', 'May', 'June', 'July', 'August',
                  'September', 'October', 'November', 'December')

    def __init__(self):
        self._month = 1
        self._day = 1
        self._year = 2000

    def get_day(self):
        return self._day

    """
    (b) Define a setYear function that takes an integer parameter
    specifying the year and sets the value of the year attribute.
    """

    def set_year(self, year):
        self._year = year
        return self._year

    """
    (c) Define the __str__ function. This should return a string that represents the
    date in the format 'January 1, 2000'.
    """

    def __str__(self):
        return f"{Date.monthNames[self._month - 1]} {self._day}, {self._year}"


test_date = Date()
print(test_date.get_day())
print(test_date.set_year(2002))
print(test_date)
