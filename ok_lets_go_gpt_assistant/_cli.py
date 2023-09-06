import logging

from ._app import App
from ._settings import Settings


logger = logging.getLogger(__name__)


def entrypoint() -> None:
    try:
        settings = Settings()
        app = App(settings)

        logger.info("Application started")

        app.run()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        logging.info("Application ended")


if __name__ == "__main__":
    entrypoint()
