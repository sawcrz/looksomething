import pygame

# parser tokens for the .obj format
PARSER_OBJECT_TOKEN = 'o'
PARSER_VERTEX_TOKEN = 'v'
PARSER_FACE_TOKEN   = 'f'
PARSER_NORMAL_TOKEN = 'vn'

# screen init configurations
WINDOW_SIZE = ( 200, 200 )
VIDEO_FLAGS = pygame.OPENGL | pygame.DOUBLEBUF | pygame.NOFRAME

DEFAULT_FPS = 60

# on render coloring configurations
DEFAULT_FLUSH_COLOR = '#333333'
RENDERER_FLUSH_COLOR = ( 0.133, 0.133, 0.133 )

# for the vertex view
POINT_SIZE = 2.0

MODEL_COLOR = ( 0.7, 0.7, 0.7 ) # floating point

# light modifiers
LIGHT_SPECULAR = ( 0.6, 0.6, 0.6 )
LIGHT_DIFFUSE = ( 0.5, 0.5, 0.5 )
LIGHT_POSITION = ( 0.0, -1.0, 0.0, 0.0 )
LIGHT_SHININESS = ( 10.0 )
