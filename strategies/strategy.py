class Strategy:
    def __init__(self, data_path):
        self.data_path = data_path
        self.selected_funds = []

    def collect_data(self):
        raise NotImplementedError
    
    def suggest(self):
        raise NotImplementedError
    
    def run(self):
        self.collect_data()
        self.suggest()
