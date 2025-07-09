# PromptHub Enterprise Platform - AI Agent Guide
ATTENTION CODEX AGENT!!:
** ALL REQUIRED TASKS ARE CLEARLY LAID OUT IN prompthub_tasks.json LOCATED IN THE PROJECT ROOT FOLDER **

## Project Overview

PromptHub is an enterprise-grade prompt engineering platform that applies software engineering best practices to AI prompt management. This platform provides Git-like version control, collaborative editing, testing frameworks, and deployment pipelines specifically designed for enterprise AI workflows.

**Key Architecture**: Microservices-based system with React frontend, Python FastAPI backend, PostgreSQL database, and real-time collaboration features.

## Repository Structure Guide

### Core Service Directories
```
services/
├── auth/           # Authentication & authorization service
├── prompts/        # Core prompt CRUD and versioning
├── collaboration/  # Real-time editing with WebSocket
├── testing/        # Automated prompt validation framework
├── execution/      # LLM provider integration & execution
├── workflow/       # Review and approval workflows
├── analytics/      # Performance monitoring & reporting
├── audit/          # Compliance and audit logging
└── integrations/   # External tool integrations (Slack, Teams)
```

### Frontend Structure
```
src/
├── components/     # Reusable UI components
│   ├── auth/      # Login, registration forms
│   ├── editor/    # Monaco editor integration
│   ├── dashboard/ # Main prompt management UI
│   └── analytics/ # Performance dashboards
├── hooks/         # Custom React hooks for API calls
├── store/         # State management (Redux/Zustand)
├── utils/         # Helper functions and utilities
└── types/         # TypeScript type definitions
```

### Infrastructure & Config
```
deploy/            # Kubernetes manifests and deployment configs
monitoring/        # Prometheus, Grafana configurations
scripts/           # Development and deployment scripts
.github/workflows/ # CI/CD pipeline definitions
```

## Development Environment Setup

### Prerequisites Installation
```bash
# Install core dependencies
npm install
pip install -r requirements.txt
poetry install --with test

# Start development environment
docker-compose up -d
npm run dev
```

### Database Operations
```bash
# Run migrations
alembic upgrade head

# Seed development data
python scripts/seed_data.py

# Reset database (development only)
python scripts/reset_db.py
```

### Service Management
```bash
# Start specific microservice
cd services/prompts && uvicorn main:app --reload --port 8001

# Run all services
docker-compose up

# Check service health
curl http://localhost:8000/health
```

## Task-Specific Development Guidelines

### Working on Authentication (TASK-003, TASK-007, TASK-009, TASK-023)
- **Location**: `services/auth/` and `src/components/auth/`
- **Key Files**: `auth.py`, `rbac.py`, `LoginForm.tsx`, `sso.py`
- **Testing**: Always test with multiple user roles and SSO providers
- **Security**: Use bcrypt for passwords, implement rate limiting, validate JWT properly
- **Standards**: Follow OWASP authentication guidelines

### Prompt Management Features (TASK-005, TASK-006, TASK-011)
- **Location**: `services/prompts/` and `src/components/dashboard/`
- **Key Files**: `crud.py`, `versioning.py`, `PromptList.tsx`
- **Version Control**: Implement SHA-based versioning like Git
- **Performance**: Use pagination for large prompt lists, implement search indexing
- **Validation**: Validate prompt syntax and parameters before saving

### Real-time Collaboration (TASK-012, TASK-013, TASK-014)
- **Location**: `services/collaboration/` and `src/components/editor/`
- **Key Files**: `websocket.py`, `ot.py`, `CollaborativeEditor.tsx`
- **Algorithm**: Use proven Operational Transform library (ShareJS or similar)
- **Performance**: Optimize for <500ms latency, handle 50+ concurrent editors
- **Fallback**: Implement graceful degradation for network issues

### Testing Framework (TASK-016, TASK-020)
- **Location**: `services/testing/`
- **Key Files**: `framework.py`, `executor.py`, `ab_testing.py`
- **Metrics**: Implement BLEU, ROUGE, and custom evaluation metrics
- **Execution**: Support parallel test execution across multiple LLM providers
- **Reporting**: Generate comprehensive test reports with statistical analysis

