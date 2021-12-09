SELECT *,st_x(centroid) as longitude,st_y(centroid) as latitude
FROM (
    select pri_neigh,st_centroid(the_geom) as centroid
    from `musa-509-final.justtest.neighborhood_2021-12-01`)