from pathlib import Path

from pydantic import BaseModel, validator, root_validator, AnyHttpUrl


class DataPath(BaseModel):
    generic: Path = Path(Path().resolve(), "data")
    modules: Path = Path(Path().resolve(), "modules")
    cache: Path = Path(Path().resolve(), "cache")

    @root_validator()
    def __validate_path(cls, values):
        for key, value in values.items():
            if not value.exists():
                value.mkdir(parents=True)
        return values


class AppPath(BaseModel):
    metadata: str = "metadata"
    authorize: str = "authorize"
    get_me: str = "getMe"
    get_bot_list: str = "getBotList"
    heartbeat: str = "heartbeat"
    notified_missing: str = "notifiedMissing"
    online_event: str = "onlineEvent"
    offline_event: str = "offlineEvent"
    register_bot: str = "registerBot"
    announcement: str = "announcement"
    module_metadata: str = "moduleMetadata"
    download_module: str = "downloadModule"
    search_module: str = "searchModule"

    @root_validator()
    def __check_duplicate(cls, values):
        if len(values.values()) != len(set(values.values())):
            raise ValueError("Duplicate path found.")
        return values


class Config(BaseModel):
    title: str = "Project. Null Hub"
    port: int = 5000
    base: str = ""
    data_path: DataPath = DataPath()
    app_path: AppPath = AppPath()
    repo_path: AnyHttpUrl = (
        "https://api.github.com/repos/ProjectNu11/PN-Plugins/zipball/main"
    )
    app_arguments: dict = {}
    uvicorn_arguments: dict = {}

    @validator("base")
    def __validate_base(cls, v):
        print(v)
        if v == "":
            return v
        if not v.startswith("/"):
            v = f"/{v}"
        if v.endswith("/"):
            raise ValueError("Base path must not end with /.")
        return v

    def get_app_path(self, path: str) -> str:
        return self.base + path


config = Config()
