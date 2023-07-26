from user import User


class PrintData:
    def __str__(self):
        pass

    def print_dict(self, dict):
        if isinstance(dict[0], User):
            for key, value in dict.items():
                print(key, value)

    def print_array(self, array):
        for item in array:
            if isinstance(item, User):
                for item in array:
                    print(item.id, item.name, item.email)
                return

    def print_user(self, user):
        print(user.id, user.name, user.email)

    def print_data(self, data):
        if isinstance(data, User):
            self.print_user(data)
        elif isinstance(data, dict):
            self.print_dict(data)
        elif isinstance(data, list):
            self.print_array(data)
        else:
            print(data)
