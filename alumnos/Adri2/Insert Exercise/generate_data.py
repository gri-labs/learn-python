from faker import Faker


class GenerateData:
    def __init__(self):
        self.fake = Faker()

    def get_name(self):
        return self.fake.name()

    def get_address(self):
        return self.fake.address()

    def get_email(self):
        return self.fake.email()

    def get_phone_number(self):
        return self.fake.phone_number()

    def get_job(self):
        return self.fake.job()
