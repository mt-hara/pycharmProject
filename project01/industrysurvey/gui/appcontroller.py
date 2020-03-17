
class AppController():
    def __init__(self, master, model, view):
        self.master = master
        self.model = model
        self.view = view
        self.view.register(self)