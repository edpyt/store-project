from pathlib import Path
from typing import Literal

from src.application.common.config import Config
from src.application.common.config.parser.config_reader import read_config
from src.infrastructure.db.config import DBConfig


def load_config(
    path: str | None = None, type_config: Literal["all", "db"] = "all",
) -> Config | DBConfig:
    if path is None:
        path = "./config_dist/dev_config.yml"
    path_obj = Path(path)

    config_data: dict = read_config(path_obj)
    db_config: DBConfig = DBConfig(**config_data["db"])

    config: Config = Config(db=db_config)

    match type_config:
        case "db":
            return db_config
        case _:
            return config
