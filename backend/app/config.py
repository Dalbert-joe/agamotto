from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AGAMOTTO API"
    database_url: str = (
        "postgresql+psycopg://agamotto:agamotto@localhost:5432/agamotto"
    )
    jwt_secret: str = "dev-only-agamotto-secret-key-2026-32bytes"
    access_token_expire_minutes: int = 15

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
