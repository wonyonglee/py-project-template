import logging
from src.types import DataFrameType
from src.interfaces import LoadInterface
from src.service import ObjectStorageService

class LoadService(LoadInterface):
  def __init__(self, object_storage_service: ObjectStorageService) -> None:
    self.oss = object_storage_service

  def load(self, df_list: dict[str, DataFrameType]):
    return {}

