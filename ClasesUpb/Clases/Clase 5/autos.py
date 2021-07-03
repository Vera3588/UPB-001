## sin ciclos

autos = {'autos':{
        1:{'marca':'Tesla',
           'modelos':{
               1:'Model S',
               2:'Model E',
               3:'Model X',
               4:'Model Y',
               }
           },
        2:{'marca':'Toyota',
           'modelos':{
               1:'Fortuner',
               2:'Prado',
               3:'Tundra',
               4:'Corola',
               }
           },
        3:{'marca':'Range Rover',
           'modelos':{
               1:'Evoque',
               2:'Defender',
               }
           },
        4:{'marca':'Mazda',
           'modelos':{
               1:'Mazda 3',
               2:'Mazda 2',
               3:'CX 30',
               }
           },
        5:{'marca':'Audi',
           'modelos':{
               1:'A7',
               2:'A5',
               3:'A3',
               }
           }
        }
}

def verificar_mayor(marca1, marca2, marca3, marca4, marca5):
    if (marca1 >= marca2 and marca1 >= marca3 and marca1 >= marca4 and marca1 >= marca5):
        print(autos['autos'][1]['marca'])
    elif (marca2 >= marca1 and marca2 >= marca3 and marca2 >= marca4 and marca2 >= marca5):
        print(autos['autos'][2]['marca'])
    elif (marca3 >= marca1 and marca3 >= marca2 and marca3 >= marca4 and marca3 >= marca5):
        print(autos['autos'][3]['marca'])
    elif (marca4 >= marca2 and marca4 >= marca3 and marca4 >= marca1 and marca4 >= marca5):
        print(autos['autos'][4]['marca'])
    elif (marca5 >= marca2 and marca5 >= marca3 and marca5 >= marca4 and marca5 >= marca1):
        print(autos['autos'][5]['marca'])

marca1 = len(autos['autos'][1]['modelos'])
marca2 = len(autos['autos'][2]['modelos'])
marca3 = len(autos['autos'][3]['modelos'])
marca4 = len(autos['autos'][4]['modelos'])
marca5 = len(autos['autos'][5]['modelos'])

verificar_mayor(marca1, marca2, marca3, marca4, marca5)


    
