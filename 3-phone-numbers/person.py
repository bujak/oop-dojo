class Person():
    _name = []
    _phone_number = []
    _list = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = self.normalize_phone_number(phone_number)
        self._name = name
        self._phone_number = phone_number


    def is_phone_number_matching(self, input_phone_number):
        if input_phone_number == self.phone_number:
            return True
        return False

    def get_name(self):
        return self.name

    @staticmethod
    def normalize_phone_number(phone_number):
        # "".join(chars for chars in phone_number if chars.isdigit()] < - this cuts all non digits characters
        phone_number = phone_number.replace(' ', '').replace('-','')
        return phone_number


if __name__ == '__main__':
    person = Person('aaa', '524245245')
    print(person.__dict__)
