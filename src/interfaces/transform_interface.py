from abc import ABC, abstractmethod

class TransformInterface(ABC):
  @abstractmethod
  def transform(self):
    pass

  @abstractmethod
  def preparation(self):
    pass