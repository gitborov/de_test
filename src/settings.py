from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file= [
            os.path.join(os.path.join(os.path.dirname(os.getcwd()), ".env.dev")),
            os.path.join(os.path.join(os.path.dirname(os.getcwd()), ".env.secret")),
        ],
        env_file_encoding="utf-8",
    )
    host: str
    user: Optional[str] = os.getenv("USER")
    password: Optional[str] = os.getenv("PASSWORD")
    db: Optional[str] = os.getenv("DB")
    port_env: ClassVar[Optional[str]] = os.getenv("PORT")
    port: Optional[int] = int(port_env) if port_env is not None else None
    url: Optional[str] = os.getenv("URL")


settings = Settings()

"../.env.dev"

if __name__ == '__main__':
    print(settings.user)
