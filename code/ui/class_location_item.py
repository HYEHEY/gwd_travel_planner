from PyQt5.QtWidgets import QWidget

from ui.ui_location_item import Ui_location_item

from class_location import Location


# from ui_location_item import Ui_location_item

class LocationItem(QWidget, Ui_location_item):
    def __init__(self, location_obj :Location, select_planner):
        super().__init__()
        self.setupUi(self)
        self.location_obj = location_obj
        self.name = location_obj.name
        self.address = location_obj.address
        self.category = location_obj.category
        self.set_text_location()
        self.select_planner = select_planner
        self.mouseDoubleClickEvent = lambda x:self.set_web_location()

    def set_text_location(self):
        self.label_name.setText(f"{self.name}")
        self.label_adress.setText(f"{self.address}")

    def set_web_location(self):
        self.select_planner.set_location_web_view(self.location_obj)





