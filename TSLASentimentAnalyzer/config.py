from pydantic import BaseSettings


class Settings(BaseSettings):

    reddit_api_client_id: str
    reddit_api_client_secret: str
    stock_data_api_key: str
    reddit_api_user_agent: str = "USERAGENT"
    model_path: str = "fourthbrain-demo/model_trained_by_me2"

    class Config:
        env_file = ".env"  # defaults to no prefix, i.e. ""


settings = Settings()
