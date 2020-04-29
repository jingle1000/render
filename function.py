from flask import send_file
from subprocess import call

def render(request):
    location = '/tmp/'
    suffix = 'tempfile'
    filename = location + suffix + '0001.png'
    
    message = request.args.get('text', default = 'HELLO', type = str)
    
    scene = request.args.get('scene', default = 'basic', type = str)
    blender_file = "models/%s.blend" % scene

    # This script changes the text, it is run inside our 3D software. 
    blender_expression = f"import bpy; bpy.data.objects['Text'].data.body = '{message}'"
    blender_expression = "import bpy"
    command = f'../usr/local/blender/blender -b {blender_file} --python-expr "{blender_expression}" -o {location}frame_#### -f 1'
    # Render 3D image
    call(command, shell=True)
    
    return send_file("/tmp/frame_0001.png", mimetype='image/png')