import React from 'react';
import { 
  Sun, 
  CloudRain, 
  Wind, 
  Thermometer, 
  Droplets, 
  Eye, 
  Compass,
  AlertTriangle
} from 'lucide-react';

const WeatherMonitor = () => {
  const currentWeather = {
    temperature: 24,
    humidity: 65,
    windSpeed: 12,
    windDirection: 'SW',
    visibility: 10,
    pressure: 1013,
    condition: 'Partly Cloudy',
    uvIndex: 6,
    rainfall: 0
  };

  const forecast = [
    { day: 'Today', high: 26, low: 18, condition: 'Partly Cloudy', icon: Sun, rain: 10 },
    { day: 'Tomorrow', high: 28, low: 20, condition: 'Sunny', icon: Sun, rain: 0 },
    { day: 'Wednesday', high: 22, low: 16, condition: 'Rainy', icon: CloudRain, rain: 80 },
    { day: 'Thursday', high: 24, low: 17, condition: 'Cloudy', icon: CloudRain, rain: 30 },
    { day: 'Friday', high: 27, low: 19, condition: 'Sunny', icon: Sun, rain: 5 },
    { day: 'Saturday', high: 25, low: 18, condition: 'Partly Cloudy', icon: Sun, rain: 15 },
    { day: 'Sunday', high: 23, low: 16, condition: 'Rainy', icon: CloudRain, rain: 90 }
  ];

  const alerts = [
    {
      id: 1,
      type: 'warning',
      title: 'Heavy Rain Expected',
      message: 'Heavy rainfall expected Wednesday. Consider postponing outdoor activities.',
      time: '2 hours ago'
    },
    {
      id: 2,
      type: 'info',
      title: 'Optimal Planting Conditions',
      message: 'Weather conditions are ideal for planting this weekend.',
      time: '1 day ago'
    }
  ];

  const getUVLevel = (uvIndex: number) => {
    if (uvIndex <= 2) return { level: 'Low', color: 'text-green-600' };
    if (uvIndex <= 5) return { level: 'Moderate', color: 'text-yellow-600' };
    if (uvIndex <= 7) return { level: 'High', color: 'text-orange-600' };
    if (uvIndex <= 10) return { level: 'Very High', color: 'text-red-600' };
    return { level: 'Extreme', color: 'text-purple-600' };
  };

  const uvLevel = getUVLevel(currentWeather.uvIndex);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900">Weather Monitor</h2>
        <p className="text-gray-600">Real-time weather conditions and forecasts</p>
      </div>

      {/* Current Weather */}
      <div className="bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl p-8 text-white">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h3 className="text-xl font-semibold mb-2">Current Weather</h3>
            <p className="text-blue-100">Updated 5 minutes ago</p>
          </div>
          <Sun className="h-12 w-12 text-yellow-300" />
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div className="text-center">
            <div className="text-3xl font-bold">{currentWeather.temperature}°C</div>
            <div className="text-blue-100">Temperature</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold">{currentWeather.humidity}%</div>
            <div className="text-blue-100">Humidity</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold">{currentWeather.windSpeed}</div>
            <div className="text-blue-100">Wind (km/h)</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold">{currentWeather.pressure}</div>
            <div className="text-blue-100">Pressure (hPa)</div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Detailed Conditions */}
        <div className="lg:col-span-2 bg-white rounded-xl p-6 shadow-sm">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Detailed Conditions</h3>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <Thermometer className="h-6 w-6 text-red-500" />
              <div>
                <p className="text-sm text-gray-600">Temperature</p>
                <p className="font-semibold">{currentWeather.temperature}°C</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <Droplets className="h-6 w-6 text-blue-500" />
              <div>
                <p className="text-sm text-gray-600">Humidity</p>
                <p className="font-semibold">{currentWeather.humidity}%</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <Wind className="h-6 w-6 text-gray-500" />
              <div>
                <p className="text-sm text-gray-600">Wind Speed</p>
                <p className="font-semibold">{currentWeather.windSpeed} km/h</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <Compass className="h-6 w-6 text-green-500" />
              <div>
                <p className="text-sm text-gray-600">Wind Direction</p>
                <p className="font-semibold">{currentWeather.windDirection}</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <Eye className="h-6 w-6 text-purple-500" />
              <div>
                <p className="text-sm text-gray-600">Visibility</p>
                <p className="font-semibold">{currentWeather.visibility} km</p>
              </div>
            </div>
            
            <div className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <Sun className="h-6 w-6 text-yellow-500" />
              <div>
                <p className="text-sm text-gray-600">UV Index</p>
                <p className={`font-semibold ${uvLevel.color}`}>
                  {currentWeather.uvIndex} ({uvLevel.level})
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Weather Alerts */}
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Weather Alerts</h3>
          <div className="space-y-4">
            {alerts.map((alert) => (
              <div key={alert.id} className={`p-4 rounded-lg border-l-4 ${
                alert.type === 'warning' ? 'bg-yellow-50 border-yellow-400' : 'bg-blue-50 border-blue-400'
              }`}>
                <div className="flex items-start space-x-3">
                  <AlertTriangle className={`h-5 w-5 mt-0.5 ${
                    alert.type === 'warning' ? 'text-yellow-600' : 'text-blue-600'
                  }`} />
                  <div>
                    <h4 className="font-medium text-gray-900">{alert.title}</h4>
                    <p className="text-sm text-gray-600 mt-1">{alert.message}</p>
                    <p className="text-xs text-gray-500 mt-2">{alert.time}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* 7-Day Forecast */}
      <div className="bg-white rounded-xl p-6 shadow-sm">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">7-Day Forecast</h3>
        <div className="grid grid-cols-1 md:grid-cols-7 gap-4">
          {forecast.map((day, index) => {
            const Icon = day.icon;
            return (
              <div key={index} className="text-center p-4 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors">
                <p className="text-sm font-medium text-gray-900 mb-2">{day.day}</p>
                <Icon className="h-8 w-8 mx-auto mb-2 text-blue-500" />
                <p className="text-xs text-gray-600 mb-2">{day.condition}</p>
                <div className="space-y-1">
                  <p className="text-sm font-semibold">{day.high}°</p>
                  <p className="text-sm text-gray-600">{day.low}°</p>
                  <div className="flex items-center justify-center space-x-1">
                    <Droplets className="h-3 w-3 text-blue-500" />
                    <span className="text-xs text-blue-600">{day.rain}%</span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default WeatherMonitor;