import maya.cmds;
def addSpikes(obj):
    try: polycount = maya.cmds.polyEvaluate(obj, face=True);
    except: raise;
    for i in range(0, polycount):
        face = '%s.f[%s]'%(obj, i);
        maya.cmds.polyExtrudeFacet(face, ltz=1, ch=0);
        maya.cmds.polyExtrudeFacet(
            face, ltz=1, ch=0,
            ls=[0.1, 0.1, 0.1]
        );
    maya.cmds.polySoftEdge(obj, a=180, ch=0);
    maya.cmds.select(obj);
print('module name: %s'%__name__);
print('globals:');
for k in globals().keys(): print('\t%s'%k);

 # Add this above to a script, then add the following line below a desired polygon for spikes.
addSpikes(maya.cmds.polyPrimitive(ch=0)[0]);