# ADR-002: Configuration

Configuration and secrets are loaded from environment variables or a single config module.
Modules do not hardcode configuration values or read environment variables ad hoc in
multiple places.