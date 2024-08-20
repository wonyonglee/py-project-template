import os
import importlib
import logging
from src.constant.define import define_env
from src.constant.common import Environment
from src.domain import DOMAIN_PROCESSOR_MAP
from run_module import run_module_with_tunneling

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s [%(levelname)s] %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
)

try:
  env = define_env()
  module_name = DOMAIN_PROCESSOR_MAP[env[Environment.PROCESSOR]]
  module = importlib.import_module(module_name)
  run_module_with_tunneling(env=env, module=module)

finally:
  logging.info('finally')
