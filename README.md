<h3>Calculating mean depth of bam attached to reference bed (ex.exome).</h3>

<h4>Dependency</h4>
python 2.7.x
<br>
pybedtools

<h4>Install</h4>
git clone https://github.com/yamamotomako/calc_mean_depth.git
cd ./calc_mean_depth
python setup.py build
python setup.py install --user

<br>
->depth_tool shell script will be installed into /your-home/.local/bin


<h4>Usage</h4>
depth_tool /path-to-bam-file/sample.bam /path-to-reference-bed/sample.bed /path-to-output-result-file


<h5>help</h5>
depth_tool -h


<h5>success log</h5>
Console write out following log.
<br>
Starting bedtools intersect...
Finished bedtools intersect...
Making output file...
Finished all process!

