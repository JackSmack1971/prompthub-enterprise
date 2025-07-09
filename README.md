# PromptHub Enterprise Platform

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [Development Setup](#development-setup)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Overview

PromptHub transforms enterprise prompt engineering from an ad-hoc process into a systematic, collaborative discipline by applying proven software engineering practices to AI prompt management. The platform provides teams with GitHub-like version control, testing frameworks, and deployment pipelines specifically designed for enterprise AI workflows.

### Key Benefits
- **75% reduction in AI output inconsistency** through structured testing and deployment workflows
- **3x acceleration in prompt engineering productivity** via collaborative development and reusable templates
- **Complete enterprise AI governance** through comprehensive audit trails and access controls
- **30% cost optimization** across multiple LLM providers through intelligent routing and monitoring

### Target Users
- **Prompt Engineers**: Develop reliable, consistent prompts for production systems
- **AI Team Leads**: Manage team productivity and ensure quality standards
- **DevOps Engineers**: Integrate AI workflows into existing CI/CD pipelines
- **Enterprise Organizations**: Scale AI initiatives with proper governance and compliance

## Features

### 🔄 Version Control & Collaboration
- **Git-like Version Control**: SHA-based versioning with complete change history
- **Real-time Collaborative Editing**: Multi-user editing with operational transform
- **Branching & Merging**: Feature branches for safe experimental development
- **Code Review Workflows**: Pull request system with approval processes

### 🧪 Testing & Validation
- **Automated Testing Framework**: Run prompts against predefined test cases
- **A/B Testing Platform**: Compare prompt performance with statistical analysis
- **Bias Detection**: Automated analysis for fairness and safety issues
- **Performance Monitoring**: Track latency, cost, and quality metrics

### 🚀 Deployment & Integration
- **One-Click Deployment**: Zero-downtime deployments with rollback capabilities
- **Multi-LLM Support**: Unified API for OpenAI, Anthropic, Azure OpenAI, and more
- **Enterprise Integrations**: Slack, Teams, JIRA, and GitHub/GitLab
- **Cost Optimization**: Intelligent provider routing based on cost and performance

### 🔒 Enterprise Security
- **Role-Based Access Control**: Granular permissions with enterprise SSO
- **Comprehensive Audit Logging**: Immutable trails for compliance
- **Data Encryption**: AES-256 at rest, TLS 1.3 in transit
- **SOC 2 Compliance**: Enterprise-grade security certifications

### 📊 Analytics & Optimization
- **Performance Dashboards**: Real-time metrics and usage analytics
- **Cost Tracking**: Detailed cost analysis across providers and teams
- **Usage Analytics**: Team productivity and adoption metrics
- **AI-Powered Optimization**: Automated suggestions for prompt improvement

## Architecture

### System Overview
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React App     │    │   API Gateway   │    │  Microservices  │
│   TypeScript    │◄──►│  Load Balancer  │◄──►│    Python       │
│                 │    │                 │    │    FastAPI      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                       ┌─────────────────┐            │
                       │   Data Layer    │◄───────────┘
                       │  PostgreSQL     │
                       │  Redis Cache    │
                       │  Elasticsearch  │
                       └─────────────────┘
```

### Microservices Architecture
- **Auth Service**: Authentication, authorization, and user management
- **Prompt Service**: Core prompt CRUD operations and version control
- **Collaboration Service**: Real-time editing with WebSocket support
- **Testing Service**: Automated validation and A/B testing framework
- **Execution Service**: LLM provider integration and request routing
- **Workflow Service**: Review processes and approval workflows
- **Analytics Service**: Performance monitoring and reporting
- **Audit Service**: Compliance logging and audit trails

### Technology Stack

#### Frontend
- **React 18** with TypeScript
- **Vite** for build tooling and development
- **Tailwind CSS** for styling
- **React Query** for data fetching and caching
- **Zustand** for state management
- **Monaco Editor** for code editing
- **Socket.IO** for real-time collaboration

#### Backend
- **Python 3.11** with FastAPI
- **PostgreSQL 15** for primary data storage
- **Redis 7** for caching and session management
- **Elasticsearch 8** for search and logging
- **WebSocket** for real-time features
- **Celery** for background task processing

#### Infrastructure
- **Docker** and **Kubernetes** for containerization
- **AWS** cloud infrastructure
- **Terraform** for infrastructure as code
- **Prometheus** and **Grafana** for monitoring
- **GitHub Actions** for CI/CD

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ and npm
- Python 3.11+ and pip
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/prompthub-enterprise.git
cd prompthub-enterprise
```

### 2. Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit environment variables
nano .env
```

### 3. Start Development Environment
```bash
# Start all services with Docker Compose
docker-compose up -d

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies
cd ../backend
pip install -r requirements.txt
poetry install --with dev,test

# Set up pre-commit hooks
pre-commit install

# Run database migrations
alembic upgrade head

# Seed development data
python scripts/seed_data.py
```

### 4. Access the Application
- **Frontend**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Admin Dashboard**: http://localhost:3000/admin

### 5. Create Your First Prompt
1. Register a new account or use the demo credentials
2. Navigate to the Dashboard
3. Click "Create New Prompt"
4. Write your prompt and save
5. Run tests and deploy to staging

## Development Setup

### Local Development

#### Backend Services
```bash
# Start individual microservices
cd services/auth && uvicorn main:app --reload --port 8001
cd services/prompts && uvicorn main:app --reload --port 8002
cd services/collaboration && uvicorn main:app --reload --port 8003

# Or use the development script
./scripts/start-dev-services.sh
```

#### Frontend Development
```bash
cd frontend
npm run dev
# Access at http://localhost:3000
```

#### Database Operations
```bash
# Create new migration
cd backend
alembic revision --autogenerate -m "Add new feature"

# Apply migrations
alembic upgrade head

# Reset database (development only)
python scripts/reset_db.py

# Backup database
pg_dump prompthub_dev > backups/dev_backup.sql
```

### Environment Variables

#### Required Variables
```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/prompthub_dev
REDIS_URL=redis://localhost:6379/0

# Authentication
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# LLM Providers
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-azure-key

# External Services
SLACK_BOT_TOKEN=xoxb-your-slack-token
TEAMS_WEBHOOK_URL=https://your-teams-webhook
GITHUB_APP_ID=12345
GITHUB_PRIVATE_KEY=your-github-private-key

# Monitoring
SENTRY_DSN=https://your-sentry-dsn
PROMETHEUS_ENDPOINT=http://prometheus:9090
```

#### Optional Variables
```bash
# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Storage
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET=prompthub-storage

# Analytics
GOOGLE_ANALYTICS_ID=GA_MEASUREMENT_ID
MIXPANEL_TOKEN=your-mixpanel-token
```

## API Documentation

### Authentication

#### Register User
```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password",
  "full_name": "John Doe",
  "organization": "Acme Corp"
}
```

#### Login
```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password"
}
```

#### Response
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 1800,
  "user": {
    "id": "uuid-here",
    "email": "user@example.com",
    "full_name": "John Doe",
    "role": "user"
  }
}
```

