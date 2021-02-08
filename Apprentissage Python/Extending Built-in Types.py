class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


text = Text("Python")
print(text.duplicate())

tList = TrackableList([1, 2, 3])
tList.append(4)
