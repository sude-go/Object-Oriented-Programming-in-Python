"""
def Widget: -> class Widget

   def Widget(self): -> The class constructor should be named __init__.
                        This method is called when an object is created, and it initializes the object's attributes.
     self._msg = 'Hello, I'm a widget!' ->The string should be enclosed in double quotes since
                         the single quote is used inside the string
   def replace(self)  -> The replace method was trying to modify a string directly, but strings are immutable in Python.
                        I modified it to create a new string with the replacement. Also, I used the find method to get
                        the index of 'w' in the string.
     index = self.index('w')
     self._msg[index] = 'g'
   def __str__(self):
     print 'My string is: ' + self._msg ->In the __str__ method, it should return the string instead of printing it.
                                        The printing can be done when you actually print the object.
"""


class Widget:
    def __init__(self):
        self._msg = "Hello, I'm a widget!"

    def replace(self):
        index = self._msg.find('w')
        if index != -1:
            self._msg = self._msg[:index] + 'g' + self._msg[index + 1:]

    def __str__(self):
        return 'My string is: ' + self._msg


widget_instance = Widget()
widget_instance.replace()
print(widget_instance)
