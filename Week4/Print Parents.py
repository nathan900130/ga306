cmds.polyCube(n='Cube')
cmds.polySphere(n='Sphere')
cmds.polyCylinder(n='Cylinder')
cmds.polyTorus(n='Torus')

cmds.parent('Cube', 'Sphere', 'Cylinder', 'Torus')

shapes = cmds.listRelatives('Cube');
cmds.listRelatives( shapes[0], allParents=True);
