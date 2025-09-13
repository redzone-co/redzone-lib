.PHONY: help
help:
	clear
	@echo -------------------------------
	@echo - Makefile Target Information -
	@echo -------------------------------
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: check
check: ## Lint, Type Check, and Format
	docker compose up -d
	clear
	@echo -------------------------------
	@echo Linting
	@echo -------------------------------
	docker compose run --rm --remove-orphans redzone flake8 . --show-source --statistic

	@echo -------------------------------
	@echo Type Checking
	@echo -------------------------------
	docker compose run --rm --remove-orphans redzone mypy .

	@echo -------------------------------
	@echo Formatting
	@echo -------------------------------
	docker compose run --rm --remove-orphans redzone black --check --diff .
	docker compose run --rm --remove-orphans redzone isort --check-only .


.PHONY: lint
lint: ## Lint
	clear
	@echo -------------------------------
	@echo Linting
	@echo -------------------------------
	docker compose run --rm --remove-orphans redzone flake8 . --show-source --statistic


.PHONY: type
type: ## Type Check
	clear
	@echo -------------------------------
	@echo Type Checking
	@echo -------------------------------
	docker compose run --rm --remove-orphans redzone mypy .


.PHONY: format
format: ## Format
	clear
	@echo -------------------------------
	@echo Formatting
	@echo -------------------------------
	docker compose run --rm --remove-orphans redzone black .
	docker compose run --rm --remove-orphans redzone isort .



%: ## ignore all commands that are not defined
	@:
