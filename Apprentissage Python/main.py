# import specific object
import sys
from ecommerce.shopping.sales import calc_shipping, calc_tax
from ecommerce.shopping import sales

print(sales.__name__)
print(sales.__package__)
print(sales.__file__)
# import module as object

# print(sys.path)

sales.calc_shipping

calc_tax()
calc_shipping()
