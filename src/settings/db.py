from pydantic import (BaseSettings, Field, BaseModel)
import os

base_dir = os.path.join(os.path.join(os.path.dirname(os.getcwd())), ".env.dev")
print(base_dir)
base_sir2 = 'C:\\Users\\SM\\PycharmProjects\\testing_de\\.env.dev'


class DbSettings(BaseSettings):
    postgres_host: str = Field(env='HOST')
    DB_name: str = Field(env='DB')
    user_name: str = Field(env='USER')
    password: str = Field(env='PASSWORD')
    port: int = Field(env='PORT')

    class Config:
        env_file = base_sir2


class ApiSettings(BaseSettings):
    url: str = Field(env='URL')

    class Config:
        env_file = base_sir2


class Settings(BaseSettings):
    db = DbSettings()
    api = ApiSettings()

    # class Config:
    #     env_file = base_dir


#
#
settings = Settings()
print(settings.api.url)

# settings = DbSettings()
