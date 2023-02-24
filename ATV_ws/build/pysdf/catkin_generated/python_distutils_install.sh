#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/agtek/autonomous_ATV/ATV_ws/src/pysdf"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/agtek/autonomous_ATV/ATV_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/agtek/autonomous_ATV/ATV_ws/install/lib/python2.7/dist-packages:/home/agtek/autonomous_ATV/ATV_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/agtek/autonomous_ATV/ATV_ws/build" \
    "/usr/bin/python2" \
    "/home/agtek/autonomous_ATV/ATV_ws/src/pysdf/setup.py" \
     \
    build --build-base "/home/agtek/autonomous_ATV/ATV_ws/build/pysdf" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/agtek/autonomous_ATV/ATV_ws/install" --install-scripts="/home/agtek/autonomous_ATV/ATV_ws/install/bin"
