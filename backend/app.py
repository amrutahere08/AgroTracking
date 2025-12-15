from flask import Flask, session
from flask_cors import CORS
from models import db, User, Crop, Field, Activity, Inventory, Revenue, Alert
from routes import api
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agrotracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS

# Initialize extensions
db.init_app(app)
CORS(app, supports_credentials=True, origins=['http://localhost:3000'])

# Register blueprints
app.register_blueprint(api)

def init_database():
    """Initialize database and create demo farmer account with realistic Indian agricultural data"""
    with app.app_context():
        db.create_all()
        
        # Create demo farmer account
        farmer = User.query.filter_by(username='farmer').first()
        if not farmer:
            farmer = User(
                username='farmer',
                email='farmer@agrotracker.com',
                role='user'
            )
            farmer.set_password('farmer123')
            db.session.add(farmer)
            db.session.commit()
        
        # Add realistic Indian agricultural sample data
        if Crop.query.count() == 0:
            print("Creating realistic Indian agricultural sample data...")
            
            # Indian Crops with INR values (realistic market prices)
            crops_data = [
                {'name': 'Rice (Basmati)', 'crop_type': 'Grain', 'status': 'growing', 'area': 8.5, 'yield_amount': 34.0, 'revenue': 425000},
                {'name': 'Wheat', 'crop_type': 'Grain', 'status': 'harvested', 'area': 6.2, 'yield_amount': 24.8, 'revenue': 372000},
                {'name': 'Cotton', 'crop_type': 'Cash Crop', 'status': 'growing', 'area': 5.0, 'yield_amount': 12.5, 'revenue': 625000},
                {'name': 'Sugarcane', 'crop_type': 'Cash Crop', 'status': 'growing', 'area': 4.3, 'yield_amount': 301.0, 'revenue': 903000},
                {'name': 'Tomatoes', 'crop_type': 'Vegetable', 'status': 'growing', 'area': 2.5, 'yield_amount': 50.0, 'revenue': 250000},
                {'name': 'Onions', 'crop_type': 'Vegetable', 'status': 'planted', 'area': 3.0, 'yield_amount': 0, 'revenue': 0},
                {'name': 'Soybeans', 'crop_type': 'Legume', 'status': 'harvested', 'area': 7.0, 'yield_amount': 21.0, 'revenue': 630000},
            ]
            
            for i, crop_data in enumerate(crops_data):
                planting_date = datetime.now() - timedelta(days=120 - i*15)
                harvest_date = datetime.now() - timedelta(days=10) if crop_data['status'] == 'harvested' else None
                
                crop = Crop(
                    name=crop_data['name'],
                    crop_type=crop_data['crop_type'],
                    planting_date=planting_date.date(),
                    harvest_date=harvest_date,
                    status=crop_data['status'],
                    area=crop_data['area'],
                    yield_amount=crop_data['yield_amount'],
                    revenue=crop_data['revenue'],
                    user_id=farmer.id
                )
                db.session.add(crop)
            
            # Indian Fields with local naming
            fields_data = [
                {'name': 'Khet 1 (Main Field)', 'size': 15.0, 'location': 'Near Village Road', 'soil_type': 'Alluvial'},
                {'name': 'Khet 2 (North)', 'size': 10.5, 'location': 'North Section', 'soil_type': 'Black Soil'},
                {'name': 'Khet 3 (South)', 'size': 8.0, 'location': 'Near Canal', 'soil_type': 'Red Soil'},
                {'name': 'Khet 4 (East)', 'size': 6.5, 'location': 'East Boundary', 'soil_type': 'Laterite'},
            ]
            
            for field_data in fields_data:
                field = Field(
                    name=field_data['name'],
                    size=field_data['size'],
                    location=field_data['location'],
                    soil_type=field_data['soil_type'],
                    user_id=farmer.id
                )
                db.session.add(field)
            
            db.session.commit()
            fields = Field.query.filter_by(user_id=farmer.id).all()
            
            # Farming Activities
            activities_data = [
                {'type': 'Planting', 'description': 'Sowed Basmati rice seeds', 'days_ago': 110},
                {'type': 'Irrigation', 'description': 'Flood irrigation for rice fields', 'days_ago': 5},
                {'type': 'Fertilizing', 'description': 'Applied DAP and Urea fertilizer', 'days_ago': 25},
                {'type': 'Harvesting', 'description': 'Wheat harvest completed', 'days_ago': 10},
                {'type': 'Pest Control', 'description': 'Sprayed organic pesticide on cotton', 'days_ago': 18},
                {'type': 'Weeding', 'description': 'Manual weeding in vegetable section', 'days_ago': 7},
            ]
            
            for i, activity_data in enumerate(activities_data):
                activity = Activity(
                    activity_type=activity_data['type'],
                    date=(datetime.now() - timedelta(days=activity_data['days_ago'])).date(),
                    description=activity_data['description'],
                    field_id=fields[i % len(fields)].id,
                    user_id=farmer.id
                )
                db.session.add(activity)
            
            # Indian Agricultural Inventory
            inventory_data = [
                {'item': 'Basmati Rice Seeds', 'quantity': 125, 'unit': 'kg', 'category': 'Seeds'},
                {'item': 'DAP Fertilizer', 'quantity': 500, 'unit': 'kg', 'category': 'Fertilizer'},
                {'item': 'Urea', 'quantity': 300, 'unit': 'kg', 'category': 'Fertilizer'},
                {'item': 'Organic Pesticide', 'quantity': 25, 'unit': 'liters', 'category': 'Pesticide'},
                {'item': 'Drip Irrigation Pipes', 'quantity': 200, 'unit': 'meters', 'category': 'Equipment'},
                {'item': 'Cotton Seeds (BT)', 'quantity': 50, 'unit': 'packets', 'category': 'Seeds'},
            ]
            
            for inv_data in inventory_data:
                inventory = Inventory(
                    item_name=inv_data['item'],
                    quantity=inv_data['quantity'],
                    unit=inv_data['unit'],
                    category=inv_data['category'],
                    user_id=farmer.id
                )
                db.session.add(inventory)
            
            # Revenue data in INR (Indian Rupees)
            revenue_data = [
                {'month': 'Jan', 'revenue': 485000, 'profit': 145000},
                {'month': 'Feb', 'revenue': 625000, 'profit': 225000},
                {'month': 'Mar', 'revenue': 780000, 'profit': 312000},
                {'month': 'Apr', 'revenue': 920000, 'profit': 385000},
            ]
            
            for rev_data in revenue_data:
                revenue = Revenue(
                    month=rev_data['month'],
                    revenue_amount=rev_data['revenue'],
                    profit_amount=rev_data['profit'],
                    year=2025,
                    user_id=farmer.id
                )
                db.session.add(revenue)
            
            # Alerts relevant to Indian farming
            alerts_data = [
                {'title': 'Monsoon Alert', 'message': 'Heavy rainfall expected in next 48 hours. Ensure proper drainage.', 'priority': 'high', 'type': 'weather', 'field': None},
                {'title': 'Wheat Ready for Harvest', 'message': 'Wheat in Khet 2 has reached maturity. Begin harvesting.', 'priority': 'medium', 'type': 'harvest', 'field': 'Khet 2 (North)'},
                {'title': 'Irrigation Needed', 'message': 'Rice fields require irrigation. Soil moisture below 60%.', 'priority': 'high', 'type': 'irrigation', 'field': 'Khet 1 (Main Field)'},
            ]
            
            for alert_data in alerts_data:
                alert = Alert(
                    title=alert_data['title'],
                    message=alert_data['message'],
                    priority=alert_data['priority'],
                    alert_type=alert_data['type'],
                    field_name=alert_data['field'],
                    user_id=farmer.id
                )
                db.session.add(alert)
            
            db.session.commit()
            print("✅ Indian agricultural sample data created!")
        
        print("\n" + "="*60)
        print("Database initialized successfully!")
        print("="*60)
        print("Login Credentials:")
        print("  Username: farmer")
        print("  Password: farmer123")
        print("\nSample Data Loaded:")
        print("  • 7 Indian crops (Rice, Wheat, Cotton, Sugarcane, etc.)")
        print("  • 4 fields with local naming (Khet 1-4)")
        print("  • 6 farming activities")
        print("  • 6 inventory items")
        print("  • 4 months revenue data (in ₹ INR)")
        print("  • 3 alerts")
        print("="*60 + "\n")

@app.route('/')
def index():
    return {'message': 'AgroTracker API is running', 'status': 'success'}

@app.route('/api/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    init_database()
    print("\n" + "="*50)
    print("AgroTracker Backend Server")
    print("="*50)
    print("Server running at: http://localhost:5000")
    print("API endpoints available at: http://localhost:5000/api/")
    print("="*50 + "\n")
    app.run(debug=True, port=5000, host='0.0.0.0')
