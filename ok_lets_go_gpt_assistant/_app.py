import logging
import typing

import gpt_assistant_lib
import socketio  # type:ignore[import]

from ._settings import Settings


logger = logging.getLogger(__name__)

HISTORY_USER_ID = "no_user_id"


class App:
    def __init__(self, settings: Settings) -> None:
        self.assistant_name = settings.assistant_name

        self.socketio_client = socketio.Client(logger=True, engineio_logger=True)
        self.ok_lets_go_url = settings.ok_lets_go_url
        self.socketio_client.on("message", self._on_message)
        self.socketio_client.on("connect", self._on_connected)
        self.web_user_id = settings.web_user_id

        self.assistant = gpt_assistant_lib.build_assistant(
            settings.openai_api_key,
            settings.system_prompt,
            settings.history_size,
            settings.history_ttl,
        )

    def run(self) -> None:
        self.socketio_client.connect(self.ok_lets_go_url)
        self.socketio_client.wait()

    def _on_connected(self) -> None:
        self.socketio_client.emit("set_name", {"name": self.assistant_name})

    def _on_message(self, data: dict[str, typing.Any]) -> None:
        logger.info("Message received", extra=data)

        user_name = data["message"]["user"]
        input_message = data["message"]["content"]
        if user_name == self.assistant_name:
            return

        logger.info(f"{user_name}: {input_message}")

        try:
            response = self.assistant.exchange(HISTORY_USER_ID, input_message)
        except gpt_assistant_lib.GptAssistantBaseException as e:
            logging.exception(f"GPT assistant exception, {e}")
            return

        self.socketio_client.send({"message": response, "user_id": self.web_user_id})
