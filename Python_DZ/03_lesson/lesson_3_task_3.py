from mailing import Mailing
from address import Address

to_address = Address(654987, "Новосибирск", "Ленина", 65, 210)
from_address = Address(896321, "Новосибирск", "Красный проспект", 55, 23)
track = "123458"
cost = "1602"

mailing = Mailing(to_address, from_address, cost, track)

print(mailing)
