from faker import Faker


class Helpers:

    @staticmethod
    def fake_data():
        faker = Faker()
        user_data = [faker.name(), faker.email(), faker.password()]
        return user_data
