import maya.cmds;
cube = maya.cmds.polyCube()[0];
cart = create_car("test_car")

maya.cmds.connectAttr(cube+'.rx', cart+'.tx');
maya.cmds.select(cube);

maya.cmds.connectAttr(cube+'.rz', cart+'.tz');
maya.cmds.select(cube);