### LLM Integration (TASK-017, TASK-018)
- **Location**: `services/execution/` and `services/llm/`
- **Key Files**: `providers.py`, `router.py`, `api.py`
- **Providers**: Support OpenAI, Anthropic, Azure OpenAI with unified interface
- **Performance**: Implement caching, rate limiting, and circuit breaker patterns
- **Cost**: Track token usage and costs per provider and user

## Code Quality Standards

### Python Backend Standards
```python
# Use FastAPI dependency injection
@app.post("/prompts/")
async def create_prompt(
    prompt: PromptCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Implementation here
```

### TypeScript Frontend Standards
```typescript
// Use React Query for data fetching
const { data: prompts, isLoading } = useQuery({
  queryKey: ['prompts', filters],
  queryFn: () => fetchPrompts(filters)
});

// Implement proper error handling
const [error, setError] = useState<string | null>(null);
```

### Database Patterns
- Use UUID primary keys to avoid conflicts in distributed system
- Include `created_at`, `updated_at`, `deleted_at` for all entities
- Implement soft deletes to maintain audit trail
- Add partial indexes for performance optimization

## Testing Requirements

### Unit Testing
```bash
# Backend tests
pytest services/prompts/tests/ -v --cov=services/prompts

# Frontend tests
npm test -- --coverage --watchAll=false

# Minimum coverage: 85% for critical business logic
```

### Integration Testing
```bash
# End-to-end tests
npx playwright test

# API integration tests
pytest tests/integration/ -v

# Database integration tests
pytest tests/db_integration/ -v
```

### Performance Testing
```bash
# Load testing with 1000+ concurrent users
k6 run performance/load_test.js

# WebSocket collaboration testing
node tests/collaboration_load.js

# Database performance testing
python tests/db_performance.py
```

## Security & Compliance Guidelines

### Authentication & Authorization
- Implement MFA for all enterprise users
- Use JWT with proper expiration and refresh token rotation
- Follow principle of least privilege for RBAC
- Log all authentication attempts and permission changes

### Data Protection
- Encrypt sensitive data at rest using AES-256
- Use TLS 1.3 for all client-server communication
- Implement proper secret management (never commit secrets)
- Follow GDPR and CCPA compliance requirements

### Audit Logging
- Log all user actions with timestamp, user ID, and action details
- Use write-only audit log storage with tamper detection
- Implement real-time streaming to SIEM systems
- Maintain logs according to enterprise retention policies

## Environment Configuration

### Development Environment Variables
```bash
# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/prompthub_dev
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET_KEY=your-dev-secret-key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

# LLM Providers
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
AZURE_OPENAI_ENDPOINT=your-azure-endpoint

# WebSocket
WEBSOCKET_SECRET=your-websocket-secret
```

### Production Considerations
- Use AWS Secrets Manager or HashiCorp Vault for secrets
- Enable database connection pooling and read replicas
- Configure auto-scaling for microservices
- Set up monitoring with Prometheus and Grafana

## Deployment Workflow

### CI/CD Pipeline
```yaml
# Automated testing on every PR
- Unit tests must pass (>85% coverage)
- Integration tests must pass
- Security scanning (Snyk, Veracode)
- Performance regression testing

# Deployment stages
1. Development → Staging (automatic on main branch)
2. Staging → Production (manual approval required)
3. Blue-green deployment with health checks
4. Automatic rollback on failure
```

### Health Checks
```python
# Implement comprehensive health checks
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": await check_database(),
        "redis": await check_redis(),
        "llm_providers": await check_llm_providers()
    }
```

## Monitoring & Observability

### Key Metrics to Track
- **Performance**: API response times (P95 <200ms), WebSocket latency
- **Business**: Prompt executions per day, user engagement, cost per execution
- **System**: Database query performance, cache hit rates, error rates
- **Security**: Authentication failures, permission denials, audit events

### Alerting Rules
```yaml
# Critical alerts
- Database connection failures
- Authentication service downtime
- High error rates (>5% for 5 minutes)
- WebSocket connection drops (>10% for 2 minutes)

# Warning alerts
- Slow API responses (P95 >500ms for 10 minutes)
- High LLM API costs (>budget threshold)
- Low cache hit rates (<80% for 15 minutes)
```

## Common Patterns & Best Practices

