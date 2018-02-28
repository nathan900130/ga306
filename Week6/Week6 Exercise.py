
import maya.cmds
sphere = maya.cmds.polySphere(radius = 0.5)[0]
cube = maya.cmds.polyCube()[0]


maya.cmds.connectAttr(cube+'.ry', sphere+'.ty')
mult = maya.cmds.createNode('multiplyDivide');
maya.cmds.connectAttr(cube+'.ry', mult+'.input1x');
maya.cmds.setAttr(mult+'.input2X', 1.0/90/0);
maya.cmda.connectAttr(mult+'.outputX'. sphere+'.ty');
maya.cmds.select(cube)
