devs = [{'cc': 1540, 'nombre': 'Miguel', 'salario': 2600000,'years':5},
        {'cc': 1556, 'nombre': 'Cristian', 'salario': 2500000,'years':2},
        {'cc': 2556, 'nombre': 'Juan Ignacio', 'salario': 2500000,'years':3},
        {'cc': 1340, 'nombre': 'Nicolas', 'salario': 2400000,'years':4},
        {'cc': 1526, 'nombre': 'Sendy', 'salario': 2400000,'years':5},
        {'cc': 2516, 'nombre': 'Santiago', 'salario': 2600000,'years':5},
        {'cc': 1547, 'nombre': 'David', 'salario': 2500000,'years':3},
        {'cc': 5556, 'nombre': 'Milton', 'salario': 2800000,'years':6},
        {'cc': 5586, 'nombre': 'Jinneth', 'salario': 2800000,'years':2},
        {'cc': 3556, 'nombre': 'Alejandro', 'salario': 2700000,'years':1}]
'''
i = 0
for dev in devs:
       if dev['salario'] > i:
         i = dev['salario']
for sal in devs:       
        if (sal['salario'] == i):
                print(f"cc: {sal['cc']} \nnombre: {sal['nombre']}")
'''
