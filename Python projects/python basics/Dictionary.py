dictionary = {"name": "Alice", "age": 30, "city": "New York"}
print("Name:", dictionary["name"])

Benz = {"Model1": 500000, "Model2": 600000, "Model3": 700000}
Audi = {"ModelA": 550000, "ModelB": 650000, "ModelC": 750000}

Car_price = {"Brand1": Benz, "Brand2": Audi}

print("Price of Model2 from Brand1:", Car_price["Brand1"]["Model2"])
