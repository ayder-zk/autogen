rm -r dist
python setup.py bdist_wheel
rm -r build
rm -r pyautogen.egg-info
cp dist/*.* "$1"
