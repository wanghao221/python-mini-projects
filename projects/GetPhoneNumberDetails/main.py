# pip install phonenumbers
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

# Enter Your Phone Number
a=input("Enter Phone Number: ")

# Number Parsing
ph_no=phonenumbers.parse(a)

# print(type(ph_no))
# print(ph_no)

# Location Of Number
print(geocoder.description_for_number(ph_no,"en"))

# Sim Name
print(carrier.name_for_number(ph_no,"en"))

# Timezone
print(timezone.time_zones_for_number(ph_no))
