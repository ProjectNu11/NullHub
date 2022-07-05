from fastapi import FastAPI

from library.model.config import config

app = FastAPI(title=config.title, **config.app_arguments)
