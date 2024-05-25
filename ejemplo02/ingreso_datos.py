from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


archivo_clubs = open('data/datos_clubs.txt', 'r', encoding='utf-8')
for linea in archivo_clubs:
    nombreClub, deporte, fundacion = linea.strip().split(';')
    club = Club(nombre=nombreClub, deporte=deporte, fundacion=int(fundacion))
    session.add(club)
    

archivo_clubs.close()

archivo_jugadores = open('data/datos_jugadores.txt', 'r', encoding='utf-8')
for linea in archivo_jugadores:
    nombre_club, posicion, dorsal, nombre = linea.strip().split(';')

    jugador = Jugador(nombre=nombre, dorsal=int(dorsal), posicion=posicion)

    jugador.club = session.query(Club).filter_by(nombre=nombre_club).one()
    session.add(jugador)
    
archivo_jugadores.close()
session.commit()









