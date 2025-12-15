# Unified gradient theme for entire application
unified_css = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
}

.App {
  min-height: 100vh;
}

/* ========== HOMEPAGE ========== */
.homepage {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  position: relative;
  overflow: hidden;
}

.homepage::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
  background-size: 50px 50px;
  animation: moveBackground 20s linear infinite;
}

@keyframes moveBackground {
  0% { transform: translate(0, 0); }
  100% { transform: translate(50px, 50px); }
}

.homepage-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 3rem;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  position: relative;
  z-index: 10;
}

.homepage-header .logo {
  font-size: 2rem;
  margin: 0;
  font-weight: 800;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.btn-header-login {
  background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
  color: #667eea;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 25px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.btn-header-login:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.homepage-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  position: relative;
  z-index: 1;
}

.hero-section {
  text-align: center;
  padding: 4rem 2rem;
  animation: fadeIn 1s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero-section h1 {
  font-size: 4.5rem;
  margin-bottom: 1rem;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.3);
  font-weight: 900;
}

.tagline {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  font-weight: 300;
  opacity: 0.95;
}

.description {
  font-size: 1.3rem;
  max-width: 700px;
  margin: 0 auto 2.5rem;
  line-height: 1.8;
  opacity: 0.9;
}

.btn-get-started {
  background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
  color: #667eea;
  border: none;
  padding: 1.3rem 3.5rem;
  font-size: 1.3rem;
  font-weight: 700;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.btn-get-started:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
}

.features-section {
  padding: 4rem 2rem;
}

.features-section h2 {
  text-align: center;
  font-size: 3rem;
  margin-bottom: 3rem;
  font-weight: 800;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.feature-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.05) 100%);
  backdrop-filter: blur(10px);
  padding: 2.5rem;
  border-radius: 25px;
  text-align: center;
  transition: all 0.4s;
  border: 1px solid rgba(255, 255, 255, 0.3);
  cursor: pointer;
}

.feature-card:hover {
  transform: translateY(-15px) scale(1.03);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.15) 100%);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
}

.feature-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
  display: inline-block;
  transition: transform 0.3s;
}

.feature-card:hover .feature-icon {
  transform: scale(1.3) rotate(10deg);
}

.feature-card h3 {
  font-size: 1.6rem;
  margin-bottom: 0.8rem;
  font-weight: 700;
}

.feature-card p {
  font-size: 1.1rem;
  opacity: 0.9;
  line-height: 1.6;
}

.cta-section {
  text-align: center;
  padding: 3rem 2rem;
}

.cta-section h2 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  font-weight: 800;
}

.btn-login {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0.1) 100%);
  color: white;
  border: 2px solid white;
  padding: 1.2rem 3rem;
  font-size: 1.2rem;
  font-weight: 700;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s;
  backdrop-filter: blur(10px);
}

.btn-login:hover {
  background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
  color: #667eea;
  transform: scale(1.08);
}

/* ========== LOGIN PAGE ========== */
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  position: relative;
  overflow: hidden;
}

.login-page::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
  background-size: 50px 50px;
  animation: moveBackground 20s linear infinite;
}

.login-container {
  background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.9) 100%);
  backdrop-filter: blur(20px);
  padding: 3rem;
  border-radius: 30px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.3);
  max-width: 450px;
  width: 100%;
  animation: slideUp 0.5s ease-out;
  border: 1px solid rgba(255,255,255,0.5);
  position: relative;
  z-index: 10;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.login-container h2 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
  text-align: center;
  font-size: 2.2rem;
  font-weight: 800;
}

.login-subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 2rem;
  font-size: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-weight: 700;
}

