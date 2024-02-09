import pathlib

def extract_file_data( path_to_file ):
    data = []
    file_location = pathlib.Path( path_to_file ).resolve( )
    handle = open( file_location, 'r' )
    
    for line in handle:
        data.append( line )
    
    return data