from Agent import Agent


class CyberAgent(Agent):
    def __init__(self,hacking , code_name, clearance_level):
        super().__init__(code_name, clearance_level)
        self.hacking=hacking


    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}hacking{self.hacking}")








