with busstop as (select systemstop,st_geogpoint(point_x,point_y) as geom
from `musa-509-final.justtest.bus_stop_2021-11-30`),

check as (SELECT N.pri_neigh,B.systemstop,N.the_geom as neigh_geom, B.geom as stop_geom, st_within(B.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN busstop as B)

select * from check 
where test = TRUE 