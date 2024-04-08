rm -r dist
python setup.py bdist_wheel
rm -r build
rm -r pyautogen.egg-info
if [ -n "$1" ]
then
  cp dist/*.* "$1"
fi
