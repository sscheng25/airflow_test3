with crimes as (
	select id,date,primary_type,st_geogpoint(longitude, latitude) as geom
	from `musa-509-final.justtest.crime_2021-11-30`
	WHERE date between DATE_SUB(current_date(), INTERVAL 30 DAY) and current_date()
),
check as (
	SELECT N.pri_neigh,C.id,C.primary_type,C.date, N.the_geom as neigh_geom, C.geom as crime_geom, st_within(C.geom,N.the_geom) as test
	FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
	CROSS JOIN crimes as C
),
crime_in_neigh as (
	SELECT cri.pri_neigh,nei.the_geom,cri.primary_type,cri.number 
	FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS nei
	right join 
	(select pri_neigh,primary_type,count(id) as number
	from check
	where test = TRUE 
	group by pri_neigh,primary_type) AS cri
	ON nei.pri_neigh = cri.pri_neigh
	Order by cri.pri_neigh
),
crime_final as (
	select pri_neigh, sum(number) as num_crime
	from crime_in_neigh
	group by(pri_neigh)
),
busstop as (
	select systemstop,st_geogpoint(point_x,point_y) as geom
	from `musa-509-final.justtest.bus_stop_2021-11-30`
),
check_bus as (
	SELECT N.pri_neigh,B.systemstop,N.the_geom as neigh_geom, B.geom as stop_geom
    from busstop as B
	cross join `musa-509-final.justtest.neighborhood_2021-12-01` AS N
    where st_within(B.geom,N.the_geom)
),
busstop_final as (
    select pri_neigh, count(systemstop) as num_busstop
	from check_bus
    group by pri_neigh
),
crime_bus as (
	select c.*, b.num_busstop
	from crime_final as c 
	join busstop_final as b 
	on c.pri_neigh = b.pri_neigh
),
grocery as (
	select store_name,st_geogpoint(longitude,latitude) as geom
	from `musa-509-final.justtest.grocery_2021-11-30`
),
check_grocery as (
	SELECT N.pri_neigh,G.store_name,N.the_geom as neigh_geom, G.geom as gro_geom
	FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
	CROSS JOIN grocery as G
	where st_within(G.geom,N.the_geom)
),
grocery_final as (
	select pri_neigh, count(store_name) as num_grocery
	from check_grocery 
	group by pri_neigh
),
crime_bus_gro as (
	select c.*, 
    IfNULL(g.num_grocery, 0) as num_grocery
	from crime_bus as c 
	left join grocery_final as g 
	on c.pri_neigh = g.pri_neigh
),
restaurants as (
	SELECT DISTINCT dba_name,longitude,latitude
	FROM `musa-509-final.justtest.restaurant_2021-11-30` 
	WHERE facility_type = 'Restaurant' and longitude is not null and latitude is not null 
),
unique as (
	select dba_name,st_geogpoint(longitude,latitude) as geom
	from restaurants
),
check_res as (
	SELECT N.pri_neigh,R.dba_name,N.the_geom as neigh_geom, R.geom as res_geom
	FROM `musa-509-final.justtest.neighborhood_2021-12-01` AS N
	CROSS JOIN unique as R
	where st_within(R.geom,N.the_geom)
),
res_final as(
	select pri_neigh, count(dba_name) as num_res
	from check_res 
	group by pri_neigh
),
nhood_details as (
	select c.*, 
    IfNULL(r.num_res, 0) as num_restaurant
	from crime_bus_gro as c 
	left join res_final as r 
	on c.pri_neigh = r.pri_neigh
),
number_table as(
	select * 
	from nhood_details
),
max_crime as(
	select num_crime as max_crime from crime_final 
	order by num_crime DESC
	limit 1),
min_crime as(
	select num_crime as min_crime from crime_final
	order by num_crime 
	limit 1),
max_res as(
	select num_res as max_res from res_final
	order by num_res desc
	limit 1),
min_res as(
	select num_res as min_res from res_final
	order by num_res
	limit 1),
max_grocery as(
	select num_grocery as max_grocery from grocery_final
	order by num_grocery desc
	limit 1),
min_grocery as(
	select num_grocery as min_grocery from grocery_final
	order by num_grocery
	limit 1),
max_busstop as(
	select num_busstop as max_busstop from busstop_final
	order by num_busstop desc
	limit 1),
min_busstop as(
	select num_busstop as min_busstop from busstop_final
	order by num_busstop
	limit 1),
add_max_crime as(select *
from number_table
left join (select * from max_crime)
on True),
add_min_crime as(select *
from add_max_crime
left join (select * from min_crime)
on True),
add_max_bus as(select *
from add_min_crime
left join (select * from max_busstop)
on True),
add_min_bus as(select *
from add_max_bus
left join (select * from min_busstop)
on True),
add_max_gro as(select *
from add_min_bus
left join (select * from max_grocery)
on True),
add_min_gro as(select *
from add_max_gro
left join (select * from min_grocery)
on True),
add_max_res as(select *
from add_min_gro
left join (select * from max_res)
on True),
add_min_res as(select *
from add_max_res
left join (select * from min_res)
on True),
norm as(
	select pri_neigh, 
	(num_crime-min_crime)/(max_crime-min_crime) as nor_crime,
	(num_busstop-min_busstop)/(max_busstop-min_busstop) as nor_busstop,
	(num_restaurant-min_res)/(max_res-min_res) as nor_res,
	(num_grocery-min_grocery)/(max_grocery-min_grocery) as nor_grocery,
	from add_min_res
)
select pri_neigh, 0.5*(1-nor_crime)+0.2*nor_busstop+0.15*nor_res+0.15*nor_grocery as index
from norm
order by index desc






