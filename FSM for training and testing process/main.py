from general_FSM_model import StateMachine

def start_transitions(): #transition can be performed from start state
    print("you are in start State ...... :")
    txt = raw_input("Input the new state (training OR testing only): ")
    return txt

def training_transitions():  #transition can be performed from training state
    print("you are in training State ...... :")
    # doing training here
    txt = raw_input("Input the new state (end OR testing only): ")
    return txt


def testing_transitions():  #transition can be performed from testing state
    print("you are in testing State ...... :")
    # doing testing here
    txt = raw_input("Input the new state (end OR training only): ")
    return txt


if __name__== "__main__":
    m = StateMachine()
    m.add_state("Start", start_transitions)
    m.add_state("Testing", testing_transitions)
    m.add_state("Training", training_transitions)
    m.add_state("End", None, end_state=1)
    m.set_start("Start")
    m.run()
