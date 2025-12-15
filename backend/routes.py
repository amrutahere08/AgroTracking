from flask import Blueprint, request, jsonify, session
from models import db, User, Crop, Field, Activity, Inventory, Revenue, Alert
from datetime import datetime
from functools import wraps

api = Blueprint('api', __name__)

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required'}), 401
        user = User.query.get(session['user_id'])
        if not user or user.role != 'admin':
            return jsonify({'error': 'Admin access required'}), 403
        return f(*args, **kwargs)
    return decorated_function

# Authentication Routes
@api.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        session['user_id'] = user.id
        session['username'] = user.username
        session['role'] = user.role
        return jsonify({
            'message': 'Login successful',
            'user': user.to_dict()
        }), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401

@api.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200

@api.route('/api/current-user', methods=['GET'])
@login_required
def current_user():
    user = User.query.get(session['user_id'])
    return jsonify({'user': user.to_dict()}), 200

# Crop Routes
@api.route('/api/crops', methods=['GET'])
@login_required
def get_crops():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if user.role == 'admin':
        crops = Crop.query.all()
    else:
        crops = Crop.query.filter_by(user_id=user_id).all()
    
    return jsonify([crop.to_dict() for crop in crops]), 200

@api.route('/api/crops', methods=['POST'])
@login_required
def create_crop():
    data = request.get_json()
    
    crop = Crop(
        name=data['name'],
        crop_type=data['crop_type'],
        planting_date=datetime.fromisoformat(data['planting_date']),
        harvest_date=datetime.fromisoformat(data['harvest_date']) if data.get('harvest_date') else None,
        status=data.get('status', 'planted'),
        user_id=session['user_id']
    )
    
    db.session.add(crop)
    db.session.commit()
    
    return jsonify(crop.to_dict()), 201

@api.route('/api/crops/<int:crop_id>', methods=['PUT'])
@login_required
def update_crop(crop_id):
    crop = Crop.query.get_or_404(crop_id)
    
    # Check ownership or admin
    user = User.query.get(session['user_id'])
    if crop.user_id != session['user_id'] and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    crop.name = data.get('name', crop.name)
    crop.crop_type = data.get('crop_type', crop.crop_type)
    if data.get('planting_date'):
        crop.planting_date = datetime.fromisoformat(data['planting_date'])
    if data.get('harvest_date'):
        crop.harvest_date = datetime.fromisoformat(data['harvest_date'])
    crop.status = data.get('status', crop.status)
    
    db.session.commit()
    
    return jsonify(crop.to_dict()), 200

@api.route('/api/crops/<int:crop_id>', methods=['DELETE'])
@login_required
def delete_crop(crop_id):
    crop = Crop.query.get_or_404(crop_id)
    
    # Check ownership or admin
    user = User.query.get(session['user_id'])
    if crop.user_id != session['user_id'] and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(crop)
    db.session.commit()
    
    return jsonify({'message': 'Crop deleted'}), 200

# Field Routes
@api.route('/api/fields', methods=['GET'])
@login_required
def get_fields():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if user.role == 'admin':
        fields = Field.query.all()
    else:
        fields = Field.query.filter_by(user_id=user_id).all()
    
    return jsonify([field.to_dict() for field in fields]), 200

@api.route('/api/fields', methods=['POST'])
@login_required
def create_field():
    data = request.get_json()
    
    field = Field(
        name=data['name'],
        size=data['size'],
        location=data.get('location'),
        soil_type=data.get('soil_type'),
        user_id=session['user_id']
    )
    
    db.session.add(field)
    db.session.commit()
    
    return jsonify(field.to_dict()), 201

@api.route('/api/fields/<int:field_id>', methods=['PUT'])
@login_required
def update_field(field_id):
    field = Field.query.get_or_404(field_id)
    
    user = User.query.get(session['user_id'])
    if field.user_id != session['user_id'] and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    field.name = data.get('name', field.name)
    field.size = data.get('size', field.size)
    field.location = data.get('location', field.location)
    field.soil_type = data.get('soil_type', field.soil_type)
    
    db.session.commit()
    
    return jsonify(field.to_dict()), 200

@api.route('/api/fields/<int:field_id>', methods=['DELETE'])
@login_required
def delete_field(field_id):
    field = Field.query.get_or_404(field_id)
    
    user = User.query.get(session['user_id'])
    if field.user_id != session['user_id'] and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(field)
    db.session.commit()
    
    return jsonify({'message': 'Field deleted'}), 200

# Activity Routes
@api.route('/api/activities', methods=['GET'])
@login_required
def get_activities():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if user.role == 'admin':
        activities = Activity.query.all()
    else:
        activities = Activity.query.filter_by(user_id=user_id).all()
    
    return jsonify([activity.to_dict() for activity in activities]), 200

@api.route('/api/activities', methods=['POST'])
@login_required
def create_activity():
    data = request.get_json()
    
    activity = Activity(
        activity_type=data['activity_type'],
        date=datetime.fromisoformat(data['date']),
        description=data.get('description'),
        field_id=data['field_id'],
        user_id=session['user_id']
    )
    
    db.session.add(activity)
    db.session.commit()
    
    return jsonify(activity.to_dict()), 201

@api.route('/api/activities/<int:activity_id>', methods=['DELETE'])
@login_required
def delete_activity(activity_id):
    activity = Activity.query.get_or_404(activity_id)
    
    user = User.query.get(session['user_id'])
    if activity.user_id != session['user_id'] and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(activity)
    db.session.commit()
    
    return jsonify({'message': 'Activity deleted'}), 200

