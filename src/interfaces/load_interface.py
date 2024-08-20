from abc import ABC, abstractmethod

class LoadInterface(ABC):
  @abstractmethod
  def load(self, df_list: dict):
    pass