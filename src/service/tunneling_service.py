import logging
from sshtunnel import SSHTunnelForwarder
from src.constant.common import Connection

LOCAL_BIND_IP = '127.0.0.1'
LOCAL_BIND_PORT = 5434

def remote_connection_override(connection_info):
  connection_info[Connection.HOST] = LOCAL_BIND_IP
  connection_info[Connection.PORT] = LOCAL_BIND_PORT
  return connection_info


class TunnelingService():
  def __init__(self, remote_host: str, remote_port: int, host: str, port: int, user: str, password: str) -> None:
    self.server = SSHTunnelForwarder(
      (host, port),
      ssh_username=user,
      ssh_password=password,
      remote_bind_address=(remote_host, remote_port),
      local_bind_address=(LOCAL_BIND_IP, LOCAL_BIND_PORT)
    )

  def start(self):
    logging.info('Start Tunneling')
    self.server.start()

  def stop(self):
    logging.info('Stop Tunneling')
    self.server.stop()

