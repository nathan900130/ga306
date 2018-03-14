import maya.cmds;
cube = maya.cmds.polyCube()[0];
cap = "cap"

maya.cmds.connectAttr(cube+'.ry', "cap"+'.ry');
maya.cmds.select(cube);

maya.cmds.connectAttr(cube+'.rx', "cap"+'.ty');
maya.cmds.select(cube);