#!/bin/bash

set -euo pipefail

dir=PROVIDED_BY_SCIENTIST

lftp -u aexpress,aexpress1 ftp-private-2.ebi.ac.uk -e "set ftp:ssl-allow no; cd $dir; mput */*.fastq.gz; bye"
