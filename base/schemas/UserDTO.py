import json

class UserDTO:
    id: int
    name: str
    email: str

    def to_json(self):
        return json.dumps(self.__dict__)