.form-group input {
  width: 100%;
  padding: 1rem;
  border: 2px solid #e0e0e0;
  border-radius: 15px;
  font-size: 1rem;
  transition: all 0.3s;
  background: white;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.btn {
  width: 100%;
  padding: 1.1rem;
  border: none;
  border-radius: 15px;
  font-size: 1.1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 1rem;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: linear-gradient(135deg, #f5f5f5 0%, #e0e0e0 100%);
  color: #333;
}

.btn-secondary:hover {
  background: linear-gradient(135deg, #e0e0e0 0%, #d0d0d0 100%);
}

.error-message {
  background: linear-gradient(135deg, #fee 0%, #fdd 100%);
  color: #c33;
  padding: 1rem;
  border-radius: 15px;
  margin-bottom: 1rem;
  text-align: center;
  font-weight: 600;
  border: 1px solid #fcc;
}

/* ========== DASHBOARD ========== */
.dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.dashboard-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1.8rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.15);
}

.dashboard-header h1 {
  font-size: 2.2rem;
  font-weight: 800;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-badge {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0.2) 100%);
  padding: 0.7rem 1.3rem;
  border-radius: 25px;
  font-size: 0.95rem;
  font-weight: 600;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.3);
}

.btn-logout {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.15) 100%);
  color: white;
  border: 2px solid white;
  padding: 0.7rem 1.8rem;
  border-radius: 15px;
  cursor: pointer;
  font-weight: 700;
  transition: all 0.3s;
  backdrop-filter: blur(10px);
}

.btn-logout:hover {
  background: white;
  color: #667eea;
  transform: translateY(-2px);
}

.dashboard-nav {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 1.2rem 2rem;
  box-shadow: 0 3px 15px rgba(0, 0, 0, 0.08);
  display: flex;
  gap: 1rem;
  overflow-x: auto;
}

