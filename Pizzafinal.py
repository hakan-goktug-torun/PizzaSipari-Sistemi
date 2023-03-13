import csv
import datetime


class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        pass


class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik Pizza"

    def get_cost(self):
        return 20


class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"

    def get_cost(self):
        return 23


class Turk_Pizzasi(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizzasi"

    def get_cost(self):
        return 23


class Dominos_Pizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Dominos Pizza"

    def get_cost(self):
        return 40


class Decoration:
    def __init__(self):
        self.description = "Unknown Decoration"

    def get_description(self):
        return self.description

    def get_cost(self):
        pass


class Zeytin(Decoration):
    def __init__(self):
        super().__init__()
        self.description = "Zeytin"

    def get_cost(self):
        return 3


class Mantar(Decoration):
    def __init__(self):
        super().__init__()
        self.description = "Mantar"

    def get_cost(self):
        return 4


class Keci_Peyniri(Decoration):
    def __init__(self):
        super().__init__()
        self.description = "Keci Peyniri"

    def get_cost(self):
        return 5


class Et(Decoration):
    def __init__(self):
        super().__init__()
        self.description = "Et"

    def get_cost(self):
        return 7


class Sogan(Decoration):
    def __init__(self):
        super().__init__()
        self.description = "Sogan"

    def get_cost(self):
        return 2


class Misir(Decoration):
    def __init__(self):
        super().__init__()
        self.description = "misir"

    def get_cost(self):
        return 1


# Örnek kullanım
pizza1 = Klasik()
pizza2 = Margherita()
pizza3 = Turk_Pizzasi()
pizza4 = Dominos_Pizza()
sauce1 = Zeytin()
sauce2 = Mantar()
sauce3 = Keci_Peyniri()
sauce4 = Et()
sauce5 = Sogan()
sauce6 = Misir()

pizzaArr = [pizza1, pizza2, pizza3, pizza4]
sosArr = [sauce1, sauce2, sauce3, sauce4, sauce5, sauce6]

cost = 0

file = open("Menu", "r")
print(file.read())

pizzaSelector = eval(input("Pizza Seciniz: "))

while (pizzaSelector > 5):
    if (pizzaSelector > 5):
        pizzaSelector = eval(input("Gecerli Bir Pizza Numarasi Giriniz: "))

sosSelector = eval(input("Sos Seciniz: "))

while (sosSelector > 17 or sosSelector < 11):
    if (sosSelector > 17 or sosSelector < 11):
        sosSelector = eval(input("Gecerli Bir Sos Numarasi Giriniz: "))

total_cost = pizzaArr[pizzaSelector - 1].get_cost() + sosArr[sosSelector - 11].get_cost()
print("Sos ile birlikte pizzanin toplam ücreti:", total_cost)

# Kullanıcı bilgilerinin alındığı kısım
name = input("Lütfen adinizi ve soyadinizi giriniz: ")

while True:
    tc_id_number = input("Lütfen T.C. kimlik numarasi giriniz: ")
    if len(tc_id_number) != 11:
        print("Geçersiz T.C. kimlik numarasi. Lütfen tam olarak 11 haneli giriniz.")
    elif not tc_id_number.isdigit():
        print("Geçersiz T.C. kimlik numarasi. Lütfen sadece rakam giriniz.")
    else:
        break
print("TC kimlik numarasi geçerlidir.")

while True:
    credit_card_number = input("Lütfen kredi karti numarasini giriniz: ")
    if len(credit_card_number) != 16:
        print("Geçersiz kredi karti numarasi. Lütfen tam olarak 16 haneli giriniz.")
    elif not tc_id_number.isdigit():
        print("Geçersiz kredi karti numarasi. Lütfen sadece rakam giriniz.")
    else:
        break
print("Kredi karti numarasi geçerlidir.")

credit_card_password = input("Lütfen kredi karti şifresini giriniz: ")

order_description = pizzaArr[pizzaSelector - 1].get_description() + " with " + sosArr[sosSelector - 11].get_description()

# Sipariş Zamanı
order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Tabloyu oluşturun ve verileri ekleyin
with open("Orders_Database.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(
        ["Pizza", "Username", "TR ID", "Credit Card Number", "Order Description", "Order Time", "Credit Card Password"])
    writer.writerow([order_description, name, tc_id_number, credit_card_number, order_description, order_time,credit_card_password])

