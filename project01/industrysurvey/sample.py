# from abc import ABCMeta, abstractmethod
# import  sys
# import  time
#
# class State(metaclass=ABCMeta):
#     @abstractmethod
#     def handle(self):
#         pass
#
# class ConcreteState(State):
#     def __init__(self, state):
#         self.state = state
#
#     def getConcreateState(self):
#         return self.state
#
#
# class ConcreteStateBooting(ConcreteState):
#     def __init__(self, state):
#         print(state)
#         super(ConcreteStateBooting, self).__init__(state)
#
#     def handle(self, context):
#         print("*** パソコンは、起動中です")
#         context.setState(ConcreteStateRun("running"))
#
#
# class ConcreteStateRun(ConcreteState):
#     def __init__(self, state):
#         super(ConcreteStateRun, self).__init__(state)
#
#     def handle(self, context):
#         print("*** パソコンは、動作中です")
#
#
# class ConcreteStateShutDown(ConcreteState):
#     def __init__(self, state):
#         super(ConcreteStateShutDown, self).__init__(state)
#
#     def handle(self, context):
#         print("*** パソコンは、停止しています")
#
#
# class ConcreteStateRestart(ConcreteState):
#     def __init__(self, state):
#         super(ConcreteStateRestart, self).__init__(state)
#
#     def handle(self, context):
#         print("*** パソコンは、再起動をはじめます")
#         context.setState(ConcreteStateBooting("booting"))
#         context.handle()
#
# class Context(object):
#     def __init__(self, stateObj):
#         self.state = stateObj
#
#     def setState(self, obj):
#         self.state = obj
#
#     def handle(self):
#         self.state.handle(self)
#
#     def getState(self):
#         return self.state.getConcreateState()
#
# def setConcreteState(operation):
#     if operation == "start":
#         return ConcreteStateBooting("booting")
#     elif operation == "stop":
#         return ConcreteStateShutDown("shutdown")
#     elif operation == "restart":
#         return ConcreteStateRestart("restart")
#
# def startMain(initial_operation, change_operation):
#     obj = Context(setConcreteState(initial_operation))
#     print("### パソコンを、[{0}]します".format(initial_operation))
#     obj.handle()
#     print("### パソコンは、[{0}]の動作状態になりました".format(obj.getState()))
#     print("")
#
#     print("... sleep 5 second")
#     print("")
#     time.sleep(5)
#
#     obj.setState(setConcreteState(change_operation))
#     print("### パソコンを、[{0}]します".format(change_operation))
#     obj.handle()
#     print("### パソコンの動作状態は、[{0}]になりました".format(obj.getState()))
#
#
def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class_, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w, class_).__new__(class_, *args, **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w


@singleton
class MyClass():
    def __init__(self):
        pass
        self.main()
    def main(self):
        return("test")

class MyClass2(MyClass):
    def __init__(self):
        super().__init__()
        pass


if __name__ == "__main__":
    t = MyClass()
    t2= MyClass2()
    print(id(t))
    print(id(t2))
    # t = MyClass()

