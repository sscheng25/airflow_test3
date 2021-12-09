with restaurants as (SELECT DISTINCT dba_name,longitude,latitude
FROM `musa-509-final.justtest.restaurant_2021-11-30` 
WHERE facility_type = 'Restaurant' and longitude is not null and latitude is not null ),

unique as (select dba_name,st_geogpoint(longitude, latitude) as geom
from restaurants),

check as (select N.pri_neigh,R.dba_name,N.the_geom as neigh_geom, R.geom as res_geom, st_within(R.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN unique as R),

count as (SELECT res.pri_neigh,nei.the_geom,res.number
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS nei
right join 
(select pri_neigh,count(*) as number
from check
where test = TRUE 
group by pri_neigh) AS res
ON nei.pri_neigh = res.pri_neigh
Order by res.pri_neigh)

select *, 
       Case 
        when number >= (min(number) over()) and number < ((max(number) over())-(min(number) over()))/5+(min(number) over())then "1"
        when number >= ((max(number) over())-(min(number) over()))/5+(min(number) over()) and number < ((max(number) over())-(min(number) over()))/5*2+(min(number) over()) then "2"
        when number >= ((max(number) over())-(min(number) over()))/5*2+(min(number) over()) and number < ((max(number) over())-(min(number) over()))/5*3+(min(number) over()) then "3"
        when number >= ((max(number) over())-(min(number) over()))/5*3+(min(number) over()) and number < ((max(number) over())-(min(number) over()))/5*4+(min(number) over()) then "4"
        when number > ((max(number) over())-(min(number) over()))/5*4+(min(number) over()) then "5"
        END 
        AS summary
from count


