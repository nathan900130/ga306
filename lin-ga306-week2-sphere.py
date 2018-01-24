cmds.sphere( r=10 )
cmds.spaceLocator( p=(1, 1, 1) )

select -r nurbsSphere1 ;
select -tgl locator1 ;
parent;
