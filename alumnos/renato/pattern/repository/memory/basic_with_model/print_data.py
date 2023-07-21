from user import User


class PrintData:
    def __str__(self):
        pass

    def print_dict(self, dict):
        for key, value in dict.items():
            print(key, value)

    def print_array(self, array):
        for item in array:
            if isinstance(item, User):
                print(item.id, item.name, item.email)
            else:
                print(item)

    def print_data(self, data):
        if isinstance(data, dict):
            self.print_dict(data)
        elif isinstance(data, list):
            self.print_array(data)
        else:
            print(data)
