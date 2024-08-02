from item import Item

from phone import Phone

Item1 = Item("Laptop", 50000, 20)
Item2 = Item("Phone", 20000, 15)
Item1.print_item()
Item2.print_item()

print(Item.pay_rate)
print(Item1.__dict__)  # All the attributes at the instance level
print(Item1.pay_rate)

# instantiating items through csv file using instantiate_from_csv() @classmethod
Item.instantiate_from_csv()  # Only can be available in class level
print(Item.all)

#  accessing instances in "all" vector
for instance in Item.all:
    print(instance)
print(Item.is_integer(7.0))
print(Item.is_integer(7))

phone1 = Phone("Oppo", 500, 5)
phone1.broken_phones = 2
print(phone1.broken_phones)

print(Item.all)
print(Phone.all)

