import React from 'react';
import { 
  TrendingUp, 
  BarChart3, 
  PieChart, 
  DollarSign, 
  Calendar, 
  Target,
  Award,
  Activity
} from 'lucide-react';

const Analytics = () => {
  const metrics = [
    {
      title: 'Total Revenue',
      value: '$45,230',
      change: '+12.5%',
      period: 'vs last quarter',
      icon: DollarSign,
      color: 'text-green-600',
      bgColor: 'bg-green-100'
    },
    {
      title: 'Crop Yield',
      value: '24.5 tons',
      change: '+8.3%',
      period: 'vs last season',
      icon: Award,
      color: 'text-blue-600',
      bgColor: 'bg-blue-100'
    },
    {
      title: 'Field Efficiency',
      value: '87%',
      change: '+5.2%',
      period: 'vs last month',
      icon: Target,
      color: 'text-purple-600',
      bgColor: 'bg-purple-100'
    },
    {
      title: 'Active Fields',
      value: '12',
      change: '+2',
      period: 'new this month',
      icon: Activity,
      color: 'text-orange-600',
      bgColor: 'bg-orange-100'
    }
  ];

  const cropPerformance = [
    { crop: 'Tomatoes', yield: 85, area: 5.2, revenue: 12500 },
    { crop: 'Corn', yield: 78, area: 8.1, revenue: 18900 },
    { crop: 'Wheat', yield: 92, area: 6.5, revenue: 15600 },
    { crop: 'Soybeans', yield: 73, area: 4.8, revenue: 9800 }
  ];

  const monthlyData = [
    { month: 'Jan', revenue: 12000, expenses: 8000, profit: 4000 },
    { month: 'Feb', revenue: 15000, expenses: 9500, profit: 5500 },
    { month: 'Mar', revenue: 18000, expenses: 11000, profit: 7000 },
    { month: 'Apr', revenue: 16000, expenses: 10200, profit: 5800 },
    { month: 'May', revenue: 22000, expenses: 13500, profit: 8500 },
    { month: 'Jun', revenue: 25000, expenses: 15000, profit: 10000 }
  ];

  const fieldUtilization = [
    { field: 'Field A', utilization: 95 },
    { field: 'Field B', utilization: 87 },
    { field: 'Field C', utilization: 92 },
    { field: 'Field D', utilization: 78 }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Analytics Dashboard</h2>
        <p className="text-gray-600">Insights and performance metrics for your farm</p>
      </div>

      {/* Key Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {metrics.map((metric, index) => {
          const Icon = metric.icon;
          return (
            <div key={index} className="bg-white rounded-xl p-6 shadow-sm">
              <div className="flex items-center justify-between mb-4">
                <div className={`p-3 rounded-lg ${metric.bgColor}`}>
                  <Icon className={`h-6 w-6 ${metric.color}`} />
                </div>
                <TrendingUp className="h-4 w-4 text-green-500" />
              </div>
              <h3 className="text-2xl font-bold text-gray-900 mb-1">{metric.value}</h3>
              <p className="text-sm text-gray-600 mb-2">{metric.title}</p>
              <p className="text-xs text-green-600 font-medium">
                {metric.change} {metric.period}
              </p>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Revenue Trend */}
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-lg font-semibold text-gray-900">Revenue Trend</h3>
            <BarChart3 className="h-5 w-5 text-gray-400" />
          </div>
          <div className="space-y-4">
            {monthlyData.map((data, index) => (
              <div key={index} className="flex items-center space-x-4">
                <div className="w-12 text-sm text-gray-600">{data.month}</div>
                <div className="flex-1 space-y-2">
                  <div className="flex justify-between text-sm">
                    <span>Revenue</span>
                    <span className="font-medium">${data.revenue.toLocaleString()}</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-green-500 h-2 rounded-full" 
                      style={{ width: `${(data.revenue / 25000) * 100}%` }}
                    ></div>
                  </div>
                  <div className="flex justify-between text-sm">
                    <span>Profit</span>
                    <span className="font-medium text-green-600">${data.profit.toLocaleString()}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Crop Performance */}
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-lg font-semibold text-gray-900">Crop Performance</h3>
            <PieChart className="h-5 w-5 text-gray-400" />
          </div>
          <div className="space-y-4">
            {cropPerformance.map((crop, index) => (
              <div key={index} className="p-4 bg-gray-50 rounded-lg">
                <div className="flex items-center justify-between mb-2">
                  <h4 className="font-medium text-gray-900">{crop.crop}</h4>
                  <span className="text-sm font-medium text-green-600">
                    ${crop.revenue.toLocaleString()}
                  </span>
                </div>
                <div className="grid grid-cols-2 gap-4 text-sm text-gray-600">
                  <div>
                    <span>Yield: </span>
                    <span className="font-medium">{crop.yield}%</span>
                  </div>
                  <div>
                    <span>Area: </span>
                    <span className="font-medium">{crop.area} acres</span>
                  </div>
                </div>
                <div className="mt-2">
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-blue-500 h-2 rounded-full" 
                      style={{ width: `${crop.yield}%` }}
                    ></div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Field Utilization */}
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <h3 className="text-lg font-semibold text-gray-900 mb-6">Field Utilization</h3>
          <div className="space-y-4">
            {fieldUtilization.map((field, index) => (
              <div key={index} className="flex items-center justify-between">
                <span className="text-sm text-gray-600">{field.field}</span>
                <div className="flex items-center space-x-3">
                  <div className="w-32 bg-gray-200 rounded-full h-2">
                    <div 
                      className={`h-2 rounded-full ${
                        field.utilization >= 90 ? 'bg-green-500' :
                        field.utilization >= 80 ? 'bg-yellow-500' : 'bg-red-500'
                      }`}
                      style={{ width: `${field.utilization}%` }}
                    ></div>
                  </div>
                  <span className="text-sm font-medium w-12">{field.utilization}%</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Quick Stats */}
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <h3 className="text-lg font-semibold text-gray-900 mb-6">Quick Stats</h3>
          <div className="space-y-4">
            <div className="flex items-center justify-between p-3 bg-green-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <Calendar className="h-5 w-5 text-green-600" />
                <span className="text-sm text-gray-700">Growing Season</span>
              </div>
              <span className="text-sm font-medium text-green-600">68 days left</span>
            </div>
            
            <div className="flex items-center justify-between p-3 bg-blue-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <Target className="h-5 w-5 text-blue-600" />
                <span className="text-sm text-gray-700">Yield Target</span>
              </div>
              <span className="text-sm font-medium text-blue-600">92% achieved</span>
            </div>
            
            <div className="flex items-center justify-between p-3 bg-purple-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <Award className="h-5 w-5 text-purple-600" />
                <span className="text-sm text-gray-700">Best Performing</span>
              </div>
              <span className="text-sm font-medium text-purple-600">Wheat (92%)</span>
            </div>
            
            <div className="flex items-center justify-between p-3 bg-orange-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <Activity className="h-5 w-5 text-orange-600" />
                <span className="text-sm text-gray-700">Activities This Week</span>
              </div>
              <span className="text-sm font-medium text-orange-600">12 completed</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Analytics;