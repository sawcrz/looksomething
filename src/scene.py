import random
import OpenGL.GL  as ogl
import OpenGL.GLU as oglu
import constants

class Scene:
    def __init__( self, model, scale ):
        self.model = model
        self.scale = scale
        self.theta = 0.2
    
    def preconfig( self ):
        # set light source
        ogl.glLoadIdentity( )
        ogl.glLightfv( ogl.GL_LIGHT0, ogl.GL_SPECULAR, constants.LIGHT_SPECULAR )
        ogl.glLightfv( ogl.GL_LIGHT0, ogl.GL_DIFFUSE, constants.LIGHT_DIFFUSE )
        ogl.glLightfv( ogl.GL_LIGHT0, ogl.GL_POSITION, constants.LIGHT_POSITION )

        # enable flags
        ogl.glEnable( ogl.GL_LIGHTING )
        ogl.glEnable( ogl.GL_LIGHT0 )
        ogl.glEnable( ogl.GL_DEPTH_TEST )

    def render( self ):
        self.theta += 0.4 

        # aet the flush color
        ogl.glClearColor( 
            constants.RENDERER_FLUSH_COLOR[0],
            constants.RENDERER_FLUSH_COLOR[1],
            constants.RENDERER_FLUSH_COLOR[2],
            1.0
        )

        # configures the point size for the vertex view
        ogl.glPointSize( constants.POINT_SIZE )

        # clear the scene for re render
        ogl.glClear( ogl.GL_COLOR_BUFFER_BIT | ogl.GL_DEPTH_BUFFER_BIT )

        # transform the model
        ogl.glLoadIdentity( )
        ogl.glScalef( self.scale, self.scale, self.scale )
        ogl.glRotatef( self.theta, 0, 1, 1 )

        # render the parsed model 
        for face in self.model.faces:
            vertex_a = face[0][0] - 1
            vertex_b = face[1][0] - 1
            vertex_c = face[2][0] - 1

            normal_a = face[0][1] - 1
            normal_b = face[1][1] - 1
            normal_c = face[2][1] - 1

            ogl.glBegin( ogl.GL_TRIANGLES )
            
            ogl.glVertex3fv( self.model.vertices[vertex_a] )
            ogl.glVertex3fv( self.model.vertices[vertex_b] )
            ogl.glVertex3fv( self.model.vertices[vertex_c] )

            # adding normals per face
            ogl.glNormal3fv( self.model.normals[normal_a] )
            ogl.glNormal3fv( self.model.normals[normal_b] )
            ogl.glNormal3fv( self.model.normals[normal_c] )

            ogl.glEnd( )
            

