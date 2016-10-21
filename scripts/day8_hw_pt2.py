class ToDoList():
    def __init__(self, items = None):
        self.items = items
        if self.items == None:
            self.items = list()
        self.index = self.tdl_index()

    # def __str__(self):
    #     return [index, item for index, item in enumerate(self.items)]

    def tdl_index(self):
        return range(len(self.items))

    def add_item(self, item):
        self.items.append(item)

    def mark_done(self, item_no):
        self.items.pop(item_no)
        self.index = self.tdl_index()

if __name__ == "__main__":
    tdl = ToDoList()
    tdl.add_item("Wash the dishes")
    tdl.add_item("Do OOP homework")
    print tdl.items
    tdl.mark_done(1) # mark the second item as done
    print tdl.items
