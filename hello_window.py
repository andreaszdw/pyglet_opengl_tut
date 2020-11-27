#!/usr/bin/env python


import pyglet
from pyglet.gl import *


class HelloWindow(pyglet.window.Window):

    def __init__(self):

        # create the window
        super(HelloWindow, self).__init__(
            width=800, height=600, resizable=True, caption="HelloWindow")
        pyglet.clock.schedule_interval(self.update, 1. / 60)

        # show the version of opengl
        print('OpenGL Version {}'.format(
            self.context.get_info().get_version()))

        # the clear color
        glClearColor(0.2, 0.3, 0.3, 1.0)

    def update(self, dt):
        pass

    def on_close(self):

        # exit the app
        pyglet.app.exit()

    def on_resize(self, width, height):

        # set the viewport
        glViewport(0, 0, width, height)

    def on_draw(self):

        # clear the screen
        glClear(GL_COLOR_BUFFER_BIT)


if __name__ == '__main__':
    window = HelloWindow()
    pyglet.app.run()
