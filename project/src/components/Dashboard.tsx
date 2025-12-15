import React from 'react';
import { 
  TrendingUp, 
  Droplets, 
  Thermometer, 
  Calendar, 
  AlertTriangle,
  CheckCircle,
  Clock,
  Sprout
} from 'lucide-react';

const Dashboard = () => {
  const stats = [
    {
      label: 'Total Fields',
      value: '12',
      change: '+2 this month',
      icon: Sprout,
      color: 'green'
    },
    {
      label: 'Active Crops',
      value: '8',
      change: '3 ready to harvest',
      icon: CheckCircle,
      color: 'blue'
    },
    {
      label: 'Avg Temperature',
      value: '24°C',
      change: '+2°C from yesterday',
      icon: Thermometer,
      color: 'orange'
    },
    {
      label: 'Rainfall',
      value: '12mm',
      change: 'Last 7 days',
      icon: Droplets,
      color: 'cyan'
    }
  ];

  const recentActivities = [
    { id: 1, action: 'Planted tomatoes', field: 'Field A', time: '2 hours ago', status: 'completed' },
    { id: 2, action: 'Watered corn field', field: 'Field B', time: '5 hours ago', status: 'completed' },
    { id: 3, action: 'Applied fertilizer', field: 'Field C', time: '1 day ago', status: 'completed' },
    { id: 4, action: 'Pest inspection', field: 'Field D', time: '2 days ago', status: 'pending' },
  ];

  const alerts = [
    { id: 1, message: 'Low soil moisture in Field B', priority: 'high', time: '30 min ago' },
    { id: 2, message: 'Harvest ready for wheat in Field A', priority: 'medium', time: '2 hours ago' },
    { id: 3, message: 'Weather alert: Heavy rain expected', priority: 'high', time: '4 hours ago' },
  ];

  return (
    <div className="space-y-8">
      {/* Welcome Section */}
      <div className="bg-gradient-to-r from-green-500 to-green-600 rounded-xl p-8 text-white">
        <h2 className="text-3xl font-bold mb-2">Welcome back, Farmer!</h2>
        <p className="text-green-100 text-lg">Here's what's happening on your farm today</p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => {
          const Icon = stat.icon;
          const colorClasses = {
            green: 'bg-green-500',
            blue: 'bg-blue-500',
            orange: 'bg-orange-500',
            cyan: 'bg-cyan-500'
          };
          
          return (
            <div key={index} className="bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
              <div className="flex items-center justify-between mb-4">
                <div className={`p-3 rounded-lg ${colorClasses[stat.color as keyof typeof colorClasses]}`}>
                  <Icon className="h-6 w-6 text-white" />
                </div>
                <TrendingUp className="h-4 w-4 text-green-500" />
              </div>
              <h3 className="text-2xl font-bold text-gray-900 mb-1">{stat.value}</h3>
              <p className="text-sm text-gray-600 mb-2">{stat.label}</p>
              <p className="text-xs text-green-600 font-medium">{stat.change}</p>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Recent Activities */}
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-xl font-bold text-gray-900">Recent Activities</h3>
            <Calendar className="h-5 w-5 text-gray-400" />
          </div>
          <div className="space-y-4">
            {recentActivities.map((activity) => (
              <div key={activity.id} className="flex items-center space-x-4 p-4 bg-gray-50 rounded-lg">
                <div className={`p-2 rounded-full ${
                  activity.status === 'completed' ? 'bg-green-100' : 'bg-yellow-100'
                }`}>
                  {activity.status === 'completed' ? (
                    <CheckCircle className="h-4 w-4 text-green-600" />
                  ) : (
                    <Clock className="h-4 w-4 text-yellow-600" />
                  )}
                </div>
                <div className="flex-1">
                  <p className="font-medium text-gray-900">{activity.action}</p>
                  <p className="text-sm text-gray-600">{activity.field} • {activity.time}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Alerts */}
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-xl font-bold text-gray-900">Alerts & Notifications</h3>
            <AlertTriangle className="h-5 w-5 text-red-400" />
          </div>
          <div className="space-y-4">
            {alerts.map((alert) => (
              <div key={alert.id} className="flex items-start space-x-4 p-4 bg-red-50 rounded-lg border-l-4 border-red-400">
                <AlertTriangle className="h-5 w-5 text-red-500 mt-0.5" />
                <div className="flex-1">
                  <p className="font-medium text-gray-900">{alert.message}</p>
                  <p className="text-sm text-gray-600 mt-1">{alert.time}</p>
                </div>
                <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                  alert.priority === 'high' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                }`}>
                  {alert.priority}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;