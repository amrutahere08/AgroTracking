import React, { useState } from 'react';
import { 
  Home, 
  Sprout, 
  MapPin, 
  Calendar, 
  CloudRain, 
  Package, 
  BarChart3,
  Plus,
  Bell,
  Settings,
  User
} from 'lucide-react';
import Dashboard from './components/Dashboard';
import CropManagement from './components/CropManagement';
import FieldManagement from './components/FieldManagement';
import ActivityLog from './components/ActivityLog';
import WeatherMonitor from './components/WeatherMonitor';
import Inventory from './components/Inventory';
import Analytics from './components/Analytics';

type TabType = 'dashboard' | 'crops' | 'fields' | 'activities' | 'weather' | 'inventory' | 'analytics';

function App() {
  const [activeTab, setActiveTab] = useState<TabType>('dashboard');

  const tabs = [
    { id: 'dashboard', label: 'Dashboard', icon: Home },
    { id: 'crops', label: 'Crops', icon: Sprout },
    { id: 'fields', label: 'Fields', icon: MapPin },
    { id: 'activities', label: 'Activities', icon: Calendar },
    { id: 'weather', label: 'Weather', icon: CloudRain },
    { id: 'inventory', label: 'Inventory', icon: Package },
    { id: 'analytics', label: 'Analytics', icon: BarChart3 },
  ];

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return <Dashboard />;
      case 'crops':
        return <CropManagement />;
      case 'fields':
        return <FieldManagement />;
      case 'activities':
        return <ActivityLog />;
      case 'weather':
        return <WeatherMonitor />;
      case 'inventory':
        return <Inventory />;
      case 'analytics':
        return <Analytics />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-green-500 rounded-lg">
                <Sprout className="h-6 w-6 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold text-gray-900">AgroTracker</h1>
                <p className="text-sm text-gray-600">Smart Farm Management</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <button className="p-2 text-gray-600 hover:text-green-600 transition-colors">
                <Bell className="h-5 w-5" />
              </button>
              <button className="p-2 text-gray-600 hover:text-green-600 transition-colors">
                <Settings className="h-5 w-5" />
              </button>
              <button className="p-2 text-gray-600 hover:text-green-600 transition-colors">
                <User className="h-5 w-5" />
              </button>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex flex-col lg:flex-row gap-8">
          {/* Sidebar Navigation */}
          <div className="lg:w-64">
            <nav className="bg-white rounded-xl shadow-sm p-4">
              <div className="space-y-2">
                {tabs.map((tab) => {
                  const Icon = tab.icon;
                  return (
                    <button
                      key={tab.id}
                      onClick={() => setActiveTab(tab.id as TabType)}
                      className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg transition-all duration-200 ${
                        activeTab === tab.id
                          ? 'bg-green-500 text-white shadow-lg transform scale-105'
                          : 'text-gray-600 hover:bg-gray-50 hover:text-green-600'
                      }`}
                    >
                      <Icon className="h-5 w-5" />
                      <span className="font-medium">{tab.label}</span>
                    </button>
                  );
                })}
              </div>
            </nav>
          </div>

          {/* Main Content */}
          <div className="flex-1">
            {renderContent()}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;