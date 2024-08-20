from abc import ABC, abstractmethod

class ExtractInterface(ABC):
  @abstractmethod
  def extract(self):
    pass

