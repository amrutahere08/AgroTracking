import React, { useState } from 'react';
import { 
  Plus, 
  MapPin, 
  Ruler, 
  Droplets, 
  Thermometer,
  Edit3,
  Trash2,
  Eye,
  Sprout
} from 'lucide-react';

const FieldManagement = () => {
  const [showAddForm, setShowAddForm] = useState(false);
  const [newField, setNewField] = useState({
    name: '',
    area: '',
    soilType: '',
    location: '',
    notes: ''
  });

  const fields = [
    {
      id: 1,
      name: 'Field A',
      area: '5.2 acres',
      soilType: 'Clay Loam',
      location: 'North Section',
      currentCrop: 'Tomatoes',
      soilPH: 6.8,
      moisture: 65,
      temperature: 24,
      status: 'active',
      lastActivity: '2024-01-15'
    },
    {
      id: 2,
      name: 'Field B',
      area: '3.8 acres',
      soilType: 'Sandy Loam',
      location: 'East Section',
      currentCrop: 'Corn',
      soilPH: 7.2,
      moisture: 58,
      temperature: 26,
      status: 'active',
      lastActivity: '2024-01-20'
    },
    {
      id: 3,
      name: 'Field C',
      area: '4.5 acres',
      soilType: 'Silt Loam',
      location: 'South Section',
      currentCrop: 'Wheat',
      soilPH: 6.5,
      moisture: 72,
      temperature: 22,
      status: 'ready',
      lastActivity: '2024-01-12'
    },
    {
      id: 4,
      name: 'Field D',
      area: '6.1 acres',
      soilType: 'Clay',
      location: 'West Section',
      currentCrop: 'Soybeans',
      soilPH: 7.0,
      moisture: 61,
      temperature: 25,
      status: 'preparation',
      lastActivity: '2024-01-10'
    }
  ];

  const handleAddField = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Adding field:', newField);
    setShowAddForm(false);
    setNewField({ name: '', area: '', soilType: '', location: '', notes: '' });
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'bg-green-100 text-green-800';
      case 'ready': return 'bg-yellow-100 text-yellow-800';
      case 'preparation': return 'bg-blue-100 text-blue-800';
      case 'fallow': return 'bg-gray-100 text-gray-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const getMoistureColor = (moisture: number) => {
    if (moisture < 40) return 'text-red-600';
    if (moisture < 60) return 'text-yellow-600';
    return 'text-green-600';
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Field Management</h2>
          <p className="text-gray-600">Monitor and manage your fields</p>
        </div>
        <button
          onClick={() => setShowAddForm(true)}
          className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg flex items-center space-x-2 transition-colors"
        >
          <Plus className="h-4 w-4" />
          <span>Add Field</span>
        </button>
      </div>

      {/* Add Field Form */}
      {showAddForm && (
        <div className="bg-white rounded-xl p-6 shadow-sm border">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Add New Field</h3>
          <form onSubmit={handleAddField} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Field Name</label>
              <input
                type="text"
                value={newField.name}
                onChange={(e) => setNewField({ ...newField, name: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Area (acres)</label>
              <input
                type="text"
                value={newField.area}
                onChange={(e) => setNewField({ ...newField, area: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Soil Type</label>
              <select
                value={newField.soilType}
                onChange={(e) => setNewField({ ...newField, soilType: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              >
                <option value="">Select Soil Type</option>
                <option value="Clay">Clay</option>
                <option value="Sandy Loam">Sandy Loam</option>
                <option value="Clay Loam">Clay Loam</option>
                <option value="Silt Loam">Silt Loam</option>
                <option value="Sandy">Sandy</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Location</label>
              <input
                type="text"
                value={newField.location}
                onChange={(e) => setNewField({ ...newField, location: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div className="md:col-span-2">
              <label className="block text-sm font-medium text-gray-700 mb-1">Notes</label>
              <textarea
                value={newField.notes}
                onChange={(e) => setNewField({ ...newField, notes: e.target.value })}
                rows={3}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
            <div className="flex items-end space-x-2">
              <button
                type="submit"
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg transition-colors"
              >
                Add Field
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

      {/* Fields Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {fields.map((field) => (
          <div key={field.id} className="bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
            <div className="flex items-start justify-between mb-4">
              <div className="flex items-center space-x-3">
                <div className="p-2 bg-green-100 rounded-lg">
                  <MapPin className="h-6 w-6 text-green-600" />
                </div>
                <div>
                  <h3 className="font-semibold text-gray-900">{field.name}</h3>
                  <p className="text-sm text-gray-600">{field.location}</p>
                </div>
              </div>
              <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(field.status)}`}>
                {field.status}
              </span>
            </div>

            <div className="grid grid-cols-2 gap-4 mb-4">
              <div className="flex items-center space-x-2">
                <Ruler className="h-4 w-4 text-gray-400" />
                <div>
                  <p className="text-sm text-gray-600">Area</p>
                  <p className="font-semibold">{field.area}</p>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <Sprout className="h-4 w-4 text-gray-400" />
                <div>
                  <p className="text-sm text-gray-600">Current Crop</p>
                  <p className="font-semibold">{field.currentCrop}</p>
                </div>
              </div>
            </div>

            <div className="space-y-3 mb-4">
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">Soil Type</span>
                <span className="font-medium">{field.soilType}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">Soil pH</span>
                <span className="font-medium">{field.soilPH}</span>
              </div>
            </div>

            {/* Environmental Conditions */}
            <div className="grid grid-cols-2 gap-4 mb-4 p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center space-x-2">
                <Droplets className="h-4 w-4 text-blue-500" />
                <div>
                  <p className="text-xs text-gray-600">Moisture</p>
                  <p className={`font-semibold ${getMoistureColor(field.moisture)}`}>
                    {field.moisture}%
                  </p>
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <Thermometer className="h-4 w-4 text-orange-500" />
                <div>
                  <p className="text-xs text-gray-600">Temperature</p>
                  <p className="font-semibold">{field.temperature}°C</p>
                </div>
              </div>
            </div>

            <div className="text-sm text-gray-600 mb-4">
              Last Activity: {new Date(field.lastActivity).toLocaleDateString()}
            </div>

            {/* Actions */}
            <div className="flex space-x-2 pt-4 border-t border-gray-100">
              <button className="flex-1 bg-blue-50 hover:bg-blue-100 text-blue-600 px-3 py-2 rounded-lg text-sm flex items-center justify-center space-x-1 transition-colors">
                <Eye className="h-4 w-4" />
                <span>View</span>
              </button>
              <button className="flex-1 bg-green-50 hover:bg-green-100 text-green-600 px-3 py-2 rounded-lg text-sm flex items-center justify-center space-x-1 transition-colors">
                <Edit3 className="h-4 w-4" />
                <span>Edit</span>
              </button>
              <button className="bg-red-50 hover:bg-red-100 text-red-600 px-3 py-2 rounded-lg text-sm transition-colors">
                <Trash2 className="h-4 w-4" />
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FieldManagement;