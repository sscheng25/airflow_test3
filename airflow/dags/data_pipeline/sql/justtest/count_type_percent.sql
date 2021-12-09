with crimes as (select id,date,primary_type,st_geogpoint(longitude, latitude) as geom
from `musa-509-final.justtest.crime_2021-11-30`
WHERE date between DATE_SUB(current_date(), INTERVAL 30 DAY) and current_date()),

check as (SELECT N.pri_neigh,C.id,C.primary_type,C.date, N.the_geom as neigh_geom, C.geom as crime_geom, st_within(C.geom,N.the_geom) as test
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
CROSS JOIN crimes as C),

crime_in_neigh as (
SELECT cri.pri_neigh,nei.the_geom,cri.primary_type,cri.number 
FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS nei
right join 
(select pri_neigh,primary_type,count(id) as number
from check
where test = TRUE 
group by pri_neigh,primary_type) AS cri
ON nei.pri_neigh = cri.pri_neigh
Order by cri.pri_neigh),
total as(
    select sum(number) as total_num
    from crime_in_neigh
)

select primary_type, sum(number) as count_type, sum(number)*100/(select total_num from total) as percent_type
from crime_in_neigh
group by primary_type
order by count_type desc