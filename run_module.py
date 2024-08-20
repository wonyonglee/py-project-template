from src.constant.common import Environment, Connection, SWITCH
# from src.service.tunneling_service import TunnelingService, remote_connection_override
def run_module_with_tunneling(env, module):
  ssh_switch = env[Environment.SSH][SWITCH]

  # if ssh_switch:
    # return _run_with_tunneling(env, module)

  _run_without_tunneling(env, module)

# def _run_with_tunneling(env, module):
#   tunneling_service = TunnelingService(env[Environment.DATABASE][Connection.HOST], env[Environment.DATABASE][Connection.PORT], **env[Environment.SSH])
#   tunneling_service.start()
#   env[Environment.DATABASE] = remote_connection_override(env[Environment.DATABASE])
#   try:
#     _run_module(env, module)
#   finally:
#     tunneling_service.stop()

def _run_without_tunneling(env, module):
  _run_module(env, module)

def _run_module(env, module):
  if hasattr(module, 'run'):
    module.run(env)

__all__ = [
  "run_module_with_tunneling",
]