import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import '../App.css';

const Unauthorized = () => {
  const navigate = useNavigate();
  const { logout } = useAuth();

  const handleGoBack = () => {
    navigate(-1);
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Access Denied</h1>
      </header>
      
      <main className="App-main">
        <section className="welcome-section">
          <h3>Unauthorized Access</h3>
          <p>You don't have permission to access this page.</p>
          <div style={{ marginTop: '2rem', display: 'flex', gap: '1rem', justifyContent: 'center' }}>
            <button 
              onClick={handleGoBack}
              style={{
                padding: '0.75rem 1.5rem',
                background: '#667eea',
                color: 'white',
                border: 'none',
                borderRadius: '6px',
                cursor: 'pointer',
                fontWeight: '600'
              }}
            >
              Go Back
            </button>
            <button 
              onClick={handleLogout}
              style={{
                padding: '0.75rem 1.5rem',
                background: '#666',
                color: 'white',
                border: 'none',
                borderRadius: '6px',
                cursor: 'pointer',
                fontWeight: '600'
              }}
            >
              Logout
            </button>
          </div>
        </section>
      </main>
    </div>
  );
};

export default Unauthorized;
