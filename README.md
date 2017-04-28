<style>
h3, h4{
    margin, padding: 0px;
}
p{
    margin, padding: 0px;
}
</style>



<h1>Depth_Tool</h1>
<h2>Calculating mean depth of bam attached to reference bed (ex.exome).</h2>


<h3>Dependency</h3>
<p>python 2.7.x<p>
<p>-pybedtools<p>>

<hr>
<h3>Install</h3>
git clone https://github.com/yamamotomako/calc_mean_depth.git<br>
cd ./calc_mean_depth<br>
python setup.py build<br>
python setup.py install --user<br>

<br>
->depth_tool shell script will be installed into /your-home/.local/bin<br>


<hr>
<h3>Usage</h3>
depth_tool   /path-to-bam-file/sample.bam   /path-to-reference-bed/sample.bed   /path-to-output-result-file


<h4>help</h4>
depth_tool -h


<h4>success log</h4>
Console write out following log.
<br>
Starting bedtools intersect...<br>
Finished bedtools intersect...<br>
Making output file...<br>
Finished all process!<br>

