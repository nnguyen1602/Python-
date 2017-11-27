## general FSM in python
class StateMachine:

    def __init__(self):
        self.handlers = {}              # a dict: link the current state name with
                                        # the correct transition function for this state
        self.startState = None          # remember start state name
        self.endStates = []             # remember end state name
        self.currentState = None

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler   # load the handlers element:(state_name:transition_function)
        if end_state:
            self.endStates.append(name) # append the name of end state

    def set_start(self, name):
        self.startState = name.upper()
        self.currentState = name.upper()

    def run(self):
        handler = self.handlers[self.startState] # this function return the new state

        while True:
            newState = handler()
            print(newState)
            if newState.upper() in self.endStates:
                print("finish process by reaching " + newState + " State")
                break
            else:
                handler = self.handlers[newState.upper()]
