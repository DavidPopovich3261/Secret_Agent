from Agent import Agent


class FieldAgent(Agent):
    def __init__(self,region,code_name,clearance_level):
        super().__init__(code_name,clearance_level)
        self.region=region

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}region{self.region}")
