# Ultra-professional theme with 3D realistic icons
professional_css = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.App {
  min-height: 100vh;
}

/* 3D Icon Effects */
.icon-3d {
  display: inline-block;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
  transform-style: preserve-3d;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.icon-3d:hover {
  transform: translateZ(20px) rotateY(15deg) rotateX(10deg);
  filter: drop-shadow(0 8px 16px rgba(0,0,0,0.4));
}

/* Homepage */
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
  background: radial-gradient(circle, rgba(255,255,255,0.08) 1px, transparent 1px);
  background-size: 40px 40px;
  animation: moveBackground 25s linear infinite;
}

@keyframes moveBackground {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(40px, 40px) rotate(360deg); }
}

.homepage-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 3rem;
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(30px) saturate(180%);
  border-bottom: 1px solid rgba(255, 255, 255, 0.25);
  position: relative;
  z-index: 10;
  box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.homepage-header .logo {
  font-size: 2rem;
  margin: 0;
  font-weight: 900;
  text-shadow: 0 4px 12px rgba(0,0,0,0.3);
  letter-spacing: -0.5px;
}

.btn-header-login {
  background: linear-gradient(135deg, #fff 0%, #f8f8f8 100%);
  color: #667eea;
  border: none;
  padding: 0.9rem 2.2rem;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25), inset 0 -2px 8px rgba(0,0,0,0.1);
  position: relative;
  overflow: hidden;
}

.btn-header-login::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
  transition: left 0.5s;
}

.btn-header-login:hover::before {
  left: 100%;
}

.btn-header-login:hover {
  transform: translateY(-4px) scale(1.05);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35), inset 0 -2px 8px rgba(0,0,0,0.1);
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
  padding: 5rem 2rem;
  animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero-section h1 {
  font-size: 5rem;
  margin-bottom: 1.5rem;
  text-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
  font-weight: 900;
  letter-spacing: -2px;
}

.tagline {
  font-size: 2.2rem;
  margin-bottom: 1.5rem;
  font-weight: 300;
  opacity: 0.95;
  letter-spacing: -0.5px;
}

.description {
  font-size: 1.3rem;
  max-width: 750px;
  margin: 0 auto 3rem;
  line-height: 1.8;
  opacity: 0.92;
}

.btn-get-started {
  background: linear-gradient(135deg, #fff 0%, #f5f5f5 100%);
  color: #667eea;
  border: none;
  padding: 1.4rem 4rem;
  font-size: 1.4rem;
  font-weight: 800;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35), inset 0 -3px 10px rgba(0,0,0,0.1);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.btn-get-started:hover {
  transform: translateY(-6px) scale(1.05);
  box-shadow: 0 18px 50px rgba(0, 0, 0, 0.45), inset 0 -3px 10px rgba(0,0,0,0.1);
}

.features-section {
  padding: 5rem 2rem;
}

.features-section h2 {
  text-align: center;
  font-size: 3.5rem;
  margin-bottom: 4rem;
  font-weight: 900;
  text-shadow: 0 4px 16px rgba(0,0,0,0.3);
  letter-spacing: -1px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2.5rem;
  margin-bottom: 3rem;
}

.feature-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.18) 0%, rgba(255, 255, 255, 0.08) 100%);
  backdrop-filter: blur(20px) saturate(180%);
  padding: 3rem;
  border-radius: 30px;
  text-align: center;
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 1px solid rgba(255, 255, 255, 0.35);
  cursor: pointer;
  box-shadow: 0 8px 32px rgba(0,0,0,0.15);
}

.feature-card:hover {
  transform: translateY(-20px) scale(1.03);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.28) 0%, rgba(255, 255, 255, 0.18) 100%);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
  border-color: rgba(255, 255, 255, 0.5);
}

.feature-icon {
  font-size: 5rem;
  margin-bottom: 1.5rem;
  display: inline-block;
  filter: drop-shadow(0 8px 16px rgba(0,0,0,0.4));
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  transform-style: preserve-3d;
}

.feature-card:hover .feature-icon {
  transform: translateZ(30px) rotateY(20deg) scale(1.3);
  filter: drop-shadow(0 12px 24px rgba(0,0,0,0.5));
}

