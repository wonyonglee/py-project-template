from enum import Enum

class Environment(Enum):
  SSH = 'ssh'
  DATABASE = 'database'
  OBJECT_STORAGE = 'object_storage'
  PROCESSOR = 'processor'
  PROFILE = 'profile'

class Profile(Enum):
  PROFILE = 'profile'
  LOCAL = 'local'
  DEV = 'dev'
  PROD = 'prod'

class ObjectStroage(Enum):
  KEY_ID = 'key_id'
  SECRET = 'secret'
  REGION = 'region'
  ENDPOINT = 'endpoint'
  BUCKET = 'bucket'

class Connection(Enum):
  HOST = 'host'
  PORT = 'port'
  USER = 'user'
  PASSWORD = 'password'

SWITCH = 'switch'
