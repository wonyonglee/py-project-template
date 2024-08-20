import logging
import duckdb
from src.constant.common import ObjectStroage
from src.types import DataFrameType
from src.service import ObjectStorageService

class DuckDBPython(ObjectStorageService):
  def start(self) -> None:
    q = f"""
      INSTALL httpfs;
      LOAD httpfs;
      
      CREATE SECRET secret_object_storage (
        TYPE S3,
        KEY_ID '{self.connection_info[ObjectStroage.KEY_ID]}',
        SECRET '{self.connection_info[ObjectStroage.SECRET]}',
        REGION '{self.connection_info[ObjectStroage.SECRET]}',
        ENDPOINT '{self.connection_info[ObjectStroage.ENDPOINT]}',
        URL_STYLE 'path',
        USE_SSL false
      );
    """
    logging.debug(q)
    duckdb.query(q)

  def stop(self) -> None:
    duckdb.close()

  def extractDataFrame(self, query: str) -> DataFrameType:
    return duckdb.query(query).pl()

  def load(self, path: str, df: DataFrameType):
    duckdb.query(f"""
      COPY (
        SELECT * FROM df
      ) TO '{path}' (FORMAT PARQUET)
    """)

