import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    assistant_name: str = "Digital Alexey"

    ok_lets_go_url: str
    web_user_id: str

    openai_api_key: str
    system_prompt: str
    history_size: int
    history_ttl: int

    model_config = pydantic_settings.SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
