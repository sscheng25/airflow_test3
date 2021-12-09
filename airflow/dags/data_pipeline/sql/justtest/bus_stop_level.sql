with bus_stop as (select systemstop,st_geogpoint(point_x, point_y) as geom
from `musa-509-final.justtest.bus_stop_2021-11-30`),

check as (SELECT N.pri_neigh,B.systemstop,N.the_geom as neigh_geom, B.geom as stop_geom, st_within(B.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN bus_stop as B),

count as (SELECT stop.pri_neigh,nei.the_geom,stop.number
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS nei
right join 
(select pri_neigh,count(*) as number
from check
where test = TRUE 
group by pri_neigh) AS stop
ON nei.pri_neigh = stop.pri_neigh
Order by stop.pri_neigh)

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


