import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import '../App.css';

const Dashboard = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>HealthDesk Dashboard</h1>
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
          <p>Role: <strong>{user?.role}</strong></p>
          <p>Email: {user?.email}</p>
          <p>This is your general dashboard.</p>
        </section>
      </main>
    </div>
  );
};

export default Dashboard;