### Prompt Management

#### Create Prompt
```http
POST /api/v1/prompts
Authorization: Bearer {token}
Content-Type: application/json

{
  "title": "Customer Support Assistant",
  "content": "You are a helpful customer support assistant...",
  "parameters": {
    "temperature": 0.7,
    "max_tokens": 150,
    "model": "gpt-4"
  },
  "tags": ["customer-support", "assistant"]
}
```

#### Get Prompt
```http
GET /api/v1/prompts/{prompt_id}
Authorization: Bearer {token}
```

#### Update Prompt
```http
PUT /api/v1/prompts/{prompt_id}
Authorization: Bearer {token}
Content-Type: application/json

{
  "content": "Updated prompt content...",
  "commit_message": "Improved response accuracy"
}
```

#### List Prompts
```http
GET /api/v1/prompts?page=1&limit=20&search=customer&tags=assistant
Authorization: Bearer {token}
```

### Version Control

#### Get Version History
```http
GET /api/v1/prompts/{prompt_id}/versions
Authorization: Bearer {token}
```

#### Create Branch
```http
POST /api/v1/prompts/{prompt_id}/branches
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "feature/improve-responses",
  "base_version": "abc123def"
}
```

#### Compare Versions
```http
GET /api/v1/prompts/{prompt_id}/compare/{version_a}...{version_b}
Authorization: Bearer {token}
```

### Prompt Execution

#### Execute Prompt
```http
POST /api/v1/execute
Authorization: Bearer {token}
Content-Type: application/json

{
  "prompt_id": "uuid-here",
  "version": "latest",
  "inputs": {
    "user_message": "Hello, I need help with my order",
    "context": "Order #12345"
  },
  "provider": "openai",
  "model": "gpt-4"
}
```

#### Response
```json
{
  "result": {
    "completion": "I'd be happy to help you with order #12345...",
    "metadata": {
      "tokens_used": 45,
      "latency_ms": 850,
      "cost_usd": 0.002,
      "provider": "openai",
      "model": "gpt-4"
    }
  },
  "execution_id": "exec-uuid-here",
  "timestamp": "2025-07-08T10:30:00Z"
}
```

### Testing

#### Create Test Case
```http
POST /api/v1/prompts/{prompt_id}/tests
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "Customer greeting test",
  "inputs": {
    "user_message": "Hello"
  },
  "expected_outputs": [
    {
      "type": "contains",
      "value": "Hello! How can I help you today?"
    },
    {
      "type": "sentiment",
      "value": "positive"
    }
  ]
}
```

#### Run Tests
```http
POST /api/v1/prompts/{prompt_id}/test-runs
Authorization: Bearer {token}
Content-Type: application/json

{
  "version": "latest",
  "test_case_ids": ["test-1", "test-2"],
  "providers": ["openai", "anthropic"]
}
```

### A/B Testing

