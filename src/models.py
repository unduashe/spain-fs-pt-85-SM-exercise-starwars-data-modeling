import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
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
    password = Column(String(255), nullable=False)
    email = Column(String(250))
    phone_number = Column(Integer)
    favourites = relationship("favourites", back_populates="user")
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    race = Column(String(250))
    eye_colour = Column(String(50))
    height = Column(String(50))
    weight = Column(String(50))
    master = Column(String(250))
    disciple = Column(String(250))
    image = Column(String(500))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    weather = Column(String(100))
    rotation_period = Column(Float)
    orbital_period = Column(Float)
    gravity = Column(Float)
    population = Column(Integer)
    terrain = Column(String(100))
    image = Column(String(500))

class Favourites(Base):
    __tablename__ = 'Favourites'
    favourite_id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    user = relationship("User", back_populates="favourites")
    character = relationship("Character")
    planet = relationship("Planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
