from abc import ABCMeta, abstractmethod

class IState(metaclass=ABCMeta):
    @abstractmethod
    def write_name(self,state_context):
        pass


class ConcreteState(IState):
    def __init__(self,text):
        self.text= text

    def write_name(self,state_context):
        pass

class StateA(ConcreteState):
    def __init__(self,text):
        super().__init__(text)

    def write_name(self,state_context):
    # def write_name(self, state_context, name):
        print(str.upper(self.text))


class StateB(ConcreteState):
    def __init__(self, text):
        super(StateB, self).__init__(text)

    def write_name(self,state_context):
        print(str.lower(self.text))

class StateC(ConcreteState):
    def __init__(self,text):
       super(StateC, self).__init__(text)

    def write_name(self,state_context):
        print(self.text)

class StateContext():
    def __init__(self,state_type):
        self.set_state(state_type)

    @property
    def mystate(self):
        return self.__mystate
    @mystate.setter
    def mystate(self, param):
        self.__mystate = param

    def set_state(self,new_state):
        self.mystate = new_state

    def write_name(self):
        self.mystate.write_name(self)


def set_concrete_State(param,text):
    if param == 1:
        return StateA(text)
    elif param == 2:
        return  StateB(text)
    else:
        return StateC(text)

if __name__=="__main__":
    text = "name is mt"
    sc = StateContext(set_concrete_State(1, text))
    sc2 = StateContext(set_concrete_State(2, text))
    sc.write_name()
    sc2.write_name()
    # statetype = StateA()
    #
    # sc = StateContext(StateA())
    # sc.write_name(text)
    # statetype= StateB()
    # sc2 = StateContext(statetype)
    # sc2.write_name(text)
