class Company():
    """
    name -          str holding the name of the company
    industry_type - str holding what industry the company belongs to
    num_employees - int holding the number of employees the company has
    total_revenue - float holding the total revenue of the company
    """
    def __init__(self, name, industry_type, num_employees, total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self, cost):
        self.total_revenue -= cost

    def gain_employees(self, new_employees):
        self.num_employees += len(new_employees)
