
<h1>Depth Tool</h1>
<h2>Calculating mean depth of bam attached to reference bed (ex.exome).</h2>


<h3>Dependency</h3>
python 2.7.x
-pybedtools

<hr>
<h3>Install</h3>
<pre><code>
git clone https://github.com/yamamotomako/calc_mean_depth.git<br>
cd ./calc_mean_depth<br>
python setup.py build<br>
python setup.py install --user<br>
</code></pre>

<br>
->depth_tool shell script will be installed into /your-home/.local/bin<br>


<hr>
<h3>Usage</h3>
<pre><code>
depth_tool   /path-to-bam-file/sample.bam   /path-to-reference-bed/sample.bed   /path-to-output-result-file
</code></pre>


<h4>help</h4>
<pre><code>
depth_tool -h
</code></pre>


<h4>success log</h4>
Console write out following log.<br>
<pre><code>
Starting bedtools intersect...<br>
Finished bedtools intersect...<br>
Making output file...<br>
Finished all process!<br>
</code></pre>


