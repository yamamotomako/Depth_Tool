#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import pybedtools
from collections import OrderedDict



def calc_mean_depth(bamfile, baitfile, outfile):

    print "Starting bedtools intersect..."

    bam_p = pybedtools.BedTool(bamfile)
    bed_p = pybedtools.BedTool(baitfile)
    bam2ref = bam_p.intersect(bed_p, bed=True, wo=True).saveas(outfile+".ints")

    print "Finished bedtools intersect..."


    ref_dict = OrderedDict()

    with open(outfile+".ints", "r") as f:
        for ff in f:
            line = ff.split("\t")
            chrm = line[0]
            match_start = line[1]
            match_end = line[2]
            ref_start = line[13]
            ref_end = line[14]
            match_base = int(line[len(line)-1])
            other_info = "\t".join(line[15:])
            key = ref_start + "-" + ref_end

            if not ref_dict.has_key(key):
                depth = match_base
                ref_dict[key] = [chrm, match_start, match_end, ref_start, ref_end, depth, other_info]
            else:
                depth = ref_dict[key][5] + match_base
                ref_dict[key][5] = depth



    print "Making output file..."

    g = open(outfile, "w")

    #header
    header_str = "\t".join(["chromesome:start-end","mean-depth"]) + "\n"
    g.write(header_str)

    for k, v in ref_dict.items():
        mean_depth = int(v[5]) / (int(v[4]) - int(v[3]))
        g.write("chr"+v[0]+":"+v[3]+"-"+v[4] + "\t" + str(mean_depth) + "\n")

    g.close()

    print "Finished all process!"



