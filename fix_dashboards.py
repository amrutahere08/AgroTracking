admin_content = """import React, { useState, useEffect } from 'react';

function AdminDashboard({ user, onLogout }) {
  const [activeTab, setActiveTab] = useState('overview');
  const [data, setData] = useState({ crops: [], fields: [], activities: [], inventory: [], analytics: {} });

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    try {
      const endpoint = activeTab === 'overview' ? 'analytics' : activeTab;
      const res = await fetch('http://localhost:5000/api/' + endpoint, { credentials: 'include' });
      const jsonData = await res.json();
      if (activeTab === 'overview') {
        setData(prev => ({ ...prev, analytics: jsonData }));
      } else {
        setData(prev => ({ ...prev, [activeTab]: jsonData }));
      }
    } catch (error) {
      console.error('Error:', error);
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
      
      <div className="dashboard-content">
        <div className="content-card">
          <h2>{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)}</h2>
          <p>Dashboard is working! Full CRUD features coming soon.</p>
          {activeTab === 'overview' && (
            <div className="stats-grid">
              <div className="stat-card"><h3>Crops</h3><div className="stat-value">{data.analytics.total_crops || 0}</div></div>
              <div className="stat-card"><h3>Fields</h3><div className="stat-value">{data.analytics.total_fields || 0}</div></div>
              <div className="stat-card"><h3>Activities</h3><div className="stat-value">{data.analytics.total_activities || 0}</div></div>
              <div className="stat-card"><h3>Inventory</h3><div className="stat-value">{data.analytics.total_inventory || 0}</div></div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default AdminDashboard;
"""

user_content = """import React, { useState, useEffect } from 'react';

function UserDashboard({ user, onLogout }) {
  const [activeTab, setActiveTab] = useState('overview');
  const [data, setData] = useState({ crops: [], fields: [], activities: [], inventory: [], analytics: {} });

  useEffect(() => {
    loadData();
  }, [activeTab]);

  const loadData = async () => {
    try {
      const endpoint = activeTab === 'overview' ? 'analytics' : activeTab;
      const res = await fetch('http://localhost:5000/api/' + endpoint, { credentials: 'include' });
      const jsonData = await res.json();
      if (activeTab === 'overview') {
        setData(prev => ({ ...prev, analytics: jsonData }));
      } else {
        setData(prev => ({ ...prev, [activeTab]: jsonData }));
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>🌾 AgroTracker - My Farm</h1>
        <div className="user-info">
          <span className="user-badge">👨‍🌾 {user.username}</span>
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
      
      <div className="dashboard-content">
        <div className="content-card">
          <h2>{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)}</h2>
          <p>Dashboard is working! Full CRUD features coming soon.</p>
          {activeTab === 'overview' && (
            <div className="stats-grid">
              <div className="stat-card"><h3>Crops</h3><div className="stat-value">{data.analytics.total_crops || 0}</div></div>
              <div className="stat-card"><h3>Fields</h3><div className="stat-value">{data.analytics.total_fields || 0}</div></div>
              <div className="stat-card"><h3>Activities</h3><div className="stat-value">{data.analytics.total_activities || 0}</div></div>
              <div className="stat-card"><h3>Inventory</h3><div className="stat-value">{data.analytics.total_inventory || 0}</div></div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default UserDashboard;
"""

with open(r'd:\resumeprojects\AgroTrackingProject\frontend\src\components\AdminDashboard.js', 'w', encoding='utf-8') as f:
    f.write(admin_content)

with open(r'd:\resumeprojects\AgroTrackingProject\frontend\src\components\UserDashboard.js', 'w', encoding='utf-8') as f:
    f.write(user_content)

print("Dashboard files created successfully!")