#### Create A/B Test
```http
POST /api/v1/experiments
Authorization: Bearer {token}
Content-Type: application/json

{
  "name": "Response Style Comparison",
  "prompt_id": "uuid-here",
  "variants": [
    {
      "name": "formal",
      "version": "abc123",
      "traffic_percentage": 50
    },
    {
      "name": "casual",
      "version": "def456",
      "traffic_percentage": 50
    }
  ],
  "success_metrics": ["user_satisfaction", "task_completion"],
  "duration_days": 7
}
```

## Testing

### Running Tests

#### Backend Tests
```bash
# Unit tests
pytest services/auth/tests/ -v --cov=services/auth
pytest services/prompts/tests/ -v --cov=services/prompts

# Integration tests
pytest tests/integration/ -v

# All tests with coverage
pytest --cov=. --cov-report=html --cov-report=term

# Performance tests
pytest tests/performance/ -v --benchmark-only
```

#### Frontend Tests
```bash
cd frontend

# Unit tests
npm test

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e

# Visual regression tests
npm run test:visual

# All tests with coverage
npm run test:coverage
```

### Test Categories

#### Unit Tests
- **Coverage Requirement**: >85% for critical business logic
- **Focus Areas**: Business logic, utilities, pure functions
- **Mocking**: External dependencies, database calls, API requests

#### Integration Tests
- **API Testing**: All endpoints with realistic data
- **Database Testing**: CRUD operations, transactions, constraints
- **Service Integration**: Inter-service communication patterns

#### End-to-End Tests
- **User Workflows**: Complete user journeys from login to deployment
- **Cross-browser**: Chrome, Firefox, Safari compatibility
- **Mobile Responsive**: Touch interactions and responsive layouts

#### Performance Tests
- **Load Testing**: 1,000+ concurrent users
- **Stress Testing**: System breaking points
- **API Performance**: <200ms P95 response times
- **Real-time Features**: WebSocket latency and throughput

### Test Data Management

#### Fixtures
```python
# pytest fixtures for consistent test data
@pytest.fixture
def sample_user():
    return User(
        email="test@example.com",
        full_name="Test User",
        role="user"
    )

@pytest.fixture
def sample_prompt():
    return Prompt(
        title="Test Prompt",
        content="You are a test assistant...",
        author_id="user-id"
    )
```

#### Test Database
```bash
# Create test database
createdb prompthub_test

# Run migrations
ENVIRONMENT=test alembic upgrade head

# Seed test data
ENVIRONMENT=test python scripts/seed_test_data.py
```

## Deployment

### Production Deployment

#### Prerequisites
- Kubernetes cluster (AWS EKS recommended)
- PostgreSQL database (RDS)
- Redis cluster (ElastiCache)
- Container registry (ECR)
- Domain name and SSL certificate

#### Build and Push Images
```bash
# Build all service images
./scripts/build-images.sh

# Tag for production
docker tag prompthub-auth:latest your-registry/prompthub-auth:v1.0.0
docker tag prompthub-prompts:latest your-registry/prompthub-prompts:v1.0.0

# Push to registry
docker push your-registry/prompthub-auth:v1.0.0
docker push your-registry/prompthub-prompts:v1.0.0
```

#### Deploy to Kubernetes
```bash
# Apply configurations
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmaps/
kubectl apply -f k8s/secrets/
kubectl apply -f k8s/deployments/
kubectl apply -f k8s/services/
kubectl apply -f k8s/ingress/

# Verify deployment
kubectl get pods -n prompthub
kubectl get services -n prompthub
```

#### Database Migration
```bash
# Run migrations in production
kubectl exec -it deployment/prompthub-auth -n prompthub -- alembic upgrade head
```

### Blue-Green Deployment

#### Setup
```bash
# Deploy to green environment
kubectl apply -f k8s/deployments/green/

# Verify green deployment
kubectl get pods -l env=green -n prompthub

# Switch traffic to green
kubectl patch service prompthub-gateway -n prompthub -p '{"spec":{"selector":{"env":"green"}}}'

# Verify traffic switch
curl -H "Host: prompthub.example.com" http://your-load-balancer/health

# Remove blue environment
kubectl delete -f k8s/deployments/blue/
```

### Environment Configurations

#### Staging Environment
```yaml
# k8s/deployments/staging.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prompthub-auth-staging
spec:
  replicas: 2
  selector:
    matchLabels:
      app: prompthub-auth
      env: staging
  template:
    metadata:
      labels:
        app: prompthub-auth
        env: staging
    spec:
      containers:
      - name: auth
        image: your-registry/prompthub-auth:staging
        env:
        - name: ENVIRONMENT
          value: "staging"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-credentials
              key: staging-url
```

