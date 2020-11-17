from microapp import Project

import os

from microapp import register_appclass, is_appclass_registered

class Paragate(Project):
    _name_ = "paragate"
    _version_ = "0.1.0"
    _description_ = "Python Computing Task Helper"
    _long_description_ = "Python Computing Task Helper"
    _author_ = "Youngsung Kim"
    _author_email_ = "youngsung.kim.act2@gmail.com"
    _url_ = "https://github.com/grnydawn/paragate"

    def __init__(self):
        self.add_argument("--suite", metavar="path", help="path to task suite")

    def perform(self, args):

        if args.suite:
            self.load_tasksuite(args.suite["_"])

        elif self.has_config("tasksuite"):
            self.load_tasksuite(self.get_config("tasksuite"))

        else:
            from paragate.builtins import suite
            for app in suite:
                if not is_appclass_registered(app):
                    register_appclass(app)

    def load_tasksuite(self, path):
        raise NotImplementedError("custom task suite is not supported yet.")

