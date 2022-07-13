from fastapi import FastAPI, APIRouter

from library.model.config import config
from library.model.response import GenericSuccess, GenericError

app = FastAPI(title=config.title, **config.app_arguments)

router = APIRouter(prefix=config.base)


@router.get("/test/success")
def test_success():
    return GenericSuccess("Hello World!")


@router.get("/test/error/{code}")
def test_error_code(code: int):
    return GenericError(code, "Hello World!")
