cmake_minimum_required(VERSION 3.15)
project(gameEngine)
set(CMAKE_CXX_STANDARD 14)




add_executable(gameEngine main.cpp src/graphics/window.cpp src/graphics/window.h src/graphics/window.cpp)



target_link_libraries(gameEngine glfw ${GLFW_LIBRARIES})
find_package(OpenGL REQUIRED)

target_include_directories(gameEngine PUBLIC ${OPENGL_INCLUDE_DIR})
target_link_libraries(gameEngine ${OPENGL_gl_LIBRARY})
target_link_libraries(gameEngine ${OPENGL_glu_LIBRARY} ${GLFW_LIBRARIES})