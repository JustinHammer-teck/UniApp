setup:
    pip install -m requirement.txt

fmt:
  black src/
  isort --atomic **/*.py

build-release:
    just fmt
    zip -r release/uniapp.zip * -x "/release"
