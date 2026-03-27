import sys
import os

print(f'현재 실행중인 python 경로: {sys.executable}' )
print(f"가상환경 활성화 여부: {os.environ.get('VIRTUAL_ENV')}")