#### Production Environment
```yaml
# k8s/deployments/production.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prompthub-auth-production
spec:
  replicas: 5
  selector:
    matchLabels:
      app: prompthub-auth
      env: production
  template:
    metadata:
      labels:
        app: prompthub-auth
        env: production
    spec:
      containers:
      - name: auth
        image: your-registry/prompthub-auth:v1.0.0
        env:
        - name: ENVIRONMENT
          value: "production"
        resources:
          requests:
            memory: "256Mi"
            cpu: "200m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

### Monitoring and Logging

#### Prometheus Configuration
```yaml
# monitoring/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prompthub-services'
    kubernetes_sd_configs:
    - role: pod
    relabel_configs:
    - source_labels: [__meta_kubernetes_pod_label_app]
      action: keep
      regex: prompthub.*
```

#### Grafana Dashboards
- **System Metrics**: CPU, memory, disk usage
- **Application Metrics**: Request rates, error rates, latency
- **Business Metrics**: Prompt executions, user activity, costs
- **Security Metrics**: Authentication failures, permission denials

## Security

### Authentication & Authorization

#### JWT Configuration
```python
# Security settings
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 30
JWT_REFRESH_TOKEN_EXPIRE_DAYS = 7

# Password hashing
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
```

#### Role-Based Access Control
```python
# Permission matrix
PERMISSIONS = {
    "admin": ["*"],
    "team_lead": [
        "prompt:read", "prompt:write", "prompt:delete",
        "user:read", "analytics:read", "audit:read"
    ],
    "engineer": [
        "prompt:read", "prompt:write",
        "test:run", "deploy:staging"
    ],
    "viewer": [
        "prompt:read", "analytics:read"
    ]
}
```

### Data Encryption

#### At Rest
```python
# Database encryption
from cryptography.fernet import Fernet

def encrypt_sensitive_data(data: str) -> str:
    key = os.getenv("ENCRYPTION_KEY").encode()
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_sensitive_data(encrypted_data: str) -> str:
    key = os.getenv("ENCRYPTION_KEY").encode()
    f = Fernet(key)
    return f.decrypt(encrypted_data.encode()).decode()
```

#### In Transit
```nginx
# NGINX SSL configuration
server {
    listen 443 ssl http2;
    server_name prompthub.example.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
}
```

### Security Headers
```python
# FastAPI middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://prompthub.example.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["prompthub.example.com", "*.prompthub.example.com"]
)
```

### Audit Logging
```python
# Audit logger
import logging
from datetime import datetime

def log_audit_event(
    user_id: str,
    action: str,
    resource: str,
    details: dict = None
):
    audit_logger.info({
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "action": action,
        "resource": resource,
        "details": details or {},
        "ip_address": request.client.host,
        "user_agent": request.headers.get("user-agent")
    })
```

### Vulnerability Management

#### Security Scanning
```yaml
# .github/workflows/security.yml
name: Security Scan
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Run Snyk
      uses: snyk/actions/python@master
      env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

    - name: Run Bandit
      run: |
        pip install bandit
        bandit -r . -f json -o bandit-report.json

    - name: Run Safety
      run: |
        pip install safety
        safety check --json --output safety-report.json
```

#### Penetration Testing
- **Frequency**: Quarterly external penetration tests
- **Scope**: Web application, API endpoints, infrastructure
- **Tools**: OWASP ZAP, Burp Suite, custom security tests
- **Reporting**: Detailed findings with remediation timelines

## Contributing

### Development Workflow

#### Setting Up Development Environment
```bash
# Fork the repository
git clone https://github.com/your-username/prompthub-enterprise.git
cd prompthub-enterprise

# Create feature branch
git checkout -b feature/your-feature-name

# Install dependencies
npm install
pip install -r requirements.txt

# Set up pre-commit hooks
pre-commit install
```

#### Code Standards

#### Python Code Style
```python
# Use Black for formatting
black --line-length 88 services/

# Use isort for imports
isort services/

# Use flake8 for linting
flake8 services/ --max-line-length=88

# Use mypy for type checking
mypy services/
```

#### TypeScript Code Style
```bash
# Use Prettier for formatting
npx prettier --write frontend/src/

# Use ESLint for linting
npx eslint frontend/src/ --fix

# Type checking
npx tsc --noEmit
```

### Pull Request Process

#### Before Submitting
1. **Run Tests**: Ensure all tests pass locally
2. **Code Review**: Self-review your changes
3. **Documentation**: Update relevant documentation
4. **Changelog**: Add entry to CHANGELOG.md
5. **Commit Messages**: Follow conventional commit format

#### Commit Message Format
```
type(scope): description

[optional body]

[optional footer]
```

Examples:
```
feat(auth): add SSO integration with SAML 2.0
fix(prompts): resolve version comparison edge case
docs(api): update authentication endpoints
test(collaboration): add real-time editing tests
```

#### Pull Request Template
```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

### Code Review Guidelines

#### For Authors
- **Small PRs**: Keep changes focused and reviewable
- **Clear Description**: Explain what and why, not just how
- **Test Coverage**: Include tests for new functionality
- **Documentation**: Update relevant docs and comments

