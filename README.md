# AI GitHub PR Reviewer

AI GitHub PR Reviewer is a multi-agent AI-powered code review system that automates source code analysis using Microsoft AutoGen and OpenAI GPT-4o mini.

The application uses multiple specialized AI agents to perform Static Analysis, Security (OWASP Top 10), Architecture Review, and Code Style Review, providing intelligent feedback to developers. Built on a scalable FastAPI microservices architecture with Celery, Redis, PostgreSQL, and Langfuse for LLM observability, the system is designed for production-ready AI-assisted code reviews.

## Features

- Multi-Agent AI architecture using Microsoft AutoGen
- Static Analysis Agent
- Security Review Agent (OWASP Top 10)
- Architecture Review Agent
- Code Style Review Agent
- FastAPI Microservices
- OpenAI GPT-4o mini Integration
- Asynchronous Processing with Celery & Redis
- PostgreSQL Database
- Langfuse LLM Tracing
- Prometheus & Grafana Monitoring
- Scalable and Production-ready Design

## Tech Stack

- Python
- Microsoft AutoGen
- OpenAI GPT-4o mini
- FastAPI
- PostgreSQL
- SQLAlchemy
- Redis
- Celery
- Langfuse
- Prometheus
- Grafana
- Docker