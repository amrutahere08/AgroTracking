import os

# AdminDashboard content
admin_dashboard = """import React, { useState, useEffect } from 'react';

function AdminDashboard({ user, onLogout }) {
  const [activeTab, setActiveTab] = useState('overview');
  const [crops, setCrops] = useState([]);
  const [fields, setFields] = useState([]);
  const [activities, setActivities] = useState([]);
  const [inventory, setInventory] = useState([]);
  const [analytics, setAnalytics] = useState({});

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    try {
      if (activeTab === 'overview') {
        const analyticsRes = await fetch('http://localhost:5000/api/analytics', { credentials: 'include' });
        const analyticsData = await analyticsRes.json();
        setAnalytics(analyticsData);
      }
      
      if (activeTab === 'crops') {
        const cropsRes = await fetch('http://localhost:5000/api/crops', { credentials: 'include' });
        const cropsData = await cropsRes.json();
        setCrops(cropsData);
      }
      
      if (activeTab === 'fields') {
        const fieldsRes = await fetch('http://localhost:5000/api/fields', { credentials: 'include' });
        const fieldsData = await fieldsRes.json();
        setFields(fieldsData);
      }
      
      if (activeTab === 'activities') {
        const activitiesRes = await fetch('http://localhost:5000/api/activities', { credentials: 'include' });
        const activitiesData = await activitiesRes.json();
        setActivities(activitiesData);
      }
      
      if (activeTab === 'inventory') {
        const inventoryRes = await fetch('http://localhost:5000/api/inventory', { credentials: 'include' });
        const inventoryData = await inventoryRes.json();
        setInventory(inventoryData);
      }
    } catch (error) {
      console.error('Error loading data:', error);
    }
  };

  const addCrop = async () => {
    const name = prompt('Crop name:');
    const cropType = prompt('Crop type:');
    const plantingDate = prompt('Planting date (YYYY-MM-DD):');
    
    if (name && cropType && plantingDate) {
      try {
        await fetch('http://localhost:5000/api/crops', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ name, crop_type: cropType, planting_date: plantingDate })
        });
        loadData();
      } catch (error) {
        alert('Error adding crop');
      }
    }
  };

  const deleteCrop = async (id) => {
    if (window.confirm('Delete this crop?')) {
      try {
        await fetch(`http://localhost:5000/api/crops/${id}`, {
          method: 'DELETE',
          credentials: 'include'
        });
        loadData();
      } catch (error) {
        alert('Error deleting crop');
      }
    }
  };

  const addField = async () => {
    const name = prompt('Field name:');
    const size = prompt('Size (acres):');
    const location = prompt('Location:');
    const soilType = prompt('Soil type:');
    
    if (name && size) {
      try {
        await fetch('http://localhost:5000/api/fields', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ name, size: parseFloat(size), location, soil_type: soilType })
        });
        loadData();
      } catch (error) {
        alert('Error adding field');
      }
    }
  };

  const deleteField = async (id) => {
    if (window.confirm('Delete this field?')) {
      try {
        await fetch(`http://localhost:5000/api/fields/${id}`, {
          method: 'DELETE',
          credentials: 'include'
        });
        loadData();
      } catch (error) {
        alert('Error deleting field');
      }
    }
  };

  const addActivity = async () => {
    if (fields.length === 0) {
      alert('Please add a field first');
      return;
    }
    
    const activityType = prompt('Activity type (e.g., planting, watering, fertilizing):');
    const date = prompt('Date (YYYY-MM-DD):');
    const description = prompt('Description:');
    const fieldId = prompt(`Field ID (${fields.map(f => `${f.id}: ${f.name}`).join(', ')}):');
    
    if (activityType && date && fieldId) {
      try {
        await fetch('http://localhost:5000/api/activities', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ activity_type: activityType, date, description, field_id: parseInt(fieldId) })
        });
        loadData();
      } catch (error) {
        alert('Error adding activity');
      }
    }
  };

  const deleteActivity = async (id) => {
    if (window.confirm('Delete this activity?')) {
      try {
        await fetch(`http://localhost:5000/api/activities/${id}`, {
          method: 'DELETE',
          credentials: 'include'
        });
        loadData();
      } catch (error) {
        alert('Error deleting activity');
      }
    }
  };

  const addInventoryItem = async () => {
    const itemName = prompt('Item name:');
    const quantity = prompt('Quantity:');
    const unit = prompt('Unit (e.g., kg, liters, bags):');
    const category = prompt('Category (e.g., seeds, fertilizer, pesticide):');
    
    if (itemName && quantity && unit) {
      try {
        await fetch('http://localhost:5000/api/inventory', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ item_name: itemName, quantity: parseFloat(quantity), unit, category })
        });
        loadData();
      } catch (error) {
        alert('Error adding inventory item');
      }
    }
  };

  const deleteInventoryItem = async (id) => {
    if (window.confirm('Delete this item?')) {
      try {
        await fetch(`http://localhost:5000/api/inventory/${id}`, {
          method: 'DELETE',
          credentials: 'include'
        });
        loadData();
      } catch (error) {
        alert('Error deleting item');
      }
    }
  };

  const renderContent = () => {
    switch (activeTab) {
      case 'overview':
        return (
          <div>
            <h2>Dashboard Overview</h2>
            <div className="stats-grid">
              <div className="stat-card">
                <h3>Total Crops</h3>
                <div className="stat-value">{analytics.total_crops || 0}</div>
              </div>
              <div className="stat-card">
                <h3>Total Fields</h3>
                <div className="stat-value">{analytics.total_fields || 0}</div>
              </div>
              <div className="stat-card">
                <h3>Activities</h3>
                <div className="stat-value">{analytics.total_activities || 0}</div>
              </div>
              <div className="stat-card">
                <h3>Inventory Items</h3>
                <div className="stat-value">{analytics.total_inventory || 0}</div>
              </div>
            </div>
          </div>
        );
      
      case 'crops':
        return (
          <div className="content-card">
            <h2>Crop Management</h2>
            <button className="btn-add" onClick={addCrop}>+ Add Crop</button>
            {crops.length > 0 ? (
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
                  {crops.map(crop => (
                    <tr key={crop.id}>
                      <td>{crop.name}</td>
                      <td>{crop.crop_type}</td>
                      <td>{crop.planting_date}</td>
                      <td>{crop.status}</td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteCrop(crop.id)}>Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="empty-state">
                <p>No crops yet. Add your first crop!</p>
              </div>
            )}
          </div>
        );
      
      case 'fields':
        return (
          <div className="content-card">
            <h2>Field Management</h2>
            <button className="btn-add" onClick={addField}>+ Add Field</button>
            {fields.length > 0 ? (
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
                  {fields.map(field => (
                    <tr key={field.id}>
                      <td>{field.name}</td>
                      <td>{field.size}</td>
                      <td>{field.location || 'N/A'}</td>
                      <td>{field.soil_type || 'N/A'}</td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteField(field.id)}>Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="empty-state">
                <p>No fields yet. Add your first field!</p>
              </div>
            )}
          </div>
        );
      
      case 'activities':
        return (
          <div className="content-card">
            <h2>Activity Log</h2>
            <button className="btn-add" onClick={addActivity}>+ Add Activity</button>
            {activities.length > 0 ? (
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
                  {activities.map(activity => (
                    <tr key={activity.id}>
                      <td>{activity.activity_type}</td>
                      <td>{activity.date}</td>
                      <td>{activity.description || 'N/A'}</td>
                      <td>{activity.field_id}</td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteActivity(activity.id)}>Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="empty-state">
                <p>No activities yet. Log your first activity!</p>
              </div>
            )}
          </div>
        );
      
      case 'inventory':
        return (
          <div className="content-card">
            <h2>Inventory Management</h2>
            <button className="btn-add" onClick={addInventoryItem}>+ Add Item</button>
            {inventory.length > 0 ? (
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
                  {inventory.map(item => (
                    <tr key={item.id}>
                      <td>{item.item_name}</td>
                      <td>{item.quantity}</td>
                      <td>{item.unit}</td>
                      <td>{item.category || 'N/A'}</td>
                      <td>
                        <button className="btn-delete" onClick={() => deleteInventoryItem(item.id)}>Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <div className="empty-state">
                <p>No inventory items yet. Add your first item!</p>
              </div>
            )}
          </div>
        );
      
      default:
        return null;
    }
  };

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>🌾 AgroTracker - Admin Panel</h1>
        <div className="user-info">
          <span className="user-badge">👨‍💼 {user.username} (Admin)</span>
          <button className="btn-logout" onClick={onLogout}>Logout</button>
        </div>
      </div>
      
      <div className="dashboard-nav">
        <button className={`nav-btn ${activeTab === 'overview' ? 'active' : ''}`} onClick={() => setActiveTab('overview')}>Overview</button>
        <button className={`nav-btn ${activeTab === 'crops' ? 'active' : ''}`} onClick={() => setActiveTab('crops')}>Crops</button>
        <button className={`nav-btn ${activeTab === 'fields' ? 'active' : ''}`} onClick={() => setActiveTab('fields')}>Fields</button>
        <button className={`nav-btn ${activeTab === 'activities' ? 'active' : ''}`} onClick={() => setActiveTab('activities')}>Activities</button>
        <button className={`nav-btn ${activeTab === 'inventory' ? 'active' : ''}`} onClick={() => setActiveTab('inventory')}>Inventory</button>
      </div>
      
      <div className="dashboard-content">
        {renderContent()}
      </div>
    </div>
  );
}

export default AdminDashboard;
"""

# UserDashboard content (same as AdminDashboard but with different header)
user_dashboard = admin_dashboard.replace("Admin Panel", "My Farm").replace("👨‍💼 {user.username} (Admin)", "👨‍🌾 {user.username}")

# Write files
admin_path = r"d:\resumeprojects\AgroTrackingProject\frontend\src\components\AdminDashboard.js"
user_path = r"d:\resumeprojects\AgroTrackingProject\frontend\src\components\UserDashboard.js"

with open(admin_path, 'w', encoding='utf-8') as f:
    f.write(admin_dashboard)

with open(user_path, 'w', encoding='utf-8') as f:
    f.write(user_dashboard)

print("Dashboard files created successfully!")
