class Report:
    """
    A class to store and display evaluation metrics.
    """
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name, value):
        """
        Adds a metric to the report.
        """
        self.metrics[name] = value

    def display_report(self):
        """
        Displays the current report.
        """
        for name, value in self.metrics.items():
            print(f"{name}: {value}")

def create_report():
    """Creates a new instance of the Report class"""
    return Report()
