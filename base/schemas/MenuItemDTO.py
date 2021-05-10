import json
from typing import List


class MenuItemDTO:
    label: str
    routerLink: str
    url: str
    to: str
    item: []

    def __init__(self, label: str, url: str, item):
        super().__init__()
        self.label = label
        self.url = url
        self.routerLink = url
        self.to = url
        self.item = item
    
    def Clean():
        self.label = ""
        self.routerLink = ""
        self.url = ""
        self.to = ""
        self.item = []

    def to_json(self):
        return json.dumps(self.__dict__)
