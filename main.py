import uvicorn

from library.model.config import config

if __name__ == "__main__":
    uvicorn.run(
        "app.app:app",
        port=config.port,
        log_level="info",
        # reload=True,
        # reload_dirs=["app", "library"],
        **config.uvicorn_arguments,
    )
