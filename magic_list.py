class MagicList(list):
    def __init__(self, cls_type=None):
        super(list, self).__init__()
        self.cls_type = cls_type

    def __setitem__(self, key, value):
        if key <= len(self):
            self.insert(key, value)
            list.__setitem__(self, key, value)
        else:
            raise IndexError('list index out of range')

    def __getitem__(self, item):
        if item == len(self):
            if self.cls_type is not None:
                self.insert(item, self.cls_type())
                return list.__getitem__(self, item)
            else:
                self.insert(item, None)
                return list.__getitem__(self, item)
        elif item < len(self):
            return list.__getitem__(self, item)
        else:
            raise IndexError('list index out of range')
