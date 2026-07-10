# ADR-003: Repository Pattern

Services depend on Repository classes only. A service that calls an API client, HTTP client,
or database/ORM directly bypasses the repository layer and violates this decision.

Keyword tags: repository, service, API client, data access, database.