#### For Reviewers
- **Timely Reviews**: Respond within 24 hours
- **Constructive Feedback**: Suggest improvements, don't just criticize
- **Security Focus**: Look for potential security issues
- **Performance Impact**: Consider scalability implications

### Issue Reporting

#### Bug Reports
```markdown
**Bug Description**
A clear description of the bug

**Steps to Reproduce**
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected Behavior**
What you expected to happen

**Screenshots**
If applicable, add screenshots

**Environment**
- OS: [e.g. iOS]
- Browser: [e.g. chrome, safari]
- Version: [e.g. 22]
```

#### Feature Requests
```markdown
**Feature Description**
A clear description of the feature

**Problem Statement**
What problem does this solve?

**Proposed Solution**
How should this feature work?

**Alternatives Considered**
Other solutions you've considered

**Additional Context**
Any other context or screenshots
```

## Performance Optimization

### Database Optimization

#### Query Optimization
```sql
-- Example optimized query with proper indexing
EXPLAIN ANALYZE
SELECT p.*, u.full_name as author_name,
       COUNT(v.id) as version_count
FROM prompts p
JOIN users u ON p.author_id = u.id
LEFT JOIN prompt_versions v ON p.id = v.prompt_id
WHERE p.organization_id = $1
  AND p.deleted_at IS NULL
  AND p.status = 'active'
GROUP BY p.id, u.full_name
ORDER BY p.updated_at DESC
LIMIT 20 OFFSET $2;

-- Required indexes
CREATE INDEX CONCURRENTLY idx_prompts_org_status_updated
ON prompts(organization_id, status, updated_at DESC)
WHERE deleted_at IS NULL;
```

#### Connection Pooling
```python
# Database connection pool configuration
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True,
    pool_recycle=3600
)
```

### Caching Strategies

#### Redis Caching
```python
# Cache configuration
CACHE_SETTINGS = {
    "prompt_metadata": {"ttl": 300},  # 5 minutes
    "user_permissions": {"ttl": 900},  # 15 minutes
    "llm_responses": {"ttl": 3600},   # 1 hour
    "analytics_data": {"ttl": 1800}   # 30 minutes
}

# Cache implementation
async def get_cached_prompt(prompt_id: str) -> Optional[dict]:
    cached = await redis.get(f"prompt:{prompt_id}")
    if cached:
        return json.loads(cached)
    return None

async def set_cached_prompt(prompt_id: str, data: dict):
    await redis.setex(
        f"prompt:{prompt_id}",
        CACHE_SETTINGS["prompt_metadata"]["ttl"],
        json.dumps(data)
    )
```

### Frontend Optimization

#### Code Splitting
```typescript
// Route-based code splitting
import { lazy, Suspense } from 'react';

const Dashboard = lazy(() => import('./components/Dashboard'));
const PromptEditor = lazy(() => import('./components/PromptEditor'));
const Analytics = lazy(() => import('./components/Analytics'));

function App() {
  return (
    <Router>
      <Suspense fallback={<LoadingSpinner />}>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/editor" element={<PromptEditor />} />
          <Route path="/analytics" element={<Analytics />} />
        </Routes>
      </Suspense>
    </Router>
  );
}
```

#### Bundle Optimization
```javascript
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
        monaco: {
          test: /[\\/]node_modules[\\/]monaco-editor[\\/]/,
          name: 'monaco',
          chunks: 'all',
        }
      }
    }
  }
};
```

## Troubleshooting

### Common Issues

#### Database Connection Issues
```bash
# Check database connectivity
pg_isready -h localhost -p 5432

# Check connection pool status
SELECT count(*) as active_connections
FROM pg_stat_activity
WHERE state = 'active';

# Reset connection pool
systemctl restart pgbouncer
```

#### WebSocket Connection Problems
```javascript
// WebSocket debugging
const ws = new WebSocket('ws://localhost:8000/ws');
ws.onopen = () => console.log('Connected');
ws.onerror = (error) => console.error('WebSocket error:', error);
ws.onclose = (event) => console.log('Disconnected:', event.code, event.reason);

// Check CORS configuration
// Ensure WebSocket endpoint allows your origin
```

#### Performance Issues
```bash
# Monitor system resources
htop
iotop
nethogs

# Check API response times
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:8000/api/v1/prompts"

# Monitor database performance
SELECT query, mean_time, calls, total_time
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;
```

#### LLM Provider API Issues
```python
# Provider health check
async def check_provider_health():
    providers = ["openai", "anthropic", "azure"]
    results = {}

    for provider in providers:
        try:
            start_time = time.time()
            response = await make_test_request(provider)
            latency = time.time() - start_time
            results[provider] = {
                "status": "healthy",
                "latency_ms": latency * 1000,
                "rate_limit_remaining": response.headers.get("x-ratelimit-remaining")
            }
        except Exception as e:
            results[provider] = {
                "status": "unhealthy",
                "error": str(e)
            }

    return results
```

