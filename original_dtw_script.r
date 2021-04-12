while (i < length(filenames_new)){
  path1 = file.path(dirc, filenames_new[i])
  path2 = file.path(dirc, filenames_new[i+1])
  d1 = read.csv(path1, header = TRUE, na.strings = c('',' ', 'NA'))
  d2 = read.csv(path2, header = TRUE, na.strings = c('',' ', 'NA'))
  p1 = d1[,397:413]
  p2 = d2[,397:413]
  audist = dist(p1, p2, method = 'euclidean')
  dtw_out = dtw(audist, keep = TRUE, open.begin = TRUE, open.end = TRUE, step = asymmetric)
  j = (i+1)/2
  ave_cost = mean(dtw_out$costMatrix)
  min_dist = dtw_out$distance
  nor_dist = dtw_out$normalizedDistance
  data = c(filenames_new[i], filenames_new[i+1], i, i+1, ave_cost, min_dist, nor_dist )
  dtw_data_BART[j,] = data
  i = i+2
}
