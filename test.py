import platform
from setuptools.msvc import EnvironmentInfo

ARCH = platform.machine()
print(f'Setting up environment for MSVC on {ARCH}')
env = EnvironmentInfo(ARCH).return_env()
for key, value in env.items():
    print(f'{key}="{value}"')
