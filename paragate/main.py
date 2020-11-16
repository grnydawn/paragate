from microapp import Project

class Paragate(Project):
    _name_ = "paragate"
    _version_ = "0.1.0"
    _description_ = "Python Computing Task Helper"
    _long_description_ = "Python Computing Task Helper"
    _author_ = "Youngsung Kim"
    _author_email_ = "youngsung.kim.act2@gmail.com"
    _url_ = "https://github.com/grnydawn/paragate"

    def __init__(self):
        self.add_argument("--test", help="test argument")
