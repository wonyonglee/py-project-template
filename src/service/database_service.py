import logging
from abc import ABC, abstractmethod

class DatabaseService(ABC):
  @abstractmethod
  def __init__(self, connection_info) -> None:
    """
    :param connection_info: host, port, user, password
    """
    pass

  @abstractmethod
  def start(self) -> None:
    pass

  @abstractmethod
  def stop(self) -> None:
    pass

  @abstractmethod
  def fetchAll(self, query) -> dict:
    """
    :param query:
    :return: {
      columns: []
      list: []
    }
    """
    pass

  @abstractmethod
  def fetchOne(self, query) -> dict:
    pass