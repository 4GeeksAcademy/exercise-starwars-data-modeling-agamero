import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('homeworld.id'))
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    starships_id = Column(Integer, ForeignKey('starships.id'))
    url = Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False)


class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    MGLT = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250))
    consumables = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    pilots = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)

class Homeworld(Base):
    __tablename__ = 'homeworld'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    
class FavsCharacter(Base):
    __tablename__ = 'CharactersFavs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))

class FavsStarships(Base):
    __tablename__ = 'StarshipsFavs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    starships_id = Column(Integer, ForeignKey('starships.id'))

class FavsHomeworld(Base):
    __tablename__ = 'Homeworldsfavs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('homeworld.id'))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
