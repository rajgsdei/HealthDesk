# HealthDesk Frontend

React-based frontend for the HealthDesk healthcare management system.

## Features

- Modern React with Vite for fast development
- Responsive UI design
- API integration with backend
- Patient enquiry submission

## Tech Stack

- **Framework**: React 18
- **Build Tool**: Vite
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Styling**: CSS3

## Project Structure

```
Frontend/
├── src/
│   ├── App.jsx                # Main App component
│   ├── App.css                # App styles
│   ├── main.jsx               # Application entry point
│   └── index.css              # Global styles
├── index.html                 # HTML template
├── vite.config.js             # Vite configuration
├── package.json               # Dependencies
└── .env.example               # Environment variables template
```

## Setup Instructions

### 1. Prerequisites

- Node.js 16 or higher
- npm or yarn

### 2. Install Dependencies

```bash
# Navigate to Frontend directory
cd Frontend

# Install dependencies
npm install
```

### 3. Configure Environment Variables (Optional)

```bash
# Copy the example env file
cp .env.example .env

# Edit .env if you need to change the API URL
```

### 4. Run the Development Server

```bash
npm run dev
```

The application will be available at: `http://localhost:3000`

## Available Scripts

- `npm run dev` - Start development server with hot-reload
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Configuration

### Proxy Setup

The Vite config includes a proxy to forward `/api` requests to the backend at `http://localhost:8000`. This is configured in [vite.config.js](vite.config.js).

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
VITE_API_URL=http://localhost:8000/api
```

## Development

The app is configured with:
- Hot Module Replacement (HMR) for instant updates
- Proxy to backend API for seamless development
- Port 3000 for the dev server

## Building for Production

```bash
# Create optimized production build
npm run build

# Preview the production build
npm run preview
```

The build output will be in the `dist/` directory.

## Next Steps

- Create enquiry submission form
- Add appointment booking interface
- Implement user authentication UI
- Add doctor selection and availability view
- Create patient dashboard
- Add clinical guidelines search interface

## Troubleshooting

**Port Already in Use:**
- Change the port in [vite.config.js](vite.config.js) (default is 3000)

**API Connection Failed:**
- Ensure the backend is running at `http://localhost:8000`
- Check that CORS is properly configured in the backend
- Verify the proxy settings in [vite.config.js](vite.config.js)

**Module Not Found:**
- Delete `node_modules` and `package-lock.json`
- Run `npm install` again
