with crimes as (select id,st_geogpoint(longitude, latitude) as geom
from `musa-509-final.justtest.crime_2021-11-30`),

check as (SELECT N.pri_neigh,C.id, N.the_geom as neigh_geom, C.geom as crime_geom, st_within(C.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN crimes as C)

select pri_neigh, count(id) as num_crimes
from check 
where test = TRUE 
group by pri_neigh