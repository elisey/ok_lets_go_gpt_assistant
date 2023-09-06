import logging

from ok_lets_go_gpt_assistant._cli import entrypoint


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


entrypoint()
