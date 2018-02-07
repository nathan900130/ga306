def rename_obj():
    m_sel = maya.cmds.ls(selection=True)
    newName = "polygon#"
    cmds.rename("%s" % (newName))

   
rename_obj()