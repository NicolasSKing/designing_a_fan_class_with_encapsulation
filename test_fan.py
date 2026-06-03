from fan_class import Fan

first_fan = Fan()
first_fan.set_speed(Fan.FAST)
first_fan.set_radius(10)
first_fan.set_color("yellow")
first_fan.set_on(True)

second_fan = Fan()
second_fan.set_speed(Fan.MEDIUM)
second_fan.set_radius(5)
second_fan.set_color("blue")
second_fan.set_on(False)

print("Fan 1")
print("Speed:", first_fan.get_speed())
print("Radius:", first_fan.get_radius())
print("Color:", first_fan.get_color())
print("On:", first_fan.get_on())

