import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import '../App.css';

const AdminDashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Admin Dashboard</h1>
        <button 
          onClick={handleLogout}
          style={{
            position: 'absolute',
            top: '1rem',
            right: '1rem',
            padding: '0.5rem 1rem',
            background: 'white',
            color: '#667eea',
            border: 'none',
            borderRadius: '6px',
            cursor: 'pointer',
            fontWeight: '600'
          }}
        >
          Logout
        </button>
      </header>
      
      <main className="App-main">
        <section className="welcome-section">
          <h3>Welcome, Admin {user?.full_name}!</h3>
          <p>Email: {user?.email}</p>
          <div style={{ marginTop: '2rem' }}>
            <h4>Admin Features:</h4>
            <ul style={{ textAlign: 'left', lineHeight: '1.8' }}>
              <li>Manage Users</li>
              <li>View All Enquiries</li>
              <li>Manage Doctors</li>
              <li>System Settings</li>
              <li>View Reports</li>
            </ul>
          </div>
        </section>
      </main>
    </div>
  );
};

export default AdminDashboard;
