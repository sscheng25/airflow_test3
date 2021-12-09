with grocery as (select store_name,st_geogpoint(longitude,latitude) as geom
from `musa-509-final.justtest.grocery_2021-11-30`),

check as (SELECT N.pri_neigh,G.store_name,N.the_geom as neigh_geom, G.geom as gro_geom, st_within(G.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN grocery as G),

gro_in_neigh as(
    select pri_neigh, count(store_name) as num_gro 
    from check 
    where test = TRUE 
    group by pri_neigh
)
select pri_neigh, num_gro 
from gro_in_neigh 
order by num_gro desc
limit 1