#### Memory Leaks
```bash
# Monitor memory usage
ps aux | grep python | awk '{print $6/1024 " MB\t" $11}'

# Profile memory usage
pip install memory-profiler
python -m memory_profiler services/prompts/main.py

# Check for WebSocket connection leaks
netstat -an | grep :8000 | wc -l
```

### Debugging Tools

#### Application Debugging
```python
# Debug logging configuration
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

# Request tracing
import uuid

@app.middleware("http")
async def add_trace_id(request: Request, call_next):
    trace_id = str(uuid.uuid4())
    request.state.trace_id = trace_id
    response = await call_next(request)
    response.headers["X-Trace-ID"] = trace_id
    return response
```

#### Database Debugging
```sql
-- Enable query logging
ALTER SYSTEM SET log_statement = 'all';
ALTER SYSTEM SET log_min_duration_statement = 100;
SELECT pg_reload_conf();

-- Monitor slow queries
SELECT query, mean_time, calls, total_time,
       100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0) AS hit_percent
FROM pg_stat_statements
WHERE mean_time > 100
ORDER BY mean_time DESC;

-- Check table sizes
SELECT schemaname,tablename,
       pg_size_pretty(size) as size_pretty,
       pg_size_pretty(total_size) as total_size_pretty
FROM (
  SELECT schemaname,tablename,
         pg_relation_size(schemaname||'.'||tablename) as size,
         pg_total_relation_size(schemaname||'.'||tablename) as total_size
  FROM pg_tables
) AS TABLES
ORDER BY total_size DESC;
```

### Performance Monitoring

#### Application Performance Monitoring
```python
# Custom metrics collection
from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNT = Counter('requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('request_duration_seconds', 'Request latency')
ACTIVE_CONNECTIONS = Gauge('websocket_connections_active', 'Active WebSocket connections')

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    REQUEST_LATENCY.observe(time.time() - start_time)
    return response
```

#### Health Check Endpoints
```python
@app.get("/health")
async def health_check():
    checks = {
        "database": await check_database_health(),
        "redis": await check_redis_health(),
        "llm_providers": await check_llm_providers_health(),
        "disk_space": check_disk_space(),
        "memory_usage": check_memory_usage()
    }

    all_healthy = all(check["status"] == "healthy" for check in checks.values())

    return {
        "status": "healthy" if all_healthy else "unhealthy",
        "timestamp": datetime.utcnow().isoformat(),
        "checks": checks,
        "version": get_app_version()
    }

@app.get("/health/live")
async def liveness_check():
    """Kubernetes liveness probe"""
    return {"status": "alive"}

@app.get("/health/ready")
async def readiness_check():
    """Kubernetes readiness probe"""
    if await check_database_health()["status"] == "healthy":
        return {"status": "ready"}
    else:
        raise HTTPException(status_code=503, detail="Not ready")
```

## Backup and Recovery

### Database Backup Strategy

#### Automated Backups
```bash
#!/bin/bash
# backup-database.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/postgresql"
DB_NAME="prompthub_production"

# Create backup directory
mkdir -p $BACKUP_DIR

# Full database backup
pg_dump -h $DB_HOST -U $DB_USER -d $DB_NAME -F c -b -v -f "$BACKUP_DIR/prompthub_full_$DATE.backup"

# Schema-only backup
pg_dump -h $DB_HOST -U $DB_USER -d $DB_NAME -s -f "$BACKUP_DIR/prompthub_schema_$DATE.sql"

# Upload to S3
aws s3 cp "$BACKUP_DIR/prompthub_full_$DATE.backup" s3://prompthub-backups/database/

# Cleanup old backups (keep last 30 days)
find $BACKUP_DIR -name "*.backup" -mtime +30 -delete

echo "Backup completed: prompthub_full_$DATE.backup"
```

#### Point-in-Time Recovery
```bash
# Enable WAL archiving in postgresql.conf
wal_level = replica
archive_mode = on
archive_command = 'aws s3 cp %p s3://prompthub-wal-archive/%f'

# Create base backup
pg_basebackup -h $DB_HOST -D /backup/base -U replication -P -W -R

# Restore to specific point in time
pg_ctl stop -D /var/lib/postgresql/data
rm -rf /var/lib/postgresql/data/*
cp -R /backup/base/* /var/lib/postgresql/data/

# Create recovery.conf
echo "restore_command = 'aws s3 cp s3://prompthub-wal-archive/%f %p'" > /var/lib/postgresql/data/recovery.conf
echo "recovery_target_time = '2025-07-08 14:30:00'" >> /var/lib/postgresql/data/recovery.conf

pg_ctl start -D /var/lib/postgresql/data
```

### Application Data Backup

#### File Storage Backup
```bash
#!/bin/bash
# backup-files.sh

# Backup user uploads and generated files
aws s3 sync /app/storage/uploads s3://prompthub-backups/uploads/ --delete
aws s3 sync /app/storage/exports s3://prompthub-backups/exports/ --delete

# Backup configuration files
tar -czf /tmp/config_backup.tar.gz /app/config/
aws s3 cp /tmp/config_backup.tar.gz s3://prompthub-backups/config/
```

