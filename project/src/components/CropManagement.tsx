import React, { useState } from 'react';
import { 
  Plus, 
  Sprout, 
  Calendar, 
  Droplets, 
  Sun, 
  MapPin,
  Edit3,
  Trash2,
  Eye
} from 'lucide-react';

const CropManagement = () => {
  const [showAddForm, setShowAddForm] = useState(false);
  const [newCrop, setNewCrop] = useState({
    name: '',
    variety: '',
    field: '',
    plantingDate: '',
    expectedHarvest: '',
    status: 'planted'
  });

  const crops = [
    {
      id: 1,
      name: 'Tomatoes',
      variety: 'Roma',
      field: 'Field A',
      plantingDate: '2024-01-15',
      expectedHarvest: '2024-04-15',
      status: 'growing',
      progress: 65,
      healthScore: 92
    },
    {
      id: 2,
      name: 'Corn',
      variety: 'Sweet Corn',
      field: 'Field B',
      plantingDate: '2024-01-20',
      expectedHarvest: '2024-05-20',
      status: 'growing',
      progress: 45,
      healthScore: 88
    },
    {
      id: 3,
      name: 'Wheat',
      variety: 'Winter Wheat',
      field: 'Field C',
      plantingDate: '2023-12-01',
      expectedHarvest: '2024-02-15',
      status: 'ready',
      progress: 100,
      healthScore: 95
    },
    {
      id: 4,
      name: 'Soybeans',
      variety: 'Organic',
      field: 'Field D',
      plantingDate: '2024-01-10',
      expectedHarvest: '2024-06-10',
      status: 'planted',
      progress: 20,
      healthScore: 85
    }
  ];

  const handleAddCrop = (e: React.FormEvent) => {
    e.preventDefault();
    // Add crop logic would go here
    console.log('Adding crop:', newCrop);
    setShowAddForm(false);
    setNewCrop({ name: '', variety: '', field: '', plantingDate: '', expectedHarvest: '', status: 'planted' });
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'planted': return 'bg-blue-100 text-blue-800';
      case 'growing': return 'bg-green-100 text-green-800';
      case 'ready': return 'bg-yellow-100 text-yellow-800';
      case 'harvested': return 'bg-gray-100 text-gray-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Crop Management</h2>
          <p className="text-gray-600">Monitor and manage your crops</p>
        </div>
        <button
          onClick={() => setShowAddForm(true)}
          className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg flex items-center space-x-2 transition-colors"
        >
          <Plus className="h-4 w-4" />
          <span>Add Crop</span>
        </button>
      </div>

      {/* Add Crop Form */}
      {showAddForm && (
        <div className="bg-white rounded-xl p-6 shadow-sm border">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Add New Crop</h3>
          <form onSubmit={handleAddCrop} className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Crop Name</label>
              <input
                type="text"
                value={newCrop.name}
                onChange={(e) => setNewCrop({ ...newCrop, name: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Variety</label>
              <input
                type="text"
                value={newCrop.variety}
                onChange={(e) => setNewCrop({ ...newCrop, variety: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Field</label>
              <select
                value={newCrop.field}
                onChange={(e) => setNewCrop({ ...newCrop, field: e.target.value })}
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
              <label className="block text-sm font-medium text-gray-700 mb-1">Planting Date</label>
              <input
                type="date"
                value={newCrop.plantingDate}
                onChange={(e) => setNewCrop({ ...newCrop, plantingDate: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Expected Harvest</label>
              <input
                type="date"
                value={newCrop.expectedHarvest}
                onChange={(e) => setNewCrop({ ...newCrop, expectedHarvest: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              />
            </div>
            <div className="flex items-end space-x-2">
              <button
                type="submit"
                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg transition-colors"
              >
                Add Crop
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

      {/* Crops Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {crops.map((crop) => (
          <div key={crop.id} className="bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow">
            <div className="flex items-start justify-between mb-4">
              <div className="flex items-center space-x-3">
                <div className="p-2 bg-green-100 rounded-lg">
                  <Sprout className="h-6 w-6 text-green-600" />
                </div>
                <div>
                  <h3 className="font-semibold text-gray-900">{crop.name}</h3>
                  <p className="text-sm text-gray-600">{crop.variety}</p>
                </div>
              </div>
              <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(crop.status)}`}>
                {crop.status}
              </span>
            </div>

            <div className="space-y-3 mb-4">
              <div className="flex items-center space-x-2 text-sm text-gray-600">
                <MapPin className="h-4 w-4" />
                <span>{crop.field}</span>
              </div>
              <div className="flex items-center space-x-2 text-sm text-gray-600">
                <Calendar className="h-4 w-4" />
                <span>Planted: {new Date(crop.plantingDate).toLocaleDateString()}</span>
              </div>
              <div className="flex items-center space-x-2 text-sm text-gray-600">
                <Sun className="h-4 w-4" />
                <span>Harvest: {new Date(crop.expectedHarvest).toLocaleDateString()}</span>
              </div>
            </div>

            {/* Progress Bar */}
            <div className="mb-4">
              <div className="flex justify-between text-sm text-gray-600 mb-1">
                <span>Growth Progress</span>
                <span>{crop.progress}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div 
                  className="bg-green-500 h-2 rounded-full transition-all duration-300"
                  style={{ width: `${crop.progress}%` }}
                ></div>
              </div>
            </div>

            {/* Health Score */}
            <div className="flex items-center justify-between mb-4">
              <span className="text-sm text-gray-600">Health Score</span>
              <div className="flex items-center space-x-2">
                <Droplets className="h-4 w-4 text-blue-500" />
                <span className="font-semibold text-green-600">{crop.healthScore}%</span>
              </div>
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

export default CropManagement;