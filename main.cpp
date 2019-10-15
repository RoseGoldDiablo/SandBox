#include <iostream>

#include "src/graphics/window.h"

int main()
{
    using namespace gameEngine;
    using namespace graphics;
    Window window("Brooks", 1500, 1000);
    glClearColor(0.2f, 0.3f, 0.8f, 1.0f);

    while (!window.closed())
    {
        std::cout << window.getWidth() << ", " << window.getHeight() <<std::endl;
        window.clear();
        glBegin(GL_TRIANGLES);
        glVertex2f(-0.5f,-0.5);
        glVertex2f(0.0f, 0.5f);
        glVertex2f(0.5f, -0.5);
        glEnd();
        window.update();
    }
    return 0;
}