from logging import getLogger

from logs import my_log
from src.math_area import area

module_name = "app"
logger = getLogger(module_name)


def main() -> None:
    logger.info(area.calculate_area_square(5))
