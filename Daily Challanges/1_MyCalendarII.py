'''You are implementing a program to use as your calendar. We can add a new event if adding the 
event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment
 is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on 
the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully 
without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]'''

class MyCalendarTwo(object):

    def __init__(self):
        self.booking=[]
        self.overlaps=[]    
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for overlaps_start ,overlaps_end in self.overlaps:
            if max(start,overlaps_start)<min(end,overlaps_end):
                return False

        for booking_start,booking_end in self.booking:
            if max(start,booking_start)<min(end,booking_end):
                self.overlaps.append((max(start,booking_start),min(end,booking_end)))

        self.booking.append((start,end))  
        return True              


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
param_1 = obj.book(10,20)
