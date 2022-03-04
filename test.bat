set CWD=%~dp0

pushd %CWD%

set PYTHONPATH=%CWD%build
python.exe src/test/main.py

popd