### Error Handling
```python
# Consistent error response format
class HTTPException(Exception):
    def __init__(self, status_code: int, detail: str, error_code: str = None):
        self.status_code = status_code
        self.detail = detail
        self.error_code = error_code

# Frontend error boundaries
<ErrorBoundary fallback={<ErrorFallback />}>
  <PromptEditor />
</ErrorBoundary>
```

### Async Operations
```python
# Use async/await for I/O operations
async def execute_prompt(prompt: str, provider: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{provider_url}/completion", json={"prompt": prompt})
        return response.json()
```

### State Management
```typescript
// Use Zustand for simple state management
interface PromptStore {
  prompts: Prompt[];
  loading: boolean;
  fetchPrompts: () => Promise<void>;
  updatePrompt: (id: string, updates: Partial<Prompt>) => void;
}
```

## Troubleshooting Guide

### Common Issues & Solutions

**Database Connection Issues**:
- Check connection string format and credentials
- Verify database server is running and accessible
- Review connection pool settings

**WebSocket Connection Problems**:
- Verify CORS configuration for WebSocket endpoints
- Check firewall rules for WebSocket traffic
- Validate JWT authentication for WebSocket connections

**LLM Provider API Failures**:
- Implement retry logic with exponential backoff
- Check API key validity and rate limits
- Use circuit breaker pattern for provider failures

**Performance Issues**:
- Monitor database query performance with EXPLAIN ANALYZE
- Check Redis cache hit rates and memory usage
- Profile API endpoints with performance monitoring tools

## Integration Guidelines

### Slack/Teams Integration (TASK-025)
```python
# Webhook notification example
async def send_notification(webhook_url: str, message: dict):
    async with httpx.AsyncClient() as client:
        await client.post(webhook_url, json={
            "text": message["text"],
            "attachments": message.get("attachments", [])
        })
```

### GitHub Integration
- Use GitHub App for secure repository access
- Implement webhook handlers for repository events
- Create pull requests for prompt deployments
- Sync user permissions with GitHub team membership

## Development Workflow

### Git Workflow
```bash
# Feature branch workflow
git checkout -b feature/TASK-XXX-description
git commit -m "feat(prompts): implement version control system"
git push origin feature/TASK-XXX-description

# Create pull request with proper description
# Link to task number and include testing instructions
```

### Code Review Checklist
- [ ] Code follows project style guidelines
- [ ] All tests pass and coverage meets requirements
- [ ] Security considerations addressed
- [ ] Performance impact assessed
- [ ] Documentation updated
- [ ] Database migrations included if needed

### Release Process
1. Create release branch from main
2. Run full test suite including performance tests
3. Update version numbers and changelog
4. Deploy to staging for final validation
5. Create release tag and deploy to production
6. Monitor deployment and performance metrics

## Performance Optimization

### Database Optimization
- Use appropriate indexes for query patterns
- Implement query result caching with Redis
- Use read replicas for reporting and analytics
- Monitor slow query log and optimize problematic queries

### Frontend Optimization
- Implement code splitting for large components
- Use React.memo for expensive component renders
- Optimize bundle size with tree shaking
- Implement service worker for offline capabilities

### API Optimization
- Use FastAPI dependency injection for database connections
- Implement response caching for expensive operations
- Use background tasks for non-critical operations
- Monitor and optimize memory usage

## Documentation Standards

### API Documentation
- Use OpenAPI/Swagger for automatic API documentation
- Include request/response examples for all endpoints
- Document error codes and their meanings
- Provide authentication and authorization details

### Code Documentation
```python
def create_prompt_version(prompt_id: str, content: str, user_id: str) -> PromptVersion:
    """
    Create a new version of a prompt with SHA-based versioning.
    
    Args:
        prompt_id: Unique identifier of the base prompt
        content: New prompt content to version
        user_id: ID of user creating the version
        
    Returns:
        PromptVersion: New version object with SHA hash
        
    Raises:
        PromptNotFoundError: If base prompt doesn't exist
        ValidationError: If content fails validation
    """
```

This AGENTS.md file provides comprehensive guidance for AI agents working on the PromptHub project, covering all aspects from development setup to deployment and monitoring. Use this as your primary reference for understanding project structure, coding standards, and best practices.
