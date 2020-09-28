#!/usr/bin/env Rscript

library("data.table")
library("optparse")

parser <- OptionParser()
parser <- add_option(parser, c("-d", "--data"), type = "character", default = NULL,
    help = "Datafile to make plots with", metavar = "character")

opts = parse_args(parser)

timing_data <- fread(opts$data)

print("RD Early Stop Time")
summary(timing_data[program=='rd_es']$time)
print(sd(timing_data[program=='rd_es']$time))
print("RD Early Stop path distance")
summary(timing_data[program=='rd_es']$normalized_root_distance)
print(sd(timing_data[program=='rd_es']$normalized_root_distance))
print("RD NO Early Stop Time")
summary(timing_data[program=='rd_nes']$time)
print(sd(timing_data[program=='rd_nes']$time))
print("RD NO Early path distance")
summary(timing_data[program=='rd_nes']$normalized_root_distance)
print(sd(timing_data[program=='rd_nes']$normalized_root_distance))
print("IQ-TREE Time")
summary(timing_data[program=='iq']$time)
print(sd(timing_data[program=='iq']$time))
print("IQ-TREE path distance")
summary(timing_data[program=='iq']$normalized_root_distance)
print(sd(timing_data[program=='iq']$normalized_root_distance))