.feature-card h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  font-weight: 800;
  letter-spacing: -0.5px;
}

.feature-card p {
  font-size: 1.1rem;
  opacity: 0.92;
  line-height: 1.7;
}

.cta-section {
  text-align: center;
  padding: 4rem 2rem;
}

.cta-section h2 {
  font-size: 2.8rem;
  margin-bottom: 2.5rem;
  font-weight: 900;
  text-shadow: 0 4px 16px rgba(0,0,0,0.3);
}

.btn-login {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.35) 0%, rgba(255, 255, 255, 0.15) 100%);
  color: white;
  border: 2px solid rgba(255,255,255,0.6);
  padding: 1.3rem 3.5rem;
  font-size: 1.3rem;
  font-weight: 800;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  backdrop-filter: blur(15px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}

.btn-login:hover {
  background: linear-gradient(135deg, #fff 0%, #f5f5f5 100%);
  color: #667eea;
  transform: scale(1.08);
  box-shadow: 0 12px 32px rgba(0,0,0,0.35);
}

/* Login Page */
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
  background: radial-gradient(circle, rgba(255,255,255,0.08) 1px, transparent 1px);
  background-size: 40px 40px;
  animation: moveBackground 25s linear infinite;
}

.login-container {
  background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(255,255,255,0.95) 100%);
  backdrop-filter: blur(30px) saturate(180%);
  padding: 3.5rem;
  border-radius: 35px;
  box-shadow: 0 40px 100px rgba(0,0,0,0.4);
  max-width: 480px;
  width: 100%;
  animation: slideUpScale 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 1px solid rgba(255,255,255,0.6);
  position: relative;
  z-index: 10;
}

@keyframes slideUpScale {
  from { opacity: 0; transform: translateY(50px) scale(0.9); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

.login-container h2 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.8rem;
  text-align: center;
  font-size: 2.5rem;
  font-weight: 900;
  letter-spacing: -1px;
}

.login-subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 2.5rem;
  font-size: 1.05rem;
  font-weight: 500;
}

.form-group {
  margin-bottom: 1.8rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.7rem;
  color: #333;
  font-weight: 800;
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.form-group input {
  width: 100%;
  padding: 1.1rem 1.3rem;
  border: 2px solid #e0e0e0;
  border-radius: 18px;
  font-size: 1.05rem;
  transition: all 0.3s;
  background: white;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 5px rgba(102, 126, 234, 0.12), inset 0 2px 4px rgba(0,0,0,0.05);
  transform: translateY(-2px);
}

.btn {
  width: 100%;
  padding: 1.2rem;
  border: none;
  border-radius: 18px;
  font-size: 1.15rem;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  margin-top: 1rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
}

.btn-primary:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(102, 126, 234, 0.5);
}

