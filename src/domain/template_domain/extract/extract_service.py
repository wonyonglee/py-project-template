import logging
from src.interfaces import ExtractInterface
from src.service import ObjectStorageService

class ExtractService(ExtractInterface):
  def __init__(self, object_storage_service: ObjectStorageService) -> None:
    self.oss = object_storage_service

  def extract(self) -> dict:
    logging.info('Extract')
    return {}