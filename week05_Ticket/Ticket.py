from datetime import datetime

class Ticket:
    def __init__(self, num : str, cost : int, legal_to : datetime):
        self._num = num
        self.__cost = cost
        self.legal_to = legal_to

    def __str__(self):
        return str(self._num) + " " + str(self.__cost) + " " + str(self.legal_to)

    def off_a_trip(self):
        print(f"Билет {self._num} использован!")

    def info(self):
        return f"Билет {self._num}: стоимость {self.__cost}, действителен до {self.legal_to}."

class TicketToRide(Ticket):
    def __init__(self, num, cost, legal_to):
        super().__init__(num, cost, legal_to)

class UnlimitedTicket(Ticket):
    def __init__(self, num, cost):
        super().__init__(num, cost, None)

    def off_a_trip(self):
        print(f"Безлимитный билет {self._num} не требует списания поездок.")

class LimitedTicket(Ticket):
    def __init__(self, num, cost, legal_to, border : datetime):
        super().__init__(num, cost, legal_to)
        self.border = border

    def off_a_trip(self, time_now : datetime):
        if time_now > self.border:
            print(f"Билет {self._num} истёк!")
        else:
            print(f"Билет {self._num} использован! Оставшееся время: {self.border - time_now}.")

class LimitedTicketWithRides(LimitedTicket):
    def __init__(self, num, cost, legal_to, border, rides : int):
        super().__init__(num, cost, legal_to, None)
        self.rides = rides

    def off_a_trip(self):
        if self.rides > 0:
            self.rides -= 1
            print(f"Поездка списана с билета {self._num}. Осталось поездок: {self.rides}.")
        else:
            print(f"Билет {self._num} исчерпан, поездки закончились!")