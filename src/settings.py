
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # env_file=("../.env.dev", "../src/.env.secret"),
        env_file=("C:\\Users\\SM\\PycharmProjects\\testing_de\\.env.dev", "../src/.env.secret"),
        env_file_encoding="utf-8",
    )

    URL: str
    NUM_PAGE: int

    HOST: str
    DB: str
    USER: str
    PASSWORD: str
    PORT: int
    SCHEME: str

settings = Settings()

# if __name__ == "__main__":
#     settings = Settings()