import React, { useState } from 'react';
import { 
  Plus, 
  Calendar, 
  Clock, 
  MapPin, 
  User,
  CheckCircle,
  Droplets,
  Sprout,
  Scissors,
  Zap,
  Filter
} from 'lucide-react';

const ActivityLog = () => {
  const [showAddForm, setShowAddForm] = useState(false);
  const [filter, setFilter] = useState('all');
  const [newActivity, setNewActivity] = useState({
    type: '',
    field: '',
    crop: '',
    date: '',
    time: '',
    notes: '',
    duration: ''
  });

  const activities = [
    {
      id: 1,
      type: 'planting',
      field: 'Field A',
      crop: 'Tomatoes',
      date: '2024-01-15',
      time: '08:00',
      duration: '3 hours',
      notes: 'Planted 200 Roma tomato seedlings',
      status: 'completed',
      worker: 'John Doe'
    },
    {
      id: 2,
      type: 'watering',
      field: 'Field B',
      crop: 'Corn',
      date: '2024-01-16',
      time: '06:30',
      duration: '2 hours',
      notes: 'Sprinkler irrigation system activated',
      status: 'completed',
      worker: 'Jane Smith'
    },
    {
      id: 3,
      type: 'fertilizing',
      field: 'Field C',
      crop: 'Wheat',
      date: '2024-01-17',
      time: '09:00',
      duration: '4 hours',
      notes: 'Applied organic fertilizer NPK 10-10-10',
      status: 'completed',
      worker: 'Mike Johnson'
    },
    {
      id: 4,
      type: 'harvesting',
      field: 'Field C',
      crop: 'Wheat',
      date: '2024-01-18',
      time: '07:00',
      duration: '8 hours',
      notes: 'Harvested 2.5 tons of wheat',
      status: 'in-progress',
      worker: 'Team A'
    },
    {
      id: 5,
      type: 'pest-control',
      field: 'Field D',
      crop: 'Soybeans',
      date: '2024-01-19',
      time: '10:00',
      duration: '1.5 hours',
      notes: 'Applied organic pesticide for aphid control',
      status: 'scheduled',
      worker: 'Sarah Wilson'
    }
  ];

  const getActivityIcon = (type: string) => {
    switch (type) {
      case 'planting': return Sprout;
      case 'watering': return Droplets;
      case 'fertilizing': return Zap;
      case 'harvesting': return Scissors;
      case 'pest-control': return CheckCircle;
      default: return Calendar;
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed': return 'bg-green-100 text-green-800';
      case 'in-progress': return 'bg-blue-100 text-blue-800';
      case 'scheduled': return 'bg-yellow-100 text-yellow-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const filteredActivities = filter === 'all' 
    ? activities 
    : activities.filter(activity => activity.type === filter);

  const handleAddActivity = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Adding activity:', newActivity);
    setShowAddForm(false);
    setNewActivity({ type: '', field: '', crop: '', date: '', time: '', notes: '', duration: '' });
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Activity Log</h2>
          <p className="text-gray-600">Track all farming activities</p>
        </div>
        <button
          onClick={() => setShowAddForm(true)}
          className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg flex items-center space-x-2 transition-colors"
        >
          <Plus className="h-4 w-4" />
          <span>Log Activity</span>
        </button>
      </div>

      {/* Filter Bar */}
      <div className="bg-white rounded-xl p-4 shadow-sm flex items-center space-x-4">
        <Filter className="h-5 w-5 text-gray-400" />
        <select
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          className="border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-500"
        >
          <option value="all">All Activities</option>
          <option value="planting">Planting</option>
          <option value="watering">Watering</option>
          <option value="fertilizing">Fertilizing</option>
          <option value="harvesting">Harvesting</option>
          <option value="pest-control">Pest Control</option>
        </select>
      </div>

      {/* Add Activity Form */}
      {showAddForm && (
        <div className="bg-white rounded-xl p-6 shadow-sm border">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Log New Activity</h3>
          <form onSubmit={handleAddActivity} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Activity Type</label>
              <select
                value={newActivity.type}
                onChange={(e) => setNewActivity({ ...newActivity, type: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              >
                <option value="">Select Activity</option>
                <option value="planting">Planting</option>
                <option value="watering">Watering</option>
                <option value="fertilizing">Fertilizing</option>
                <option value="harvesting">Harvesting</option>
                <option value="pest-control">Pest Control</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Field</label>
              <select
                value={newActivity.field}
                onChange={(e) => setNewActivity({ ...newActivity, field: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              >
                <option value="">Select Field</option>
                <option value="Field A">Field A</option>
                <option value="Field B">Field B</option>
                <option value="Field C">Field C</option>
                <option value="Field D">Field D</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Crop</label>
              <input
                type="text"
                value={newActivity.crop}
                onChange={(e) => setNewActivity({ ...newActivity, crop: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Date</label>
              <input
                type="date"
                value={newActivity.date}
                onChange={(e) => setNewActivity({ ...newActivity, date: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Time</label>
              <input
                type="time"
                value={newActivity.time}
                onChange={(e) => setNewActivity({ ...newActivity, time: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Duration</label>
              <input
                type="text"
                placeholder="e.g., 2 hours"
                value={newActivity.duration}
                onChange={(e) => setNewActivity({ ...newActivity, duration: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium text-gray-700 mb-1">Notes</label>
              <textarea
                value={newActivity.notes}
                onChange={(e) => setNewActivity({ ...newActivity, notes: e.target.value })}
                rows={3}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                placeholder="Additional details about the activity..."
              />
            </div>
            <div className="flex items-end space-x-2">
              <button
                type="submit"
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg transition-colors"
              >
                Log Activity
              </button>
              <button
                type="button"
                onClick={() => setShowAddForm(false)}
                className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-lg transition-colors"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Activities List */}
      <div className="space-y-4">
        {filteredActivities.map((activity) => {
          const ActivityIcon = getActivityIcon(activity.type);
          return (
            <div key={activity.id} className="bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
              <div className="flex items-start space-x-4">
                <div className="p-3 bg-green-100 rounded-lg">
                  <ActivityIcon className="h-6 w-6 text-green-600" />
                </div>
                <div className="flex-1">
                  <div className="flex items-start justify-between mb-2">
                    <div>
                      <h3 className="font-semibold text-gray-900 capitalize">
                        {activity.type.replace('-', ' ')}
                      </h3>
                      <p className="text-sm text-gray-600">{activity.notes}</p>
                    </div>
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(activity.status)}`}>
                      {activity.status.replace('-', ' ')}
                    </span>
                  </div>
                  
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm text-gray-600">
                    <div className="flex items-center space-x-1">
                      <MapPin className="h-4 w-4" />
                      <span>{activity.field}</span>
                    </div>
                    <div className="flex items-center space-x-1">
                      <Sprout className="h-4 w-4" />
                      <span>{activity.crop}</span>
                    </div>
                    <div className="flex items-center space-x-1">
                      <Calendar className="h-4 w-4" />
                      <span>{new Date(activity.date).toLocaleDateString()}</span>
                    </div>
                    <div className="flex items-center space-x-1">
                      <Clock className="h-4 w-4" />
                      <span>{activity.time}</span>
                    </div>
                  </div>
                  
                  <div className="flex items-center justify-between mt-3 pt-3 border-t border-gray-100">
                    <div className="flex items-center space-x-1 text-sm text-gray-600">
                      <User className="h-4 w-4" />
                      <span>{activity.worker}</span>
                    </div>
                    <span className="text-sm font-medium text-gray-700">
                      Duration: {activity.duration}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ActivityLog;