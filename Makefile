# --- VARIABLES ---
# Path to the environment file and docker-compose configuration
DC = docker compose --env-file .env -f infra/docker-compose.yml
ENV_FILE = .env

# --- INFRASTRUCTURE MANAGEMENT ---

.PHONY: up down restart ps init-topics

# Spin up all services (Postgres, Redpanda, ChromaDB) in detached mode
up:
	$(DC) up -d

# Stop and remove all containers defined in docker-compose
down:
	$(DC) down

# Restart services (useful for refreshing environment variables)
restart:
	$(DC) down && $(DC) up -d

# List all running project containers and their status
ps:
	$(DC) ps

# Initialize Redpanda topics for the data pipeline
# Run this once after the initial 'make up'
init-topics:
	docker exec -it maylily-redpanda rpk topic create raw_knitting_events curated_knitting_ideas

# --- DEVELOPMENT ENVIRONMENT ---

.PHONY: venv install

# Create a local Python virtual environment
venv:
	python3 -m venv venv
	@echo "Virtual environment created. To activate, run: source venv/bin/activate"

# Install Python dependencies from requirements.txt
install:
	pip install --upgrade pip
	pip install -r requirements.txt