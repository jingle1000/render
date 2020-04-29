import bpy

txt = bpy.data.objects["Text"]
bg = bpy.data.objects["Cube"]

txt.data.body = "My Test"

size = txt.bound_box.data.dimensions[0]

bg.scale[0] = size / 2