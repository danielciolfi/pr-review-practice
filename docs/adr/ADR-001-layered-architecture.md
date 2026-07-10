# ADR-001: Layered Architecture

Business logic lives in the service layer. Entrypoints â€” CLI commands, route handlers, or a
script's main() â€” parse input and format output only. They must not contain business logic
or perform data access directly.