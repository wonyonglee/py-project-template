import os
import logging
from src.constant.common import Environment
from src.constant.define import get_env_variable
from src.libraries.duckdb_python import DuckDBPython
from .extract.extract_service import ExtractService
from .transform.transform_service import TransformService
from .load.load_service import LoadService

# 도메인별 환경변수 설정시 사용
def define_domain_env(env):
  env['domain_env'] = {
    'use_domain': get_env_variable('USE_DOMAIN')
  }
  return env

def run(env):
  logging.info(env[Environment.PROCESSOR])
  env = define_domain_env(env)
  logging.debug(env)
  duckdb_python = DuckDBPython(connection_info=env[Environment.OBJECT_STORAGE])
  duckdb_python.start()
  extract_service = ExtractService(object_storage_service=duckdb_python)
  extract_service.extract()
  transform_service = TransformService(df_list={}, rule_list=[])
  transform_service.preparation()
  transform_service.transform()
  load_service = LoadService(object_storage_service=duckdb_python)
  load_service.load(df_list={})
  duckdb_python.stop()

  logging.info(f'{env[Environment.PROCESSOR]} processor is done.')