.btn-secondary {
  background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
  color: #333;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.btn-secondary:hover {
  background: linear-gradient(135deg, #e8e8e8 0%, #d8d8d8 100%);
  transform: translateY(-2px);
}

.error-message {
  background: linear-gradient(135deg, #fee 0%, #fdd 100%);
  color: #c33;
  padding: 1.1rem;
  border-radius: 18px;
  margin-bottom: 1.5rem;
  text-align: center;
  font-weight: 700;
  border: 2px solid #fcc;
  box-shadow: 0 4px 12px rgba(255,0,0,0.15);
}

/* Dashboard */
.dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.dashboard-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem 2.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.dashboard-header h1 {
  font-size: 2.5rem;
  font-weight: 900;
  text-shadow: 0 4px 12px rgba(0,0,0,0.3);
  letter-spacing: -1px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1.2rem;
}

.user-badge {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.35) 0%, rgba(255, 255, 255, 0.25) 100%);
  padding: 0.8rem 1.5rem;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: 700;
  backdrop-filter: blur(15px);
  border: 1px solid rgba(255,255,255,0.4);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.btn-logout {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0.2) 100%);
  color: white;
  border: 2px solid rgba(255,255,255,0.6);
  padding: 0.8rem 2rem;
  border-radius: 18px;
  cursor: pointer;
  font-weight: 800;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  backdrop-filter: blur(15px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.btn-logout:hover {
  background: white;
  color: #667eea;
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}

.dashboard-nav {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 1.5rem 2.5rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  display: flex;
  gap: 1.2rem;
  overflow-x: auto;
}

.nav-btn {
  padding: 1.1rem 2rem;
  border: none;
  background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
  border-radius: 18px;
  cursor: pointer;
  font-weight: 800;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 0.7rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  font-size: 1rem;
}

.nav-btn:hover {
  background: linear-gradient(135deg, #e8e8e8 0%, #d8d8d8 100%);
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.nav-btn.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.5);
  transform: translateY(-2px);
}

.nav-icon {
  font-size: 1.6rem;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
}

.dashboard-content {
  padding: 2.5rem;
  max-width: 1400px;
  margin: 0 auto;
}

/* Notification */
.notification {
  position: fixed;
  top: 25px;
  right: 25px;
  padding: 1.3rem 2rem;
  border-radius: 18px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
  z-index: 1000;
  animation: slideInRight 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-size: 1.05rem;
}

@keyframes slideInRight {
  from { transform: translateX(500px); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

.notification-success {
  background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
  color: white;
  border: 2px solid #66bb6a;
}

.notification-error {
  background: linear-gradient(135deg, #f44336 0%, #e53935 100%);
  color: white;
  border: 2px solid #ef5350;
}

/* Loading */
.loading-container {
  text-align: center;
  padding: 6rem;
}

.spinner {
  border: 6px solid #f3f3f3;
  border-top: 6px solid #667eea;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  animation: spin 1s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
  margin: 0 auto 2rem;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-bottom: 2.5rem;
}

.stat-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 2.5rem;
  border-radius: 30px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  display: flex;
  align-items: center;
  gap: 2rem;
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 1px solid rgba(102, 126, 234, 0.15);
}

.stat-card:hover {
  transform: translateY(-12px) scale(1.02);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
}

.stat-icon {
  font-size: 5rem;
  filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));
  transform-style: preserve-3d;
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.stat-card:hover .stat-icon {
  transform: translateZ(25px) rotateY(15deg) scale(1.15);
  filter: drop-shadow(0 12px 24px rgba(0,0,0,0.4));
}

.stat-info h3 {
  color: #666;
  font-size: 0.95rem;
  margin-bottom: 0.7rem;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 1.5px;
}

.stat-value {
  font-size: 3.5rem;
  font-weight: 900;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -2px;
}

.stat-card-crops .stat-icon { color: #4caf50; }
.stat-card-fields .stat-icon { color: #2196f3; }
.stat-card-activities .stat-icon { color: #ff9800; }
.stat-card-inventory .stat-icon { color: #9c27b0; }

/* Weather Card */
.weather-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 3rem;
  border-radius: 30px;
  box-shadow: 0 12px 40px rgba(102, 126, 234, 0.5);
  margin-bottom: 2.5rem;
}

.weather-card h3 {
  margin-bottom: 2rem;
  font-size: 2rem;
  font-weight: 900;
  text-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

.weather-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 1.8rem;
}

.weather-item {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.15) 100%);
  padding: 1.5rem;
  border-radius: 20px;
  backdrop-filter: blur(15px);
  border: 1px solid rgba(255,255,255,0.4);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transition: all 0.3s;
}

.weather-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}

.weather-label {
  color: rgba(255, 255, 255, 0.95);
  font-size: 0.95rem;
  margin-bottom: 0.7rem;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 1px;
}

.weather-value {
  font-size: 2.2rem;
  font-weight: 900;
  text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

/* Quick Actions */
.quick-actions {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 3rem;
  border-radius: 30px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  margin-bottom: 2.5rem;
}

.quick-actions h3 {
  margin-bottom: 2rem;
  color: #333;
  font-size: 2rem;
  font-weight: 900;
  letter-spacing: -0.5px;
}

.action-buttons {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
}

.action-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 1.5rem;
  border-radius: 22px;
  cursor: pointer;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  font-size: 1.1rem;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
}

.action-btn:hover {
  transform: translateY(-8px) scale(1.03);
  box-shadow: 0 16px 40px rgba(102, 126, 234, 0.6);
}

.action-icon {
  font-size: 2.5rem;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
}

/* Content Card */
.content-card {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  padding: 3rem;
  border-radius: 30px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
  margin-bottom: 2.5rem;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.card-header h2 {
  color: #333;
  font-size: 2.2rem;
  font-weight: 900;
  letter-spacing: -0.5px;
}

.header-actions {
  display: flex;
  gap: 1.2rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-input {
  padding: 1.1rem 1.5rem;
  border: 2px solid #e0e0e0;
  border-radius: 18px;
  font-size: 1.05rem;
  min-width: 280px;
  transition: all 0.3s;
  background: white;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
}

.search-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 5px rgba(102, 126, 234, 0.12), inset 0 2px 4px rgba(0,0,0,0.05);
  transform: translateY(-2px);
}

/* Table */
.table-container {
  overflow-x: auto;
  border-radius: 20px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1.5rem;
}

.data-table th {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 1.5rem;
  text-align: left;
  font-weight: 900;
  color: #495057;
  border-bottom: 3px solid #dee2e6;
  text-transform: uppercase;
  font-size: 0.95rem;
  letter-spacing: 1.5px;
}

.data-table td {
  padding: 1.5rem;
  border-bottom: 1px solid #f0f0f0;
  font-size: 1.05rem;
}

.data-table tr {
  transition: all 0.3s;
}

.data-table tr:hover {
  background: linear-gradient(135deg, #f8f9fa 0%, #f0f0f0 100%);
  transform: scale(1.01);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.status-badge {
  padding: 0.6rem 1.3rem;
  border-radius: 30px;
  font-size: 0.9rem;
  font-weight: 800;
  display: inline-block;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-growing {
  background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
  color: #2e7d32;
  box-shadow: 0 2px 8px rgba(46, 125, 50, 0.2);
}

.status-harvested {
  background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
  color: #e65100;
  box-shadow: 0 2px 8px rgba(230, 81, 0, 0.2);
}

.status-planted {
  background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
  color: #1565c0;
  box-shadow: 0 2px 8px rgba(21, 101, 192, 0.2);
}

.category-badge {
  padding: 0.6rem 1.3rem;
  border-radius: 30px;
  font-size: 0.9rem;
  background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
  color: #6a1b9a;
  font-weight: 800;
  box-shadow: 0 2px 8px rgba(106, 27, 154, 0.2);
}

/* Buttons */
.btn-add {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 1.1rem 2.2rem;
  border-radius: 18px;
  cursor: pointer;
  font-weight: 800;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  font-size: 1.1rem;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-add:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(102, 126, 234, 0.6);
}

.btn-edit {
  background: linear-gradient(135deg, #2196f3 0%, #1976d2 100%);
  color: white;
  border: none;
  padding: 0.7rem 1.4rem;
  border-radius: 12px;
  cursor: pointer;
  font-size: 0.95rem;
  transition: all 0.3s;
  margin-right: 0.7rem;
  font-weight: 700;
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
}

.btn-edit:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 18px rgba(33, 150, 243, 0.5);
}

.btn-delete {
  background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
  color: white;
  border: none;
  padding: 0.7rem 1.4rem;
  border-radius: 12px;
  cursor: pointer;
  font-size: 0.95rem;
  transition: all 0.3s;
  font-weight: 700;
  box-shadow: 0 4px 12px rgba(244, 67, 54, 0.3);
}

.btn-delete:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 18px rgba(244, 67, 54, 0.5);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 6rem 2rem;
  color: #999;
}

.empty-icon {
  font-size: 6rem;
  margin-bottom: 2rem;
  opacity: 0.5;
  animation: bounce 2.5s ease-in-out infinite;
  filter: drop-shadow(0 8px 16px rgba(0,0,0,0.2));
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-25px); }
}

.empty-state p {
  font-size: 1.4rem;
  margin-bottom: 2.5rem;
  color: #666;
  font-weight: 600;
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
    padding: 0.7rem 1.5rem;
    font-size: 0.95rem;
  }

  .hero-section h1 {
    font-size: 3rem;
  }

  .dashboard-header {
    flex-direction: column;
    gap: 1.2rem;
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
    f.write(professional_css)

print('Ultra-professional 3D theme created!')
