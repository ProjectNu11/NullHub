from datetime import datetime

from pydantic import BaseModel, validator


class Bot(BaseModel):
    """
    Bot model.
    """

    id: int
    name: str
    num: int = 0
    type: int = 1
    maintainer: list[dict[str, int | None]] = []
    register_time: datetime = datetime.fromtimestamp(0)


class ProjectNullBot(Bot):
    """
    ProjectNullBot model.
    """

    hashed_token: str
    is_active: bool = False
    last_seen: datetime = datetime.fromtimestamp(0)
    missed_heartbeat: tuple[int, datetime, bool] = [0, datetime.fromtimestamp(0), False]
    dev_group: list[int] = []
    owners: list[int] = []
    installed_modules: list[str] = []
    groups: list[int] = []
    activated: list[int] = []

    @validator("hashed_token")
    def check_hashed_token(cls, v):
        if len(v) != 32:
            raise ValueError("Hashed token must be 64 characters long.")
        return

    def update_password(self, password):
        """
        Update password.
        """

        self.hashed_token = password
