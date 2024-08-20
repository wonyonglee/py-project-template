import os
from .common import Environment, Connection, ObjectStroage, Profile, SWITCH

def transform_port(port):
  if port is None:
    return port
  return int(port)

def get_env_variable(name: str, default=None) -> str:
  return os.getenv(name, default)

def define_env():
  # 기본값 설정
  env_profile = get_env_variable('PROFILE', Profile.PROD)
  env_processor = get_env_variable('PROCESSOR')

  ssh_config = {
    SWITCH: get_env_variable('SSH_SWITCH'),
    Connection.HOST: get_env_variable('SSH_HOST'),
    Connection.PORT: get_env_variable('SSH_PORT'),
    Connection.USER: get_env_variable('SSH_USER'),
    Connection.PASSWORD: get_env_variable('SSH_PASSWORD')
  }

  database_config = {
    Connection.HOST: get_env_variable('VERTICA_HOST'),
    Connection.PORT: get_env_variable('VERTICA_PORT'),
    Connection.USER: get_env_variable('VERTICA_USER'),
    Connection.PASSWORD: get_env_variable('VERTICA_PASSWORD')
  }

  object_storage_config = {
    ObjectStroage.KEY_ID: get_env_variable('KEY_ID'),
    ObjectStroage.SECRET: get_env_variable('SECRET'),
    ObjectStroage.REGION: get_env_variable('REGION'),
    ObjectStroage.ENDPOINT: get_env_variable('ENDPOINT'),
    ObjectStroage.BUCKET: get_env_variable('BUCKET')
  }

  return {
    Environment.PROFILE: env_profile,
    Environment.PROCESSOR: env_processor,
    Environment.SSH: ssh_config,
    Environment.DATABASE: database_config,
    Environment.OBJECT_STORAGE: object_storage_config
  }