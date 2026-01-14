import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import '../App.css';

const StaffDashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Staff Dashboard</h1>
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
          <h3>Welcome, {user?.full_name}!</h3>
          <p>Email: {user?.email}</p>
          <div style={{ marginTop: '2rem' }}>
            <h4>Staff Features:</h4>
            <ul style={{ textAlign: 'left', lineHeight: '1.8' }}>
              <li>View Patient Enquiries</li>
              <li>Book Appointments</li>
              <li>Check Doctor Availability</li>
              <li>Manage Appointments</li>
              <li>Send Notifications</li>
            </ul>
          </div>
        </section>
      </main>
    </div>
  );
};

export default StaffDashboard;