#### Redis Backup
```bash
# Create Redis snapshot
redis-cli BGSAVE

# Wait for completion
while [ $(redis-cli LASTSAVE) -eq $LAST_SAVE ]; do
  sleep 1
done

# Copy RDB file
cp /var/lib/redis/dump.rdb /backup/redis/dump_$(date +%Y%m%d_%H%M%S).rdb

# Upload to S3
aws s3 cp /backup/redis/dump_$(date +%Y%m%d_%H%M%S).rdb s3://prompthub-backups/redis/
```

### Disaster Recovery Plan

#### Recovery Time Objectives (RTO)
- **Critical Services**: 4 hours
- **Non-critical Services**: 24 hours
- **Full System Recovery**: 48 hours

#### Recovery Point Objectives (RPO)
- **Database**: 15 minutes (using WAL streaming)
- **File Storage**: 1 hour (using S3 cross-region replication)
- **Configuration**: 24 hours (daily backups)

#### Recovery Procedures
```bash
# 1. Assess damage and activate disaster recovery team
# 2. Deploy infrastructure from Terraform templates
terraform apply -var-file="disaster-recovery.tfvars"

# 3. Restore database from latest backup
pg_restore -h $NEW_DB_HOST -U postgres -d prompthub_production /backup/latest.backup

# 4. Restore file storage
aws s3 sync s3://prompthub-backups/uploads/ /app/storage/uploads/

# 5. Deploy application services
kubectl apply -f k8s/disaster-recovery/

# 6. Verify system functionality
./scripts/verify-recovery.sh

# 7. Update DNS to point to new infrastructure
# 8. Monitor and validate full functionality
```

## Scaling Guide

### Horizontal Scaling

#### Application Services
```yaml
# k8s/hpa.yaml - Horizontal Pod Autoscaler
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: prompthub-auth-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: prompthub-auth
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```

#### Database Scaling
```yaml
# PostgreSQL read replicas
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: prompthub-postgres
spec:
  instances: 3

  postgresql:
    parameters:
      max_connections: "200"
      shared_buffers: "256MB"
      effective_cache_size: "1GB"

  monitoring:
    enabled: true

  backup:
    retentionPolicy: "30d"
    barmanObjectStore:
      destinationPath: "s3://prompthub-pg-backup"
```

### Vertical Scaling

#### Resource Optimization
```yaml
# Optimized resource requests and limits
resources:
  requests:
    memory: "512Mi"
    cpu: "300m"
  limits:
    memory: "1Gi"
    cpu: "500m"

# For memory-intensive operations (analytics)
resources:
  requests:
    memory: "2Gi"
    cpu: "500m"
  limits:
    memory: "4Gi"
    cpu: "1000m"
```

### Load Balancing

#### NGINX Configuration
```nginx
upstream prompthub_backend {
    least_conn;
    server prompthub-auth-1:8000 max_fails=3 fail_timeout=30s;
    server prompthub-auth-2:8000 max_fails=3 fail_timeout=30s;
    server prompthub-auth-3:8000 max_fails=3 fail_timeout=30s;
}

upstream prompthub_websocket {
    ip_hash;  # Sticky sessions for WebSocket
    server prompthub-collaboration-1:8001;
    server prompthub-collaboration-2:8001;
    server prompthub-collaboration-3:8001;
}

server {
    listen 80;
    server_name prompthub.example.com;

    location /api/ {
        proxy_pass http://prompthub_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /ws/ {
        proxy_pass http://prompthub_websocket;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

### Caching Strategies

#### Multi-Level Caching
```python
# L1: Application-level caching
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_user_permissions(user_id: str) -> List[str]:
    return fetch_user_permissions_from_db(user_id)

# L2: Redis distributed caching
async def get_prompt_with_cache(prompt_id: str) -> dict:
    # Try cache first
    cached = await redis.get(f"prompt:{prompt_id}")
    if cached:
        return json.loads(cached)

    # Fetch from database
    prompt = await db.fetch_prompt(prompt_id)

    # Cache for future requests
    await redis.setex(f"prompt:{prompt_id}", 300, json.dumps(prompt))
    return prompt

# L3: CDN for static assets
# Configured in CloudFront/CloudFlare
```

## API Rate Limiting

### Implementation
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Apply rate limits to endpoints
@app.post("/api/v1/execute")
@limiter.limit("100/minute")  # 100 requests per minute per IP
async def execute_prompt(request: Request, ...):
    pass

@app.post("/api/v1/auth/login")
@limiter.limit("5/minute")  # Stricter limit for auth endpoints
async def login(request: Request, ...):
    pass
```

