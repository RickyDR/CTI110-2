#Your Name

#Date

#Assignment Name

#A brief description of the project

gas_mileage=float(input('gas mileage:'))

gas_cost=float(input('gas cost:'))

gas_20_miles=float((20*gas_cost)/gas_mileage)

gas_75_miles=float((gas_cost*75)/gas_mileage)

gas_500_miles=float((gas_cost*500)/gas_mileage)

print(f'{gas_20_miles:.2f} {gas_75_miles:.2f} {gas_500_miles}')
