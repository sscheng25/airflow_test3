SELECT pri_neigh,neigh.xmin as x_min,neigh.ymin as y_min, neigh.xmax as x_max,neigh.ymax as y_max
FROM (SELECT pri_neigh,st_boundingbox(the_geom) as neigh
FROM `musa-509-final.justtest.neighborhood_2021-12-01`)