### Advanced Rate Limiting
```python
# User-based rate limiting
from slowapi.util import get_remote_address

def get_user_id(request: Request):
    token = request.headers.get("authorization")
    if token:
        try:
            payload = jwt.decode(token.replace("Bearer ", ""), SECRET_KEY, algorithms=[ALGORITHM])
            return payload.get("sub")
        except:
            pass
    return get_remote_address(request)

limiter = Limiter(key_func=get_user_id)

# Different limits for different user tiers
@app.post("/api/v1/execute")
async def execute_prompt(request: Request, current_user: User = Depends(get_current_user)):
    user_tier = current_user.subscription_tier

    limits = {
        "free": "10/hour",
        "pro": "1000/hour",
        "enterprise": "10000/hour"
    }

    await limiter.limit(limits.get(user_tier, "10/hour"))(request)
    # ... rest of endpoint logic
```

## License

### MIT License

```
MIT License

Copyright (c) 2025 PromptHub Enterprise Platform

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Support and Community

### Getting Help

#### Documentation
- **API Documentation**: https://docs.prompthub.example.com
- **User Guide**: https://docs.prompthub.example.com/guide
- **Developer Documentation**: https://docs.prompthub.example.com/dev
- **Video Tutorials**: https://www.youtube.com/prompthub

#### Community Resources
- **GitHub Discussions**: https://github.com/your-org/prompthub-enterprise/discussions
- **Discord Server**: https://discord.gg/prompthub
- **Stack Overflow**: Tag questions with `prompthub`
- **Reddit Community**: r/prompthub

#### Professional Support
- **Enterprise Support**: support@prompthub.example.com
- **Security Issues**: security@prompthub.example.com
- **Sales Inquiries**: sales@prompthub.example.com
- **Partnership Opportunities**: partners@prompthub.example.com

### Contributing to the Community

#### Ways to Contribute
- **Code Contributions**: Submit pull requests for bug fixes and features
- **Documentation**: Help improve documentation and tutorials
- **Bug Reports**: Report issues and help with debugging
- **Feature Requests**: Suggest new features and improvements
- **Community Support**: Help other users in discussions and forums

#### Recognition
- **Contributor Hall of Fame**: Top contributors featured on website
- **Exclusive Access**: Early access to new features and beta programs
- **Swag Program**: PromptHub merchandise for active contributors
- **Conference Opportunities**: Speaking opportunities at AI/ML conferences

### Roadmap

#### Upcoming Features (Q3-Q4 2025)
- **Advanced AI Safety**: Enhanced bias detection and content filtering
- **Multi-language Support**: Internationalization for global teams
- **Advanced Analytics**: ML-powered insights and optimization recommendations
- **Workflow Automation**: No-code workflow builder for prompt operations
- **Enterprise Integrations**: Salesforce, ServiceNow, and custom enterprise tools

#### Long-term Vision (2026+)
- **AI-Powered Prompt Generation**: Automated prompt creation and optimization
- **Federated Learning**: Privacy-preserving model improvement across organizations
- **Advanced Governance**: Compliance automation and regulatory reporting
- **Ecosystem Platform**: Third-party plugin marketplace and extensibility framework

---

## Quick Reference

### Essential Commands
```bash
# Development
npm run dev                 # Start frontend development server
docker-compose up          # Start all services
pytest                     # Run backend tests
npm test                   # Run frontend tests

# Production
./scripts/deploy.sh        # Deploy to production
kubectl get pods           # Check service status
./scripts/backup.sh        # Create backup
./scripts/health-check.sh  # Verify system health

# Maintenance
alembic upgrade head       # Apply database migrations
./scripts/cleanup-logs.sh  # Clean up old log files
redis-cli FLUSHDB         # Clear Redis cache
./scripts/optimize-db.sh   # Optimize database performance
```

### Environment Variables Checklist
- [ ] `DATABASE_URL` - PostgreSQL connection string
- [ ] `REDIS_URL` - Redis connection string
- [ ] `JWT_SECRET_KEY` - JWT signing secret
- [ ] `OPENAI_API_KEY` - OpenAI API access
- [ ] `ANTHROPIC_API_KEY` - Anthropic API access
- [ ] `SLACK_BOT_TOKEN` - Slack integration
- [ ] `SENTRY_DSN` - Error tracking
- [ ] `AWS_ACCESS_KEY_ID` - AWS services
- [ ] `ENCRYPTION_KEY` - Data encryption

### Performance Targets
- **API Response Time**: P95 < 200ms
- **WebSocket Latency**: < 500ms
- **Database Queries**: P95 < 50ms
- **Page Load Time**: < 3 seconds
- **Uptime**: 99.9%
- **Test Coverage**: > 85%

### Security Checklist
- [ ] HTTPS enabled with valid SSL certificate
- [ ] JWT tokens have reasonable expiration times
- [ ] Database credentials are properly secured
- [ ] API rate limiting is configured
- [ ] Audit logging is enabled
- [ ] Security headers are configured
- [ ] Dependency vulnerabilities are scanned
- [ ] User input is properly validated and sanitized

---

**Ready to transform your prompt engineering workflow?**

Start with our [Quick Start Guide](#quick-start) or join our [Community](#support-and-community) to connect with other PromptHub users and contributors.

For enterprise inquiries and custom deployment options, contact our sales team at sales@prompthub.example.com.
