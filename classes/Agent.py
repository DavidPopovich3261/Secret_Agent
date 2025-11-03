

class Agent:
    def __init__(self,code_name,clearance_level):
        self.code_name=code_name
        self._clearance_level=clearance_level


    def setter(self,clearance_level):
        if clearance_level>0 and clearance_level<11:
            self._clearance_level=clearance_level


    def getter(self):
        print(f"{self._clearance_level}")



    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}")