# Script to create full CRUD dashboards
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
        const res = await fetch('http://localhost:5000/api/analytics', { credentials: 'include' });
        setAnalytics(await res.json());
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
      console.error('Error:', error);
    }
  };

  const addCrop = async () => {
    const name = prompt('Crop name:');
    const cropType = prompt('Crop type:');
    const plantingDate = prompt('Planting date (YYYY-MM-DD):');
    if (name && cropType && plantingDate) {
      await fetch('http://localhost:5000/api/crops', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ name, crop_type: cropType, planting_date: plantingDate })
      });
      loadData();
    }
  };

  const deleteCrop = async (id) => {
    if (window.confirm('Delete this crop?')) {
      await fetch('http://localhost:5000/api/crops/' + id, { method: 'DELETE', credentials: 'include' });
      loadData();
    }
  };

  const addField = async () => {
    const name = prompt('Field name:');
    const size = prompt('Size (acres):');
    const location = prompt('Location:');
    const soilType = prompt('Soil type:');
    if (name && size) {
      await fetch('http://localhost:5000/api/fields', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ name, size: parseFloat(size), location, soil_type: soilType })
      });
      loadData();
    }
  };

  const deleteField = async (id) => {
    if (window.confirm('Delete this field?')) {
      await fetch('http://localhost:5000/api/fields/' + id, { method: 'DELETE', credentials: 'include' });
      loadData();
    }
  };

  const addActivity = async () => {
    if (fields.length === 0) {
      alert('Please add a field first');
      return;
    }
    const activityType = prompt('Activity type (e.g., planting, watering):');
    const date = prompt('Date (YYYY-MM-DD):');
    const description = prompt('Description:');
    const fieldList = fields.map(f => f.id + ': ' + f.name).join(', ');
    const fieldId = prompt('Field ID (' + fieldList + '):');
    if (activityType && date && fieldId) {
      await fetch('http://localhost:5000/api/activities', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ activity_type: activityType, date, description, field_id: parseInt(fieldId) })
      });
      loadData();
    }
  };

  const deleteActivity = async (id) => {
    if (window.confirm('Delete this activity?')) {
      await fetch('http://localhost:5000/api/activities/' + id, { method: 'DELETE', credentials: 'include' });
      loadData();
    }
  };

  const addInventoryItem = async () => {
    const itemName = prompt('Item name:');
    const quantity = prompt('Quantity:');
    const unit = prompt('Unit (e.g., kg, liters):');
    const category = prompt('Category (e.g., seeds, fertilizer):');
    if (itemName && quantity && unit) {
      await fetch('http://localhost:5000/api/inventory', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ item_name: itemName, quantity: parseFloat(quantity), unit, category })
      });
      loadData();
    }
  };

  const deleteInventoryItem = async (id) => {
    if (window.confirm('Delete this item?')) {
      await fetch('http://localhost:5000/api/inventory/' + id, { method: 'DELETE', credentials: 'include' });
      loadData();
    }
  };

  const renderContent = () => {
    if (activeTab === 'overview') {
      return (
        <div>
          <h2>Dashboard Overview</h2>
          <div className="stats-grid">
            <div className="stat-card"><h3>Total Crops</h3><div className="stat-value">{analytics.total_crops || 0}</div></div>
            <div className="stat-card"><h3>Total Fields</h3><div className="stat-value">{analytics.total_fields || 0}</div></div>
            <div className="stat-card"><h3>Activities</h3><div className="stat-value">{analytics.total_activities || 0}</div></div>
            <div className="stat-card"><h3>Inventory Items</h3><div className="stat-value">{analytics.total_inventory || 0}</div></div>
          </div>
        </div>
      );
    } else if (activeTab === 'crops') {
      return (
        <div className="content-card">
          <h2>Crop Management</h2>
          <button className="btn-add" onClick={addCrop}>+ Add Crop</button>
          {crops.length > 0 ? (
            <table className="data-table">
              <thead><tr><th>Name</th><th>Type</th><th>Planting Date</th><th>Status</th><th>Actions</th></tr></thead>
              <tbody>
                {crops.map(crop => (
                  <tr key={crop.id}>
                    <td>{crop.name}</td>
                    <td>{crop.crop_type}</td>
                    <td>{crop.planting_date}</td>
                    <td>{crop.status}</td>
                    <td><button className="btn-delete" onClick={() => deleteCrop(crop.id)}>Delete</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : <div className="empty-state"><p>No crops yet. Add your first crop!</p></div>}
        </div>
      );
    } else if (activeTab === 'fields') {
      return (
        <div className="content-card">
          <h2>Field Management</h2>
          <button className="btn-add" onClick={addField}>+ Add Field</button>
          {fields.length > 0 ? (
            <table className="data-table">
              <thead><tr><th>Name</th><th>Size (acres)</th><th>Location</th><th>Soil Type</th><th>Actions</th></tr></thead>
              <tbody>
                {fields.map(field => (
                  <tr key={field.id}>
                    <td>{field.name}</td>
                    <td>{field.size}</td>
                    <td>{field.location || 'N/A'}</td>
                    <td>{field.soil_type || 'N/A'}</td>
                    <td><button className="btn-delete" onClick={() => deleteField(field.id)}>Delete</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : <div className="empty-state"><p>No fields yet. Add your first field!</p></div>}
        </div>
      );
    } else if (activeTab === 'activities') {
      return (
        <div className="content-card">
          <h2>Activity Log</h2>
          <button className="btn-add" onClick={addActivity}>+ Add Activity</button>
          {activities.length > 0 ? (
            <table className="data-table">
              <thead><tr><th>Type</th><th>Date</th><th>Description</th><th>Field ID</th><th>Actions</th></tr></thead>
              <tbody>
                {activities.map(activity => (
                  <tr key={activity.id}>
                    <td>{activity.activity_type}</td>
                    <td>{activity.date}</td>
                    <td>{activity.description || 'N/A'}</td>
                    <td>{activity.field_id}</td>
                    <td><button className="btn-delete" onClick={() => deleteActivity(activity.id)}>Delete</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : <div className="empty-state"><p>No activities yet. Log your first activity!</p></div>}
        </div>
      );
    } else if (activeTab === 'inventory') {
      return (
        <div className="content-card">
          <h2>Inventory Management</h2>
          <button className="btn-add" onClick={addInventoryItem}>+ Add Item</button>
          {inventory.length > 0 ? (
            <table className="data-table">
              <thead><tr><th>Item Name</th><th>Quantity</th><th>Unit</th><th>Category</th><th>Actions</th></tr></thead>
              <tbody>
                {inventory.map(item => (
                  <tr key={item.id}>
                    <td>{item.item_name}</td>
                    <td>{item.quantity}</td>
                    <td>{item.unit}</td>
                    <td>{item.category || 'N/A'}</td>
                    <td><button className="btn-delete" onClick={() => deleteInventoryItem(item.id)}>Delete</button></td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : <div className="empty-state"><p>No inventory items yet. Add your first item!</p></div>}
        </div>
      );
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
        <button className={'nav-btn ' + (activeTab === 'overview' ? 'active' : '')} onClick={() => setActiveTab('overview')}>Overview</button>
        <button className={'nav-btn ' + (activeTab === 'crops' ? 'active' : '')} onClick={() => setActiveTab('crops')}>Crops</button>
        <button className={'nav-btn ' + (activeTab === 'fields' ? 'active' : '')} onClick={() => setActiveTab('fields')}>Fields</button>
        <button className={'nav-btn ' + (activeTab === 'activities' ? 'active' : '')} onClick={() => setActiveTab('activities')}>Activities</button>
        <button className={'nav-btn ' + (activeTab === 'inventory' ? 'active' : '')} onClick={() => setActiveTab('inventory')}>Inventory</button>
      </div>
      <div className="dashboard-content">{renderContent()}</div>
    </div>
  );
}

export default AdminDashboard;
"""

user_dashboard = admin_dashboard.replace("Admin Panel", "My Farm").replace("👨‍💼 {user.username} (Admin)", "👨‍🌾 {user.username}").replace("function AdminDashboard", "function UserDashboard").replace("export default AdminDashboard", "export default UserDashboard")

with open(r'd:\resumeprojects\AgroTrackingProject\frontend\src\components\AdminDashboard.js', 'w', encoding='utf-8') as f:
    f.write(admin_dashboard)

with open(r'd:\resumeprojects\AgroTrackingProject\frontend\src\components\UserDashboard.js', 'w', encoding='utf-8') as f:
    f.write(user_dashboard)

print("Full CRUD dashboards created successfully!")
