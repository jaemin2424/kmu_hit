execute_process(COMMAND "/home/jaemin/catkin_ws/build/diagnostics/diagnostic_updater/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jaemin/catkin_ws/build/diagnostics/diagnostic_updater/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
