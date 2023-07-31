import phonenumbers
from phonenumbers import carrier, geocoder, timezone

number = input("Enter Number with +__ : ")
phone = phonenumbers.parse(number)

time = timezone.time_zones_for_number(phone)
car = carrier.carrier_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print(time)
print(car)
print(reg)
print(phone)