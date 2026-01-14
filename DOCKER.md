# HealthDesk Docker Setup

This directory contains Docker configurations for the HealthDesk application.

## Prerequisites

- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Docker Compose v2.0+

## Quick Start

### 1. Build and Run All Services

```bash
docker-compose up --build
```

This will start:
- **MongoDB** on port 27017
- **API Backend** on port 8000
- **React Frontend** on port 3000

### 2. Access the Application

- **Frontend:** http://localhost:3000
- **API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **MongoDB:** localhost:27017

### 3. Default Credentials

- **Admin User:** admin@healthdesk.com / admin123
- **MongoDB:** admin / adminpassword

## Docker Commands

### Start Services
```bash
# Start all services
docker-compose up

# Start in detached mode (background)
docker-compose up -d

# Start specific service
docker-compose up frontend
```

### Stop Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (clears database)
docker-compose down -v
```

### Rebuild Services
```bash
# Rebuild all services
docker-compose up --build

# Rebuild specific service
docker-compose build api
```

### View Logs
```bash
# View all logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# View specific service logs
docker-compose logs -f api
```

### Execute Commands in Container
```bash
# Access API container bash
docker-compose exec api sh

# Access MongoDB shell
docker-compose exec mongodb mongosh -u admin -p adminpassword

# Run Python commands in API container
docker-compose exec api python -c "print('Hello')"
```

## Services

### MongoDB
- **Image:** mongo:7.0
- **Port:** 27017
- **Data:** Persisted in Docker volume `mongodb_data`
- **Credentials:** admin / adminpassword

### API (FastAPI)
- **Build:** ./Api-Service/Dockerfile
- **Port:** 8000
- **Hot Reload:** Enabled in development
- **Dependencies:** All versions locked from requirements.txt

### Frontend (React + Nginx)
- **Build:** ./Frontend/Dockerfile (multi-stage)
- **Port:** 3000 (mapped to 80 in container)
- **Server:** Nginx 1.25
- **Dependencies:** All versions locked from package-lock.json

## Environment Variables

### API Service
Environment variables can be customized in `docker-compose.yml`:

```yaml
environment:
  - MONGODB_URL=mongodb://admin:adminpassword@mongodb:27017/healthdesk?authSource=admin
  - MONGODB_DB_NAME=healthdesk
  - ALLOWED_ORIGINS=http://localhost:3000,http://localhost
  - PROJECT_NAME=HealthDesk API
  - VERSION=0.1.0
```

### Frontend Service
```yaml
environment:
  - VITE_API_URL=http://localhost:8000/api
```

## Production Deployment

For production, modify `docker-compose.yml`:

1. **Remove hot-reload from API:**
```yaml
command: uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

2. **Use environment-specific compose file:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

3. **Set secure MongoDB credentials**

4. **Use proper CORS origins**

5. **Enable HTTPS with reverse proxy (nginx/traefik)**

## Volume Management

### View Volumes
```bash
docker volume ls
```

### Backup MongoDB Data
```bash
docker-compose exec mongodb mongodump --out /backup
docker cp healthdesk-mongodb:/backup ./backup
```

### Restore MongoDB Data
```bash
docker cp ./backup healthdesk-mongodb:/backup
docker-compose exec mongodb mongorestore /backup
```

## Troubleshooting

### Container won't start
```bash
# Check logs
docker-compose logs api

# Restart specific service
docker-compose restart api
```

### Port already in use
```bash
# Check what's using the port
netstat -ano | findstr :8000

# Change port in docker-compose.yml
ports:
  - "8001:8000"  # Use 8001 instead
```

### MongoDB connection issues
```bash
# Test MongoDB connection
docker-compose exec api python -c "from motor.motor_asyncio import AsyncIOMotorClient; print('OK')"

# Check MongoDB is running
docker-compose ps mongodb
```

### Clear everything and restart
```bash
# Stop all containers
docker-compose down

# Remove all volumes (WARNING: deletes data)
docker-compose down -v

# Remove all images
docker-compose down --rmi all

# Rebuild from scratch
docker-compose up --build
```

## Health Checks

All services include health checks:

```bash
# View health status
docker-compose ps
```

- **MongoDB:** Ping database
- **API:** Check /api/health endpoint
- **Frontend:** Check nginx is serving

## Development vs Production

### Development (Current Setup)
- Hot reload enabled
- Source code mounted as volumes
- Debug logs enabled
- Development dependencies included

### Production Recommendations
- Disable hot reload
- Use production MongoDB with authentication
- Enable HTTPS
- Use environment variables from secrets
- Add rate limiting
- Enable monitoring and logging
- Use Docker secrets for sensitive data

## Network

All services run on the `healthdesk-network` bridge network, allowing them to communicate using service names:

- Frontend → API: `http://api:8000`
- API → MongoDB: `mongodb://mongodb:27017`

## File Structure

```
HealthDesk/
├── Api-Service/
│   ├── Dockerfile              # Backend Docker image
│   ├── .dockerignore           # Exclude files from build
│   └── ...
├── Frontend/
│   ├── Dockerfile              # Frontend Docker image (multi-stage)
│   ├── nginx.conf              # Nginx configuration
│   ├── .dockerignore           # Exclude files from build
│   └── ...
├── docker-compose.yml          # Orchestration configuration
└── DOCKER.md                   # This file
```

## Additional Commands

### Scale Services (if needed in future)
```bash
docker-compose up --scale api=3
```

### Update Dependencies
After updating `requirements.txt` or `package.json`:
```bash
docker-compose build --no-cache api
docker-compose up -d api
```

---

**Ready to go!** Run `docker-compose up` and access http://localhost:3000
