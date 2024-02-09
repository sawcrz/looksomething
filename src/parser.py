import constants
import model

def parse_normal( normal ):
    return( float( normal[1] ), float( normal[2] ), float( normal[3] ) )

def parse_face( face ):
    clean_pairs = []
    face.remove('f')
    groups = [ face[0].split( '//' ), face[1].split( '//' ), face[2].split( '//' ) ]

    for group in groups:
        clean_pairs.append( [ int( group[0] ), int( group[1] ) ] )

    return clean_pairs

def parse_vertex( vertex ):
    return( float( vertex[1] ), float ( vertex[2] ), float( vertex[3] ) )

def parse_model( model_data ):
    vertices = []
    normals = []
    faces = []
    name = ''

    for item in model_data:
        slices = item.split( ' ' )
        if( slices[0] == constants.PARSER_VERTEX_TOKEN ):
            vertices.append( parse_vertex( slices ) )
        elif( slices[0] == constants.PARSER_FACE_TOKEN ):
            faces.append( parse_face( slices ) )
        elif( slices[0] == constants.PARSER_NORMAL_TOKEN ):
            normals.append( parse_normal( slices ) )
        elif( slices[0] == constants.PARSER_OBJECT_TOKEN ):
            name = slices[1]
    
    return model.Model( name, vertices, faces, normals )