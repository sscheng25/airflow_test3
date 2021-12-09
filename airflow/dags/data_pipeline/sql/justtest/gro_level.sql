with grocery as (select store_name,st_geogpoint(longitude, latitude) as geom
from `musa-509-final.justtest.grocery_2021-11-30`),

check as (SELECT N.pri_neigh,G.store_name,N.the_geom as neigh_geom, G.geom as gro_geom, st_within(G.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN grocery as G),

count as (SELECT gro.pri_neigh,nei.the_geom,gro.number
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS nei
right join 
(select pri_neigh,count(*) as number
from check
where test = TRUE 
group by pri_neigh) AS gro
ON nei.pri_neigh = gro.pri_neigh
Order by gro.pri_neigh)

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


