#!/usr/bin/env python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with [{}] items".format(len(items)))

    def remove(self, value):
        print("Removed [{}] from the list".format(value))
        super().remove(value)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        print("Popped [{}] from the list".format(self[index]))
        item = super().pop(index)
        return item
