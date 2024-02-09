class Model:
    def __init__( self, name = 'model', vertices = [], faces = [], normals = [] ):
        self.name = name
        self.faces = faces
        self.vertices = vertices 
        self.normals = normals

    def set_name( self, new_name ):
        self.name = new_name

    def set_vertices( self, vertex_list ):
        self.vertices = vertex_list
    
    def set_faces( self, face_list ):
        self.faces = face_list
    
    def set_normals( self, normals ):
        self.normals = normals
        