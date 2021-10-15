from transport import *

boeing_777_300 = AirTransport(manufacturer='Boeing', model='777-300', weight=155500, seating_capacity=1397,
                              max_speed=945, consumption=FuelConsumption(tank_volume=181283), max_altitude=13100)

hyundai_hrcs2 = Train(manufacturer='Hyundai', model='HRCS2', weight=461000, seating_capacity=579,
                      max_speed=160, consumption=ElectricityConsumption(battery_type='Li-ion'), wagons=9)

drakkar_roskilde6 = WaterTransport(manufacturer='Vikings', model='Roskilde-6', weight=1000, seating_capacity=70,
                                   max_speed=28, consumption=MechanicalEnergyConsumption(), volume_submerged=1000)

scania_r730 = AutoTransport(manufacturer='Scania', model='R730', weight=7800, seating_capacity=1, max_speed=160,
                            consumption=FuelConsumption(tank_volume=300), wheels=4)

sugar = Horse(name='sugar', weight=500, seating_capacity=2, max_speed=88,
              consumption=OrganicEnergyConsumption(food_weight_rate=0.017))

print(boeing_777_300.get_info())
print(hyundai_hrcs2.get_info())
print(drakkar_roskilde6.get_info())
print(scania_r730.get_info())
print(sugar.get_info())

print(f'Boeing heavier than hyundai: {boeing_777_300 > hyundai_hrcs2}')

print('Air transport: ', end='')
boeing_777_300()
print('Train: ', end='')
hyundai_hrcs2()
print('Water transport: ', end='')
drakkar_roskilde6()
print('Auto transport: ', end='')
scania_r730()

print()

with scania_r730:
    print(f'Moves at a speed of {scania_r730.max_speed} km / h')

print()

print(f'Required amount of food per day: '
      f'{OrganicEnergyConsumption.calc_food_amount(sugar.weight, sugar.consumption.food_weight_rate)} kg')
print(Horse.mro())
sugar.move()
