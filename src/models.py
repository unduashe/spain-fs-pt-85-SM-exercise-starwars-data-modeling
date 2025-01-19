import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(154), nullable=False)
    favourites = relationship("favourites", back_populates="user")
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    race = Column(String(250), nullable=False)
    eye_colour = Column(String(250))
    height = Column(String(250))
    weight = Column(String(250))
    master = Column(String(250))
    disciple = Column(String(250))
    image = Column(String(500))
    # parent = relationship("Parent", back_populates="children")


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(Integer)
    weather = Column(String(100))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    terrain = Column(String(250))
    image = Column(String(500))

class Favourites(Base):
    __tablename__ = 'Favourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favourite_id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    user_id = Column(Integer, ForeignKey("User.id"))
    user = relationship("User", back_populates="favourites")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
