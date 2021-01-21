from OpenGL.GL import *
from glew_wish import *
import glfw 
import random

def main():
    #inicia glfw
    if not glfw.init():
        return

    #crea la ventana independientemente del SO
    window = glfw.create_window(800,600,"Mi ventana", None, None)

    #configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #validamos que se crre la ventana
    if not window:
        glfw.terminate()
        return 

    #establecemos el contexto
    glfw.make_context_current(window)
    #activamos la validación de funciones modernas
    glewExperimental = True

    #inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo iniciar GLEW")
        return

    #obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):

        color1= random.random()
        color2= random.random()
        color3= random.random()

        #establece region de dibujo
        glViewport(0,0,800,600)
        #establece color de borrado
        glClearColor(color1,color2,color3,1)
        #borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #dibujar

        #preguntar si hubo entradas de perifericos (Teclado, mouse, etc)
        glfw.poll_events()
        #intercambia los buffers
        glfw.swap_buffers(window)

    #se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #termina los procesos que inicio glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()