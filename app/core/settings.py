from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_PATH = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH), env_file_encoding="utf-8", extra="ignore"
    )

    db_user: str = Field(validation_alias="DB_USER")
    db_password: SecretStr = Field(validation_alias="DB_PASSWORD")
    db_host: str = Field(validation_alias="DB_HOST")
    db_port: int = Field(validation_alias="DB_PORT")
    db_name: str = Field(validation_alias="DB_NAME")

    # JWT
    jwt_secret_key: str = Field(validation_alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(validation_alias="JWT_ALGORITHM")
    jwt_access_ttl_seconds: int = Field(validation_alias="JWT_ACCESS_TTL_SECONDS")
    jwt_issuer: str = Field(validation_alias="JWT_ISSUER")
    jwt_audience: str = Field(validation_alias="JWT_AUDIENCE")

    # Redis
    redis_url: str = Field(validation_alias="REDIS_URL")
    lock_ttl_sec: int = Field(validation_alias="LOCK_TTL_SEC")


settings = Settings()
