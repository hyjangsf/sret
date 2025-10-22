import sys

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("가상환경 안입니다.")
else:
    print("가상환경이 아닙니다.")
