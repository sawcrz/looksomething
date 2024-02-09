import pygame
import os

import scene
import observer
import constants
import parser

pygame.init( )

# set the window position
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( 20, 60 )

screen = pygame.display.set_mode( constants.WINDOW_SIZE, constants.VIDEO_FLAGS )
runtime_observer = observer.Observer( )

runtime_scene = scene.Scene( 
    parser.parse_model( 
        runtime_observer.load_resources( 'assets/kube.obj' ) 
    ), 0.5
)

runtime_scene.preconfig( )

while runtime_observer.alive:
    runtime_observer.poll_events( )

    screen.fill( constants.DEFAULT_FLUSH_COLOR )
    runtime_scene.render( )
    pygame.display.flip( )
    runtime_observer.update_clock( )

pygame.quit( )