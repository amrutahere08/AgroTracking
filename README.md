# 🌾 AgroTracker - Smart Agricultural Management System

[![React](https://img.shields.io/badge/React-19.2.3-61DAFB?logo=react)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?logo=flask)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive web-based agricultural management system designed to help farmers track crops, manage fields, monitor inventory, and analyze farm performance with real-time data visualization and analytics.

![AgroTracker Dashboard](https://img.shields.io/badge/Status-Production%20Ready-success)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)


---

## ✨ Features

### 🌱 Crop Management
- **Comprehensive Crop Tracking**: Monitor multiple crops with detailed information including planting dates, harvest schedules, and growth status
- **Crop Performance Analytics**: Track yield amounts, area coverage, and revenue generation per crop
- **Status Monitoring**: Real-time status updates (Planted, Growing, Harvested)
- **Indian Agricultural Focus**: Pre-configured with popular Indian crops (Basmati Rice, Wheat, Cotton, Sugarcane, etc.)

### 🏞️ Field Management
- **Multi-Field Support**: Manage multiple fields (Khet) with individual tracking
- **Soil Type Classification**: Track soil types (Alluvial, Black Soil, Red Soil, Laterite)
- **Location Mapping**: GPS-based field location tracking
- **Size Monitoring**: Accurate field size measurement in acres

### 📊 Advanced Analytics Dashboard
- **Revenue & Profit Trends**: Interactive charts showing monthly revenue and profit trends
- **Crop Performance Visualization**: Visual representation of crop yields and performance metrics
- **Real-time Statistics**: Live updates on total crops, fields, activities, and inventory
- **Data-Driven Insights**: Make informed decisions based on historical data

### 📦 Inventory Management
- **Resource Tracking**: Monitor seeds, fertilizers, pesticides, and equipment
- **Quantity Management**: Track stock levels with unit measurements
- **Category Organization**: Organized inventory by categories (Seeds, Fertilizer, Pesticide, Equipment)
- **Low Stock Alerts**: Automated notifications for inventory replenishment

### 📅 Activity Logging
- **Comprehensive Activity Tracking**: Log all farming activities (Planting, Irrigation, Fertilizing, Harvesting, Pest Control, Weeding)
- **Date-based Records**: Maintain detailed historical records of all farm operations
- **Field-specific Activities**: Link activities to specific fields for better organization
- **Activity Timeline**: Visual timeline of all farming operations

### 🚨 Smart Alert System
- **Priority-based Alerts**: High, Medium, and Low priority notifications
- **Weather Alerts**: Monsoon warnings and weather-related notifications
- **Harvest Reminders**: Automated alerts when crops are ready for harvest
- **Irrigation Notifications**: Soil moisture-based irrigation reminders
- **Custom Alert Types**: Weather, Harvest, Irrigation, and more

### 🌤️ Weather Integration
- **Current Weather**: Real-time temperature and humidity data
- **Weather Forecast**: 3-day weather predictions
- **Farming Recommendations**: Weather-based farming suggestions

### 👥 User Management
- **Role-based Access Control**: Separate Admin and User (Farmer) roles
- **Secure Authentication**: Password hashing with Werkzeug security
- **Session Management**: Secure session handling with Flask
- **Multi-user Support**: Support for multiple farmers with isolated data

### 💰 Financial Tracking
- **Revenue Monitoring**: Track monthly revenue in Indian Rupees (₹)
- **Profit Analysis**: Calculate and visualize profit margins
- **Yearly Comparisons**: Compare financial performance across years
- **Export Reports**: Generate financial reports for accounting

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 19.2.3
- **UI/UX**: Custom CSS with gradient themes and responsive design
- **State Management**: React Hooks (useState, useEffect)
- **HTTP Client**: Fetch API
- **Testing**: React Testing Library, Jest

### Backend
- **Framework**: Flask 3.0.0 (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Werkzeug password hashing
- **CORS**: Flask-CORS for cross-origin requests
- **Session Management**: Flask sessions with secure cookies

### Database Schema
- **Users**: User authentication and role management
- **Crops**: Crop information and tracking
- **Fields**: Field details and specifications
- **Activities**: Farming activity logs
- **Inventory**: Resource and inventory management
- **Revenue**: Financial tracking and analytics
- **Alerts**: Notification and alert system

### Development Tools
- **Version Control**: Git
- **Package Managers**: npm (frontend), pip (backend)
- **API Testing**: Postman/Thunder Client compatible
- **Development Server**: Flask development server, React development server

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Client Layer (Browser)                   │
│                    React Frontend (Port 3000)                │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            │ HTTP/HTTPS
                            │ REST API Calls
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                    Application Layer                         │
│                 Flask Backend (Port 5000)                    │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Routes (API Endpoints)                              │  │
│  │  - Authentication (/api/login, /api/logout)          │  │
│  │  - Crops (/api/crops)                                │  │
│  │  - Fields (/api/fields)                              │  │
│  │  - Activities (/api/activities)                      │  │
│  │  - Inventory (/api/inventory)                        │  │
│  │  - Analytics (/api/analytics)                        │  │
│  │  - Alerts (/api/alerts)                              │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            │ SQLAlchemy ORM
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                      Data Layer                              │
│                   SQLite Database                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Tables: users, crops, fields, activities,           │  │
│  │          inventory, revenue, alerts                  │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📥 Installation

### Prerequisites
- **Python**: 3.8 or higher
- **Node.js**: 14.0 or higher
- **npm**: 6.0 or higher
- **Git**: For cloning the repository

### Step 1: Clone the Repository
```bash
git clone https://github.com/amrutahere08/AgroTracking.git
cd AgroTracking
```

### Step 2: Backend Setup

1. **Navigate to backend directory**:
```bash
cd backend
```

2. **Create a virtual environment** (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

4. **Initialize the database**:
The database will be automatically initialized when you first run the application. It includes sample Indian agricultural data.

### Step 3: Frontend Setup

1. **Navigate to frontend directory**:
```bash
cd ../frontend
```

2. **Install Node.js dependencies**:
```bash
npm install
```

---

## 🚀 Usage

### Starting the Application

#### 1. Start the Backend Server

```bash
# From the backend directory
cd backend
python app.py
```

The backend server will start at: `http://localhost:5000`

You should see:
```
==================================================
AgroTracker Backend Server
==================================================
Server running at: http://localhost:5000
API endpoints available at: http://localhost:5000/api/
==================================================
```

#### 2. Start the Frontend Development Server

Open a new terminal window:

```bash
# From the frontend directory
cd frontend
npm start
```

The React app will automatically open at: `http://localhost:3000`

### Default Login Credentials

**Demo Farmer Account:**
- **Username**: `farmer`
- **Password**: `farmer123`

### Sample Data Included

The application comes pre-loaded with realistic Indian agricultural data:
- ✅ 7 Indian crops (Rice, Wheat, Cotton, Sugarcane, Tomatoes, Onions, Soybeans)
- ✅ 4 fields with local naming (Khet 1-4)
- ✅ 6 farming activities
- ✅ 6 inventory items
- ✅ 4 months of revenue data (in ₹ INR)
- ✅ 3 active alerts

---

## 📡 API Documentation

### Authentication Endpoints

#### Login
```http
POST /api/login
Content-Type: application/json

{
  "username": "farmer",
  "password": "farmer123"
}
```

#### Logout
```http
POST /api/logout
```

#### Get Current User
```http
GET /api/current-user
```

### Crop Endpoints

#### Get All Crops
```http
GET /api/crops
```

#### Create New Crop
```http
POST /api/crops
Content-Type: application/json

{
  "name": "Wheat",
  "crop_type": "Grain",
  "planting_date": "2025-01-15",
  "harvest_date": "2025-05-20",
  "status": "planted"
}
```

#### Update Crop
```http
PUT /api/crops/{crop_id}
```

#### Delete Crop
```http
DELETE /api/crops/{crop_id}
```

### Field Endpoints

#### Get All Fields
```http
GET /api/fields
```

#### Create New Field
```http
POST /api/fields
Content-Type: application/json

{
  "name": "Khet 5",
  "size": 10.5,
  "location": "North Section",
  "soil_type": "Alluvial"
}
```

### Activity Endpoints

#### Get All Activities
```http
GET /api/activities
```

#### Create New Activity
```http
POST /api/activities
Content-Type: application/json

{
  "activity_type": "Irrigation",
  "date": "2025-01-20",
  "description": "Flood irrigation",
  "field_id": 1
}
```

### Inventory Endpoints

#### Get Inventory
```http
GET /api/inventory
```

#### Add Inventory Item
```http
POST /api/inventory
Content-Type: application/json

{
  "item_name": "Basmati Seeds",
  "quantity": 100,
  "unit": "kg",
  "category": "Seeds"
}
```

### Analytics Endpoints

#### Get Dashboard Analytics
```http
GET /api/analytics
```

#### Get Revenue Data
```http
GET /api/revenue
```

#### Get Crop Performance
```http
GET /api/crop-performance
```

### Alert Endpoints

#### Get All Alerts
```http
GET /api/alerts
```

#### Create Alert
```http
POST /api/alerts
```

#### Mark Alert as Read
```http
PUT /api/alerts/{alert_id}
```

### Weather Endpoint

#### Get Weather Data
```http
GET /api/weather
```

---

## 📸 Screenshots

### Login Page
Modern gradient-themed login interface with secure authentication.

### User Dashboard
Comprehensive dashboard with real-time statistics, recent activities, and quick access to all features.

### Admin Dashboard
Advanced analytics with revenue trends, crop performance charts, and system-wide management.

### Crop Management
Detailed crop tracking with status indicators, yield monitoring, and revenue tracking.

### Field Management
Multi-field management with soil type classification and location tracking.

### Inventory System
Resource management with category-based organization and quantity tracking.

### Alert System
Priority-based notification system with weather alerts and harvest reminders.

---

## 📁 Project Structure

```
AgroTrackingProject/
│
├── backend/                      # Flask Backend
│   ├── app.py                   # Main application file
│   ├── models.py                # Database models (SQLAlchemy)
│   ├── routes.py                # API routes and endpoints
│   ├── requirements.txt         # Python dependencies
│   └── instance/
│       └── agrotracker.db       # SQLite database (auto-generated)
│
├── frontend/                     # React Frontend
│   ├── public/                  # Static files
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/          # React components
│   │   │   ├── Homepage.js      # Landing page
│   │   │   ├── Login.js         # Login component
│   │   │   ├── Dashboard.js     # Main dashboard
│   │   │   ├── UserDashboard.js # Farmer dashboard
│   │   │   └── AdminDashboard.js # Admin dashboard
│   │   ├── App.js               # Main App component
│   │   ├── App.css              # Global styles
│   │   ├── index.js             # Entry point
│   │   └── index.css            # Base styles
│   ├── package.json             # Node.js dependencies
│   └── README.md                # Frontend documentation
│
├── README.md                     # This file
└── .gitignore                   # Git ignore rules
```


## 👨‍💻 Author

**Amruta Hegde**

- GitHub: [@amrutahere08](https://github.com/amrutahere08)
- Repository: [AgroTracking](https://github.com/amrutahere08/AgroTracking)

---

## 🙏 Acknowledgments

- **React Team** for the amazing frontend framework
- **Flask Team** for the lightweight and powerful backend framework
- **SQLAlchemy** for the excellent ORM
- **Indian Agricultural Community** for inspiration and real-world use cases


## 🔮 Future Enhancements

- [ ] Mobile application (React Native)
- [ ] Real-time weather API integration
- [ ] IoT sensor integration for soil moisture and temperature
- [ ] Machine learning for crop yield prediction
- [ ] Multi-language support (Hindi, Marathi, Tamil, etc.)
- [ ] Export data to PDF/Excel
- [ ] SMS/Email notifications for alerts
- [ ] Marketplace integration for crop selling
- [ ] Government scheme recommendations
- [ ] Satellite imagery integration

---

## 📊 Project Status

![Status](https://img.shields.io/badge/Status-Active-success)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-green)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)



---

<div align="center">

### ⭐ Star this repository if you find it helpful!

Made with ❤️ for Indian Farmers

</div>
