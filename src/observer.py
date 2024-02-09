import pygame
import constants
import file_handle
import OpenGL.GL as ogl

class Observer:
    def __init__( self ):
        self.alive = True
        self.clock = pygame.time.Clock( )
        self.current_forced_fps = constants.DEFAULT_FPS

    def increase_fps( self, ammount ):
        if( not ( self.current_forced_fps + ammount > constants.DEFAULT_FPS ) ):
            self.current_forced_fps += ammount
    
    def decrease_fps( self, ammount ):
        if( not ( self.current_forced_fps - ammount <= 0 ) ):
            self.current_forced_fps -= ammount
    
    def update_clock( self ):
        self.clock.tick( self.current_forced_fps )

    def load_resources( self, file_path ):
        return file_handle.extract_file_data( file_path )
    
    def set_wireframe( self ):
        ogl.glPolygonMode( ogl.GL_FRONT_AND_BACK, ogl.GL_LINE )

    def set_filled( self ):
        ogl.glPolygonMode( ogl.GL_FRONT_AND_BACK, ogl.GL_FILL )

    def set_vertex( self ):
        ogl.glPolygonMode( ogl.GL_FRONT_AND_BACK, ogl.GL_POINT )

    def manage_keyboard_event( self, key ):
        if( key == pygame.K_ESCAPE ):
            self.alive = False
        elif( key == pygame.K_F1 ):
            self.set_filled( )
        elif( key == pygame.K_F2 ):
            self.set_wireframe( )
        elif( key == pygame.K_F3 ):
            self.set_vertex( )

    def poll_events( self ):
        for event in pygame.event.get( ):
            if( event.type == pygame.QUIT ):
                self.alive = False
            elif( event.type == pygame.KEYDOWN ):
                self.manage_keyboard_event( event.key )