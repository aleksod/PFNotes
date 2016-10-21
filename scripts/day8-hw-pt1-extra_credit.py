class TipOutTracker():
    def __init__(self, default_tip = 0.18):
        self.default_tip = default_tip
        self.bills_n_tips = []

    def __len__(self):
        return len(self.bills_n_tips)

    def get_tips(self):
        return [bill * tip for bill, tip in self.bills_n_tips]

    def add_bill(self, bill, tip = None):
        if tip == None:
            tip = self.default_tip
        self.bills_n_tips.append((bill, tip))

    def __add__(self, another_class_instance):
        for i, bill_n_tip in enumerate(another_class_instance.bills_n_tips):
            print i, bill_n_tip
            raw_input("Press Enter to continue...")
            self.bills_n_tips.append(bill_n_tip)

    def total_tip_out(self):
        # return sum(self.get_tips(self.bills_n_tips))
        return sum(self.get_tips())

if __name__ == "__main__":
    tot = TipOutTracker(0.18)
    tot.add_bill(58.90, 0.15)
    tot.add_bill(31.58)
    # print tot.total_tip_out()
    tot.add_bill(81.44, 0.20)
    # print len(tot)
    tot2 = tot
    tot+tot2
    tot.bills_n_tips
