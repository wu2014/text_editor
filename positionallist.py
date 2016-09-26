"""
File: positionallist.py

Positional lists.
"""
from node import TwoWayNode
class LinkedPositionalList(object):
    """ Linked implementation of a positional list."""

    def __init__(self):
        self._head = TwoWayNode(None, None, None)
        self._head.next = self._head
        self._head.previous = self._head
        self._cursor = self._head
        self._lastItemPos = None
        self._size = 0
        self._cursorDefined = False

    def hasNext(self):
        return self._cursor != self._head

    def hasPrevious(self):
        return self._cursor.previous != self._head

    def first(self):
        """Moves he cursor to the first item
        if there is one."""
        if not self.isEmpty():
            self._cursor = self._head.next
            self._lastItemPos = None
            self._cursorDefined = True

    def last(self):
        """Moves the cursor to the last item
        if there is one."""
        if not self.isEmpty():
            self._cursor = self._head
            self._lastItemPos = self._cursor.previous
            self._cursorDefined = True

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: lastItemPos refers to the node that
                       contains the data item returned."""
        if not self.hasNext():
            raise AttributeError, "No next item"
        self._lastItemPos = self._cursor
        self._cursor = self._cursor.next
        return self._lastItemPos.data

    def previous(self):
        """Precondition: hasPrevious returns True."""
        if not self.hasPrevious():
            raise AttributeError, "No previous item"
        self._lastItemPos = self._cursor.previous
        self._cursor = self._cursor.previous
        return self._lastItemPos.data

    def insert(self, item):
        """Inserts item after the current cursor position, or
        after the last item if the cursor is undefined."""
        newNode = TwoWayNode(item, self._cursor.previous, self._cursor)
        self._cursor.previous.next = newNode
        self._cursor.previous = newNode
        self._size += 1
        if self.isCursorDefined():
            self._cursor = newNode
        self._lastItemPos = newNode.previous

    def remove(self):
        """Removes the item most recently returned by
        next or previous.
        Precondition: insert or remove was not the most
                      recently used method."""
        if self._lastItemPos is None:
            raise AttributeError, "No established item to remove"
        if not self.isCursorDefined():
            raise AttributeError, "Cursor is not defined"
        if self._lastItemPos == self._cursor:
            self._cursor = self._cursor.next
        self._lastItemPos.previous.next = self._lastItemPos.next
        self._lastItemPos.next.previous = self._lastItemPos.previous
        self._size -= 1
        self._lastItemPos = self._lastItemPos.previous

    def replace(self, item):
        """Replaces the item most recently returned by
        next or previous.
        Precondition: insert or remove was not the most
                      recently used method."""
        if self._lastItemPos is None:
            raise AttributeError, "No established item to set"
        self._lastItemPos.data = item

    def isEmpty(self):
        return len(self) == 0

    def isCursorDefined(self):
        return self._cursorDefined
    
    def __len__(self):
        return self._size

    def __str__(self):
        """Includes items from first through last."""
        result = ""
        probe = self._head.next
        while probe != self._head:
            result += str(probe.data) + " "
            probe = probe.next
        return result

def main():
    a = LinkedPositionalList()
    while True:
        print "\ntext-editor Menu for a positional list:"
        print "1 - Enter a filename of a text (.txt) file to edit"
        print "2 - Create a new text (.txt) file to edit"
        print "3 - Navigate and display the first line"
        print "4 - Navigate and display the last line"
        print "5 - Navigate and display the next line"
        print "6 - Navigate and display the previous line"
        print "7 - Insert a new line at the current cursor position"
        print "8 - Delete the current cursor position"
        print "9 - Replace the current line with a new line"
        print "10 - Save the current list back to a text file"
        print "11 - exit the menu"
        response = raw_input("Choice (1 - 11)? ")
        if response == '1':
            file_name = raw_input("Enter a filename of a text (.txt) file to edit: ")
            edit_file = open(file_name, 'r')
            for line in edit_file:
               a.insert(line)
        elif response == '2':
            file_name = raw_input("Create a new text (.txt) file to edit: ")
            edit_file = open(file_name, 'w')
            edit_file.write(str(a))
        elif response == '3':
            a.first()
            print a.next()
        elif response == '4':
            a.last()
            print a.previous()
        elif response == '5':
            if a.hasNext(): print a.next()
        elif response == '6':
            if a.hasPrevious(): print a.previous()
        elif response == '7':
            newLine = raw_input("Insert a new line at the current cursor position: ")
            a.insert(newLine +'\n')
        elif response == '8':
            a.remove()
        elif response == '9':
            newLine = raw_input("Replace the current line with a new line: ")
            a.replace(newLine + '\n')
        elif response == '10':
            file_name = raw_input("Enter a new text (.txt) file to save: ")
            edit_file = open(file_name, 'w')
            edit_file.write(str(a))   
            edit_file.close()             
        elif response == '11':
            break
        else:
            print "Invalid Menu Choice!"         

if __name__ == '__main__': 
    main()