.nav-btn {
  padding: 1rem 1.8rem;
  border: none;
  background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
  border-radius: 15px;
  cursor: pointer;
  font-weight: 700;
  transition: all 0.3s;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.nav-btn:hover {
  background: linear-gradient(135deg, #e8e8e8 0%, #d8d8d8 100%);
  transform: translateY(-3px);
}

.nav-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

.nav-icon {
  font-size: 1.4rem;
}

.dashboard-content {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

/* Notification */
.notification {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 1.2rem 1.8rem;
  border-radius: 15px;
  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.3);
  z-index: 1000;
  animation: slideInRight 0.3s ease-out;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.7rem;
}

@keyframes slideInRight {
  from { transform: translateX(400px); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

.notification-success {
  background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
  color: white;
}

.notification-error {
  background: linear-gradient(135deg, #f44336 0%, #e53935 100%);
  color: white;
}

/* Loading */
.loading-container {
  text-align: center;
  padding: 5rem;
}

.spinner {
  border: 5px solid #f3f3f3;
  border-top: 5px solid #667eea;
  border-radius: 50%;
  width: 70px;
  height: 70px;
  animation: spin 1s linear infinite;
  margin: 0 auto 1.5rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 2rem;
  border-radius: 25px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 1.5rem;
  transition: all 0.3s;
  border: 1px solid rgba(102, 126, 234, 0.1);
}

.stat-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  font-size: 4rem;
  opacity: 0.9;
}

.stat-info h3 {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 1px;
}

.stat-value {
  font-size: 3rem;
  font-weight: 900;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-card-crops .stat-icon { color: #4caf50; }
.stat-card-fields .stat-icon { color: #2196f3; }
.stat-card-activities .stat-icon { color: #ff9800; }
.stat-card-inventory .stat-icon { color: #9c27b0; }

/* Weather Card */
.weather-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2.5rem;
  border-radius: 25px;
  box-shadow: 0 10px 35px rgba(102, 126, 234, 0.4);
  margin-bottom: 2rem;
}

.weather-card h3 {
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
  font-weight: 800;
}

.weather-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1.5rem;
}

.weather-item {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.1) 100%);
  padding: 1.2rem;
  border-radius: 15px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.3);
}

.weather-label {
  color: rgba(255, 255, 255, 0.9);
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.weather-value {
  font-size: 2rem;
  font-weight: 800;
}

/* Quick Actions */
.quick-actions {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 2.5rem;
  border-radius: 25px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.quick-actions h3 {
  margin-bottom: 1.5rem;
  color: #333;
  font-size: 1.8rem;
  font-weight: 800;
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.action-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 1.3rem;
  border-radius: 18px;
  cursor: pointer;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  transition: all 0.3s;
  font-size: 1.05rem;
}

.action-btn:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 35px rgba(102, 126, 234, 0.5);
}

.action-icon {
  font-size: 2rem;
}

/* Content Card */
.content-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 2.5rem;
  border-radius: 25px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.1);
  margin-bottom: 2rem;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.card-header h2 {
  color: #333;
  font-size: 2rem;
  font-weight: 800;
}

.header-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-input {
  padding: 1rem 1.3rem;
  border: 2px solid #e0e0e0;
  border-radius: 15px;
  font-size: 1rem;
  min-width: 250px;
  transition: all 0.3s;
  background: white;
}

.search-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

/* Table */
.table-container {
  overflow-x: auto;
  border-radius: 15px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.data-table th {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 1.3rem;
  text-align: left;
  font-weight: 800;
  color: #495057;
  border-bottom: 3px solid #dee2e6;
  text-transform: uppercase;
  font-size: 0.9rem;
  letter-spacing: 1px;
}

.data-table td {
  padding: 1.3rem;
  border-bottom: 1px solid #f0f0f0;
}

.data-table tr {
  transition: all 0.2s;
}

.data-table tr:hover {
  background: linear-gradient(135deg, #f8f9fa 0%, #f0f0f0 100%);
  transform: scale(1.01);
}

.status-badge {
  padding: 0.5rem 1.2rem;
  border-radius: 25px;
  font-size: 0.85rem;
  font-weight: 700;
  display: inline-block;
}

.status-growing {
  background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
  color: #2e7d32;
}

.status-harvested {
  background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
  color: #e65100;
}

.status-planted {
  background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
  color: #1565c0;
}

.category-badge {
  padding: 0.5rem 1.2rem;
  border-radius: 25px;
  font-size: 0.85rem;
  background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
  color: #6a1b9a;
  font-weight: 700;
}

/* Buttons */
.btn-add {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 1rem 2rem;
  border-radius: 15px;
  cursor: pointer;
  font-weight: 700;
  transition: all 0.3s;
  font-size: 1.05rem;
}

.btn-add:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5);
}

.btn-edit {
  background: linear-gradient(135deg, #2196f3 0%, #1976d2 100%);
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s;
  margin-right: 0.5rem;
  font-weight: 600;
}

.btn-edit:hover {
  transform: scale(1.08);
  box-shadow: 0 5px 20px rgba(33, 150, 243, 0.5);
}

.btn-delete {
  background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 10px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s;
  font-weight: 600;
}

.btn-delete:hover {
  transform: scale(1.08);
  box-shadow: 0 5px 20px rgba(244, 67, 54, 0.5);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 5rem 2rem;
  color: #999;
}

.empty-icon {
  font-size: 5rem;
  margin-bottom: 1.5rem;
  opacity: 0.5;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.empty-state p {
  font-size: 1.3rem;
  margin-bottom: 2rem;
  color: #666;
  font-weight: 500;
}

/* Responsive */
@media (max-width: 768px) {
  .homepage-header {
    padding: 1rem 1.5rem;
  }

  .homepage-header .logo {
    font-size: 1.5rem;
  }

  .btn-header-login {
    padding: 0.6rem 1.5rem;
    font-size: 0.9rem;
  }

  .hero-section h1 {
    font-size: 2.5rem;
  }

  .dashboard-header {
    flex-direction: column;
    gap: 1rem;
  }

  .dashboard-nav {
    flex-wrap: wrap;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .card-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .header-actions {
    width: 100%;
    flex-direction: column;
  }

  .search-input {
    width: 100%;
  }
}
"""

with open(r'd:\resumeprojects\AgroTrackingProject\frontend\src\App.css', 'w', encoding='utf-8') as f:
    f.write(unified_css)

print('Unified gradient theme applied to all pages!')
