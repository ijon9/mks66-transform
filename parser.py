from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r').read().split("\n")
    print(f)
    for i in range(0, len(f)):
        if f[i] == "line":
            print("line")
            pts = f[i+1].split(" ")
            for x in range(0, len(pts)):
                pts[x] = int(pts[x])
            add_edge(points, pts[0], pts[1], pts[2], pts[3], pts[4], pts[5])
        elif f[i] == "ident":
            print("ident")
            ident(transform)
        elif f[i] == "scale":
            print("scale")
            pts = f[i+1].split(" ")
            matrix_mult(make_scale(pts[0], pts[1], pts[2]), transform)
        elif f[i] == "translate":
            print("translate")
            pts = f[i+1].split(" ")
            matrix_mult(make_translate(pts[0], pts[1], pts[2]), transform)
        elif f[i] == "rotate":
            print("rotate")
            pts = f[i+1].split(" ")
            if pts[0] == "x":
                matrix_mult(make_rotX(pts[1]), transform)
            elif pts[0] == "y":
                matrix_mult(make_rotY(pts[1]), transform)
            elif pts[0] == "z":
                matrix_mult(make_rotZ(pts[1]), transform)
        elif f[i] == "apply":
            print("apply")
            matrix_mult(transform, points)
        elif f[i] == "display":
            print("display")
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif f[i] == "save":
            print("save")
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(f[i+1])
        elif f[i] == "quit":
            return

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
