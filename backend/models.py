from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='user')  # 'admin' or 'user'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    crops = db.relationship('Crop', backref='owner', lazy=True, cascade='all, delete-orphan')
    fields = db.relationship('Field', backref='owner', lazy=True, cascade='all, delete-orphan')
    activities = db.relationship('Activity', backref='owner', lazy=True, cascade='all, delete-orphan')
    inventory = db.relationship('Inventory', backref='owner', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        }


class Crop(db.Model):
    __tablename__ = 'crops'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    crop_type = db.Column(db.String(50), nullable=False)
    planting_date = db.Column(db.Date, nullable=False)
    harvest_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='planted')  # planted, growing, harvested
    area = db.Column(db.Float, default=0.0)  # in acres
    yield_amount = db.Column(db.Float, default=0.0)  # in tons
    revenue = db.Column(db.Float, default=0.0)  # in currency
    image_url = db.Column(db.String(500))  # path to crop image
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'crop_type': self.crop_type,
            'planting_date': self.planting_date.isoformat() if self.planting_date else None,
            'harvest_date': self.harvest_date.isoformat() if self.harvest_date else None,
            'status': self.status,
            'area': self.area,
            'yield_amount': self.yield_amount,
            'revenue': self.revenue,
            'image_url': self.image_url,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }


class Field(db.Model):
    __tablename__ = 'fields'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=False)  # in acres
    location = db.Column(db.String(200))
    soil_type = db.Column(db.String(50))
    image_url = db.Column(db.String(500))  # path to field image
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    activities = db.relationship('Activity', backref='field', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'size': self.size,
            'location': self.location,
            'soil_type': self.soil_type,
            'image_url': self.image_url,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }


class Activity(db.Model):
    __tablename__ = 'activities'
    
    id = db.Column(db.Integer, primary_key=True)
    activity_type = db.Column(db.String(50), nullable=False)  # planting, watering, fertilizing, etc.
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    field_id = db.Column(db.Integer, db.ForeignKey('fields.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'activity_type': self.activity_type,
            'date': self.date.isoformat() if self.date else None,
            'description': self.description,
            'field_id': self.field_id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }


class Inventory(db.Model):
    __tablename__ = 'inventory'
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False)  # kg, liters, bags, etc.
    category = db.Column(db.String(50))  # seeds, fertilizer, pesticide, tools, etc.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'quantity': self.quantity,
            'unit': self.unit,
            'category': self.category,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }


class Revenue(db.Model):
    __tablename__ = 'revenue'
    
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)  # e.g., "Jan", "Feb"
    revenue_amount = db.Column(db.Float, nullable=False)
    profit_amount = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'month': self.month,
            'revenue_amount': self.revenue_amount,
            'profit_amount': self.profit_amount,
            'year': self.year,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }


class Alert(db.Model):
    __tablename__ = 'alerts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), default='medium')  # low, medium, high
    alert_type = db.Column(db.String(50))  # harvest, moisture, weather, etc.
    field_name = db.Column(db.String(100))  # related field if applicable
    is_read = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'priority': self.priority,
            'alert_type': self.alert_type,
            'field_name': self.field_name,
            'is_read': self.is_read,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }
