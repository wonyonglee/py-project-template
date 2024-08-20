import logging
from src.types import DataFrameType
from src.interfaces import TransformInterface

class TransformService(TransformInterface):
  def __init__(self, df_list: dict, rule_list: list[str]) -> None:
    self.__df_list = df_list
    self.__rule_list = rule_list

  def transform(self) -> dict[str, DataFrameType]:
    logging.info('Transform')
    return {}

  def preparation(self):
    logging.info('Preparation')