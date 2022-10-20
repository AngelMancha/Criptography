
class Person():
    def __init__(self, user, birthdate, degree,
                 subject, bank,
                 email, password):

        self.__user = user
        self.__birthdate = birthdate
        self.__degree = degree
        self.__subject = subject
        self.__bank = bank
        self.__email = email
        self.__password = password

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def birthdate(self):
        return self.__birthdate
    @birthdate.setter
    def birthdate(self, birthdate):
        self.__birthdate = birthdate

    @property
    def degree(self):
        return self.__degree

    @degree.setter
    def degree(self, degree):
        self.__degree = degree

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    @property
    def bank(self):
        return self.__bank

    @bank.setter
    def bank(self, bank):
        self.__bank = bank

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password