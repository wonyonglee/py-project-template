from abc import ABC, abstractmethod
from src.types.dataframe import DataFrameType

class ObjectStorageService(ABC):
  def __init__(self, connection_info) -> None:
    self.connection_info = connection_info

  @abstractmethod
  def start(self) -> None:
    pass

  @abstractmethod
  def stop(self) -> None:
    pass

  @abstractmethod
  def extractDataFrame(self, q) -> DataFrameType:
    pass

  @abstractmethod
  def load(self, path, df: DataFrameType):
    pass