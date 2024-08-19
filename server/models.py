from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData() #creates a meta data object

db = SQLAlchemy(metadata=metadata) #Initializes sqlalchemy with metadata

# Add models here 
# Define a model class by inheriting from db.model
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self): #provides a string representation of the model instance
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>" 

