with crime_oct as(
    select id, date, primary_type, st_geogpoint(longitude, latitude) as geom
    from `musa-509-final.justtest.crime_2021-11-30`
    where date >='2021-10-01' and date < '2021-11-01'
    order by date
),
crime_nhood as (
    select N.pri_neigh, C.id, N.the_geom as neigh_geom, C.geom as crime_geom
    FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
    cross join crime_oct as C
    where st_within(C.geom,N.the_geom)
),
crime_final as (
	select pri_neigh, count(id) as num_crime
	from crime_nhood
	group by pri_neigh
)
select * 
from crime_final
order by num_crime 
limit 1