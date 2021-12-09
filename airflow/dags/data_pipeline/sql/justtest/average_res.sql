with restaurants as (SELECT DISTINCT dba_name,longitude,latitude
FROM `musa-509-final.justtest.restaurant_2021-11-30` 
WHERE facility_type = 'Restaurant' and longitude is not null and latitude is not null ),

unique as (select dba_name,st_geogpoint(longitude,latitude) as geom
from restaurants),

check as (SELECT N.pri_neigh,R.dba_name,N.the_geom as neigh_geom, R.geom as res_geom, st_within(R.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN unique as R),

res_in_neigh as(
    select pri_neigh, count(dba_name) as num_res
    from check 
    where test = TRUE 
    group by pri_neigh
)
select avg(num_res) as mean_res
from res_in_neigh 