# Inventory Routes
@api.route('/api/inventory', methods=['GET'])
@login_required
def get_inventory():
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if user.role == 'admin':
        inventory = Inventory.query.all()
    else:
        inventory = Inventory.query.filter_by(user_id=user_id).all()
    
    return jsonify([item.to_dict() for item in inventory]), 200

@api.route('/api/inventory', methods=['POST'])
@login_required
def create_inventory():
    data = request.get_json()
    
    item = Inventory(
        item_name=data['item_name'],
        quantity=data['quantity'],
        unit=data['unit'],
        category=data.get('category'),
        user_id=session['user_id']
    )
    
    db.session.add(item)
    db.session.commit()
    
    return jsonify(item.to_dict()), 201

@api.route('/api/inventory/<int:item_id>', methods=['PUT'])
@login_required
def update_inventory(item_id):
    item = Inventory.query.get_or_404(item_id)
    
    user = User.query.get(session['user_id'])
    if item.user_id != session['user_id'] and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    item.item_name = data.get('item_name', item.item_name)
    item.quantity = data.get('quantity', item.quantity)
    item.unit = data.get('unit', item.unit)
    item.category = data.get('category', item.category)
    
    db.session.commit()
    
    return jsonify(item.to_dict()), 200

@api.route('/api/inventory/<int:item_id>', methods=['DELETE'])
@login_required
def delete_inventory(item_id):
    item = Inventory.query.get_or_404(item_id)
    
    user = User.query.get(session['user_id'])
    if item.user_id != session['user_id'] and user.role != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(item)
    db.session.commit()
    
    return jsonify({'message': 'Inventory item deleted'}), 200

# Weather Route (mock data for now)
@api.route('/api/weather', methods=['GET'])
@login_required
def get_weather():
    # Mock weather data
    weather_data = {
        'temperature': 25,
        'humidity': 65,
        'conditions': 'Partly Cloudy',
        'forecast': [
            {'day': 'Today', 'temp': 25, 'conditions': 'Partly Cloudy'},
            {'day': 'Tomorrow', 'temp': 27, 'conditions': 'Sunny'},
            {'day': 'Day 3', 'temp': 24, 'conditions': 'Rainy'}
        ]
    }
    return jsonify(weather_data), 200

# Analytics Route
@api.route('/api/analytics', methods=['GET'])
@login_required
def get_analytics():
    user_id = session['user_id']
    
    total_crops = Crop.query.filter_by(user_id=user_id).count()
    total_fields = Field.query.filter_by(user_id=user_id).count()
    total_activities = Activity.query.filter_by(user_id=user_id).count()
    total_inventory = Inventory.query.filter_by(user_id=user_id).count()
    
    return jsonify({
        'total_crops': total_crops,
        'total_fields': total_fields,
        'total_activities': total_activities,
        'total_inventory': total_inventory
    }), 200

# Revenue Routes
@api.route('/api/revenue', methods=['GET'])
@login_required
def get_revenue():
    user_id = session['user_id']
    revenue_data = Revenue.query.filter_by(user_id=user_id).all()
    
    # Return existing data from database
    if revenue_data:
        return jsonify([r.to_dict() for r in revenue_data]), 200
    
    # If no data, return empty array (data should be created during init_database)
    return jsonify([]), 200

@api.route('/api/revenue', methods=['POST'])
@login_required
def create_revenue():
    data = request.get_json()
    
    revenue = Revenue(
        month=data['month'],
        revenue_amount=data['revenue_amount'],
        profit_amount=data['profit_amount'],
        year=data.get('year', 2025),
        user_id=session['user_id']
    )
    
    db.session.add(revenue)
    db.session.commit()
    
    return jsonify(revenue.to_dict()), 201

# Crop Performance Route
@api.route('/api/crop-performance', methods=['GET'])
@login_required
def get_crop_performance():
    user_id = session['user_id']
    crops = Crop.query.filter_by(user_id=user_id).filter(Crop.yield_amount > 0).all()
    
    performance_data = []
    for crop in crops:
        if crop.area > 0:
            yield_percent = min(100, int((crop.yield_amount / crop.area) * 10))
        else:
            yield_percent = 0
        
        performance_data.append({
            'name': crop.name,
            'yield_percent': yield_percent,
            'area': crop.area,
            'revenue': crop.revenue
        })
    
    return jsonify(performance_data), 200

# Alerts Routes
@api.route('/api/alerts', methods=['GET'])
@login_required
def get_alerts():
    user_id = session['user_id']
    alerts = Alert.query.filter_by(user_id=user_id).order_by(Alert.created_at.desc()).all()
    return jsonify([alert.to_dict() for alert in alerts]), 200

@api.route('/api/alerts', methods=['POST'])
@login_required
def create_alert():
    data = request.get_json()
    
    alert = Alert(
        title=data['title'],
        message=data['message'],
        priority=data.get('priority', 'medium'),
        alert_type=data.get('alert_type'),
        field_name=data.get('field_name'),
        user_id=session['user_id']
    )
    
    db.session.add(alert)
    db.session.commit()
    
    return jsonify(alert.to_dict()), 201

@api.route('/api/alerts/<int:alert_id>', methods=['PUT'])
@login_required
def update_alert(alert_id):
    alert = Alert.query.get_or_404(alert_id)
    
    if alert.user_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    alert.is_read = data.get('is_read', alert.is_read)
    
    db.session.commit()
    
    return jsonify(alert.to_dict()), 200

@api.route('/api/alerts/<int:alert_id>', methods=['DELETE'])
@login_required
def delete_alert(alert_id):
    alert = Alert.query.get_or_404(alert_id)
    
    if alert.user_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(alert)
    db.session.commit()
    
    return jsonify({'message': 'Alert deleted'}), 200

