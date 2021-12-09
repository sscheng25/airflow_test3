with restaurants as (SELECT DISTINCT dba_name,longitude,latitude
FROM `musa-509-final.justtest.restaurant_2021-11-30` 
WHERE facility_type = 'Restaurant' and longitude is not null and latitude is not null ),

unique as (select dba_name,st_geogpoint(longitude,latitude) as geom
from restaurants),

check as (SELECT N.pri_neigh,R.dba_name,N.the_geom as neigh_geom, R.geom as res_geom, st_within(R.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN unique as R)

select * from check 
where test = TRUE 