# Enhanced Admin Dashboard with Dynamic Features
admin_code = """import React, { useState, useEffect } from 'react';

function AdminDashboard({ user, onLogout }) {
  const [activeTab, setActiveTab] = useState('overview');
  const [crops, setCrops] = useState([]);
  const [fields, setFields] = useState([]);
  const [activities, setActivities] = useState([]);
  const [inventory, setInventory] = useState([]);
  const [analytics, setAnalytics] = useState({});
  const [weather, setWeather] = useState({});
  const [loading, setLoading] = useState(false);
  const [notification, setNotification] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const showNotification = (message, type = 'success') => {
    setNotification({ message, type });
    setTimeout(() => setNotification(null), 3000);
  };

  const loadData = async () => {
    setLoading(true);
    try {
      if (activeTab === 'overview') {
        const [analyticsRes, weatherRes] = await Promise.all([
          fetch('http://localhost:5000/api/analytics', { credentials: 'include' }),
          fetch('http://localhost:5000/api/weather', { credentials: 'include' })
        ]);
        setAnalytics(await analyticsRes.json());
        setWeather(await weatherRes.json());
      } else if (activeTab === 'crops') {
        const res = await fetch('http://localhost:5000/api/crops', { credentials: 'include' });
        setCrops(await res.json());
      } else if (activeTab === 'fields') {
        const res = await fetch('http://localhost:5000/api/fields', { credentials: 'include' });
        setFields(await res.json());
      } else if (activeTab === 'activities') {
        const res = await fetch('http://localhost:5000/api/activities', { credentials: 'include' });
        setActivities(await res.json());
      } else if (activeTab === 'inventory') {
        const res = await fetch('http://localhost:5000/api/inventory', { credentials: 'include' });
        setInventory(await res.json());
      }
    } catch (error) {
      showNotification('Error loading data', 'error');
    } finally {
      setLoading(false);
    }
  };

  const addCrop = async () => {
    const name = prompt('Crop name:');
    const cropType = prompt('Crop type (e.g., Wheat, Rice, Corn):');
    const plantingDate = prompt('Planting date (YYYY-MM-DD):');
    if (name && cropType && plantingDate) {
      try {
        await fetch('http://localhost:5000/api/crops', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ name, crop_type: cropType, planting_date: plantingDate })
        });
        showNotification('Crop added successfully!');
        loadData();
      } catch (error) {
        showNotification('Error adding crop', 'error');
      }
    }
  };

  const deleteCrop = async (id) => {
    if (window.confirm('Are you sure you want to delete this crop?')) {
      try {
        await fetch('http://localhost:5000/api/crops/' + id, { method: 'DELETE', credentials: 'include' });
        showNotification('Crop deleted successfully!');
        loadData();
      } catch (error) {
        showNotification('Error deleting crop', 'error');
      }
    }
  };

  const addField = async () => {
    const name = prompt('Field name:');
    const size = prompt('Size in acres:');
    const location = prompt('Location:');
    const soilType = prompt('Soil type (e.g., Clay, Sandy, Loam):');
    if (name && size) {
      try {
        await fetch('http://localhost:5000/api/fields', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ name, size: parseFloat(size), location, soil_type: soilType })
        });
        showNotification('Field added successfully!');
        loadData();
      } catch (error) {
        showNotification('Error adding field', 'error');
      }
    }
  };

  const deleteField = async (id) => {
    if (window.confirm('Are you sure you want to delete this field?')) {
      try {
        await fetch('http://localhost:5000/api/fields/' + id, { method: 'DELETE', credentials: 'include' });
        showNotification('Field deleted successfully!');
        loadData();
      } catch (error) {
        showNotification('Error deleting field', 'error');
      }
    }
  };

  const addActivity = async () => {
    if (fields.length === 0) {
      showNotification('Please add a field first', 'error');
      return;
    }
    const activityType = prompt('Activity type (e.g., Planting, Watering, Fertilizing, Harvesting):');
    const date = prompt('Date (YYYY-MM-DD):');
    const description = prompt('Description (optional):');
    const fieldList = fields.map(f => f.id + ': ' + f.name).join(', ');
    const fieldId = prompt('Field ID (' + fieldList + '):');
    if (activityType && date && fieldId) {
      try {
        await fetch('http://localhost:5000/api/activities', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ activity_type: activityType, date, description, field_id: parseInt(fieldId) })
        });
        showNotification('Activity logged successfully!');
        loadData();
      } catch (error) {
        showNotification('Error logging activity', 'error');
      }
    }
  };

  const deleteActivity = async (id) => {
    if (window.confirm('Are you sure you want to delete this activity?')) {
      try {
        await fetch('http://localhost:5000/api/activities/' + id, { method: 'DELETE', credentials: 'include' });
        showNotification('Activity deleted successfully!');
        loadData();
      } catch (error) {
        showNotification('Error deleting activity', 'error');
      }
    }
  };

  const addInventoryItem = async () => {
    const itemName = prompt('Item name:');
    const quantity = prompt('Quantity:');
    const unit = prompt('Unit (e.g., kg, liters, bags, pieces):');
    const category = prompt('Category (e.g., Seeds, Fertilizer, Pesticide, Tools):');
    if (itemName && quantity && unit) {
      try {
        await fetch('http://localhost:5000/api/inventory', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ item_name: itemName, quantity: parseFloat(quantity), unit, category })
        });
        showNotification('Inventory item added successfully!');
        loadData();
      } catch (error) {
        showNotification('Error adding inventory item', 'error');
      }
    }
  };

  const deleteInventoryItem = async (id) => {
    if (window.confirm('Are you sure you want to delete this item?')) {
      try {
        await fetch('http://localhost:5000/api/inventory/' + id, { method: 'DELETE', credentials: 'include' });
        showNotification('Inventory item deleted successfully!');
        loadData();
      } catch (error) {
        showNotification('Error deleting item', 'error');
      }
    }
  };

  const filterData = (data) => {
    if (!searchTerm) return data;
    return data.filter(item => 
      Object.values(item).some(val => 
        String(val).toLowerCase().includes(searchTerm.toLowerCase())
      )
    );
  };

  const renderContent = () => {
    if (loading) {
      return (
        <div className="loading-container">
          <div className="spinner"></div>
          <p>Loading data...</p>
        </div>
      );
    }

    if (activeTab === 'overview') {
      return (
        <div>
          <h2>📊 Dashboard Overview</h2>
          <div className="stats-grid">
            <div className="stat-card stat-card-crops">
              <div className="stat-icon">🌱</div>
              <div className="stat-info">
                <h3>Total Crops</h3>
                <div className="stat-value">{analytics.total_crops || 0}</div>
              </div>
            </div>
            <div className="stat-card stat-card-fields">
              <div className="stat-icon">🗺️</div>
              <div className="stat-info">
                <h3>Total Fields</h3>
                <div className="stat-value">{analytics.total_fields || 0}</div>
              </div>
            </div>
            <div className="stat-card stat-card-activities">
              <div className="stat-icon">📋</div>
              <div className="stat-info">
                <h3>Activities</h3>
                <div className="stat-value">{analytics.total_activities || 0}</div>
              </div>
            </div>
            <div className="stat-card stat-card-inventory">
              <div className="stat-icon">📦</div>
              <div className="stat-info">
                <h3>Inventory Items</h3>
                <div className="stat-value">{analytics.total_inventory || 0}</div>
              </div>
            </div>
          </div>
          
          <div className="weather-card">
            <h3>🌤️ Current Weather</h3>
            <div className="weather-info">
              <div className="weather-item">
                <span className="weather-label">Temperature:</span>
                <span className="weather-value">{weather.temperature}°C</span>
              </div>
              <div className="weather-item">
                <span className="weather-label">Humidity:</span>
                <span className="weather-value">{weather.humidity}%</span>
              </div>
              <div className="weather-item">
                <span className="weather-label">Conditions:</span>
                <span className="weather-value">{weather.conditions}</span>
              </div>
            </div>
          </div>

          <div className="quick-actions">
            <h3>⚡ Quick Actions</h3>
            <div className="action-buttons">
              <button className="action-btn" onClick={() => { setActiveTab('crops'); addCrop(); }}>
                <span className="action-icon">🌱</span>
                <span>Add Crop</span>
              </button>
              <button className="action-btn" onClick={() => { setActiveTab('fields'); addField(); }}>
                <span className="action-icon">🗺️</span>
                <span>Add Field</span>
              </button>
              <button className="action-btn" onClick={() => { setActiveTab('activities'); addActivity(); }}>
                <span className="action-icon">📋</span>
                <span>Log Activity</span>
              </button>
              <button className="action-btn" onClick={() => { setActiveTab('inventory'); addInventoryItem(); }}>
                <span className="action-icon">📦</span>
                <span>Add Inventory</span>
              </button>
            </div>
          </div>
        </div>
      );
    } else if (activeTab === 'crops') {
      const filteredCrops = filterData(crops);
      return (
        <div className="content-card">
          <div className="card-header">
            <h2>🌱 Crop Management</h2>
            <div className="header-actions">
              <input 
                type="text" 
                className="search-input" 
                placeholder="Search crops..." 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
              <button className="btn-add" onClick={addCrop}>+ Add Crop</button>
            </div>
          </div>
          {filteredCrops.length > 0 ? (
            <div className="table-container">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Planting Date</th>
                    <th>Status</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredCrops.map(crop => (
                    <tr key={crop.id}>
                      <td><strong>{crop.name}</strong></td>
                      <td>{crop.crop_type}</td>
                      <td>{crop.planting_date}</td>
                      <td><span className={'status-badge status-' + crop.status.toLowerCase()}>{crop.status}</span></td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteCrop(crop.id)}>🗑️ Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="empty-state">
              <div className="empty-icon">🌱</div>
              <p>No crops found. Start by adding your first crop!</p>
              <button className="btn-add" onClick={addCrop}>+ Add Your First Crop</button>
            </div>
          )}
        </div>
      );
    } else if (activeTab === 'fields') {
      const filteredFields = filterData(fields);
      return (
        <div className="content-card">
          <div className="card-header">
            <h2>🗺️ Field Management</h2>
            <div className="header-actions">
              <input 
                type="text" 
                className="search-input" 
                placeholder="Search fields..." 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
              <button className="btn-add" onClick={addField}>+ Add Field</button>
            </div>
          </div>
          {filteredFields.length > 0 ? (
            <div className="table-container">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Size (acres)</th>
                    <th>Location</th>
                    <th>Soil Type</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredFields.map(field => (
                    <tr key={field.id}>
                      <td><strong>{field.name}</strong></td>
                      <td>{field.size}</td>
                      <td>{field.location || 'N/A'}</td>
                      <td>{field.soil_type || 'N/A'}</td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteField(field.id)}>🗑️ Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="empty-state">
              <div className="empty-icon">🗺️</div>
              <p>No fields found. Add your first field to get started!</p>
              <button className="btn-add" onClick={addField}>+ Add Your First Field</button>
            </div>
          )}
        </div>
      );
    } else if (activeTab === 'activities') {
      const filteredActivities = filterData(activities);
      return (
        <div className="content-card">
          <div className="card-header">
            <h2>📋 Activity Log</h2>
            <div className="header-actions">
              <input 
                type="text" 
                className="search-input" 
                placeholder="Search activities..." 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
              <button className="btn-add" onClick={addActivity}>+ Log Activity</button>
            </div>
          </div>
          {filteredActivities.length > 0 ? (
            <div className="table-container">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Type</th>
                    <th>Date</th>
                    <th>Description</th>
                    <th>Field ID</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredActivities.map(activity => (
                    <tr key={activity.id}>
                      <td><strong>{activity.activity_type}</strong></td>
                      <td>{activity.date}</td>
                      <td>{activity.description || 'N/A'}</td>
                      <td>Field #{activity.field_id}</td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteActivity(activity.id)}>🗑️ Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="empty-state">
              <div className="empty-icon">📋</div>
              <p>No activities logged yet. Start tracking your farm activities!</p>
              <button className="btn-add" onClick={addActivity}>+ Log Your First Activity</button>
            </div>
          )}
        </div>
      );
    } else if (activeTab === 'inventory') {
      const filteredInventory = filterData(inventory);
      return (
        <div className="content-card">
          <div className="card-header">
            <h2>📦 Inventory Management</h2>
            <div className="header-actions">
              <input 
                type="text" 
                className="search-input" 
                placeholder="Search inventory..." 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
              <button className="btn-add" onClick={addInventoryItem}>+ Add Item</button>
            </div>
          </div>
          {filteredInventory.length > 0 ? (
            <div className="table-container">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Item Name</th>
                    <th>Quantity</th>
                    <th>Unit</th>
                    <th>Category</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredInventory.map(item => (
                    <tr key={item.id}>
                      <td><strong>{item.item_name}</strong></td>
                      <td>{item.quantity}</td>
                      <td>{item.unit}</td>
                      <td><span className="category-badge">{item.category || 'Uncategorized'}</span></td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteInventoryItem(item.id)}>🗑️ Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="empty-state">
              <div className="empty-icon">📦</div>
              <p>No inventory items found. Add items to track your supplies!</p>
              <button className="btn-add" onClick={addInventoryItem}>+ Add Your First Item</button>
            </div>
          )}
        </div>
      );
    }
  };

  return (
    <div className="dashboard">
      {notification && (
        <div className={'notification notification-' + notification.type}>
          {notification.message}
        </div>
      )}
      <div className="dashboard-header">
        <h1>🌾 AgroTracker - Admin Panel</h1>
        <div className="user-info">
          <span className="user-badge">👨‍💼 {user.username} (Admin)</span>
          <button className="btn-logout" onClick={onLogout}>Logout</button>
        </div>
      </div>
      <div className="dashboard-nav">
        <button className={'nav-btn ' + (activeTab === 'overview' ? 'active' : '')} onClick={() => setActiveTab('overview')}>
          <span className="nav-icon">📊</span> Overview
        </button>
        <button className={'nav-btn ' + (activeTab === 'crops' ? 'active' : '')} onClick={() => setActiveTab('crops')}>
          <span className="nav-icon">🌱</span> Crops
        </button>
        <button className={'nav-btn ' + (activeTab === 'fields' ? 'active' : '')} onClick={() => setActiveTab('fields')}>
          <span className="nav-icon">🗺️</span> Fields
        </button>
        <button className={'nav-btn ' + (activeTab === 'activities' ? 'active' : '')} onClick={() => setActiveTab('activities')}>
          <span className="nav-icon">📋</span> Activities
        </button>
        <button className={'nav-btn ' + (activeTab === 'inventory' ? 'active' : '')} onClick={() => setActiveTab('inventory')}>
          <span className="nav-icon">📦</span> Inventory
        </button>
      </div>
      <div className="dashboard-content">{renderContent()}</div>
    </div>
  );
}

export default AdminDashboard;
"""

# Create UserDashboard (same as Admin but with different title)
user_code = admin_code.replace("Admin Panel", "My Farm").replace("👨‍💼 {user.username} (Admin)", "👨‍🌾 {user.username}").replace("function AdminDashboard", "function UserDashboard").replace("export default AdminDashboard", "export default UserDashboard")

with open(r'd:\resumeprojects\AgroTrackingProject\frontend\src\components\AdminDashboard.js', 'w', encoding='utf-8') as f:
    f.write(admin_code)

with open(r'd:\resumeprojects\AgroTrackingProject\frontend\src\components\UserDashboard.js', 'w', encoding='utf-8') as f:
    f.write(user_code)

print("Enhanced dashboards created successfully!")
