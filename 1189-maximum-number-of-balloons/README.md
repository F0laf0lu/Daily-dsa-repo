<h2><a href="https://leetcode.com/problems/maximum-number-of-balloons">1297. Maximum Number of Balloons</a></h2><h3>Easy</h3><hr><p>Given a string <code>text</code>, you want to use the characters of <code>text</code> to form as many instances of the word <strong>&quot;balloon&quot;</strong> as possible.</p>

<p>You can use each character in <code>text</code> <strong>at most once</strong>. Return the maximum number of instances that can be formed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;nlaebolko&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;loonbalxballpoon&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;leetcode&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>text</code> consists of lower case English letters only.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/" target="_blank"> 2287: Rearrange Characters to Make Target String.</a></p>


<h2>Key Insight</h2>
<p>You need to get the char that limits the forming of instances of 'balloon' after counter the frequencies of the required letters in the text

For example:
After count the frequencies of the required char to formed the word balloon from the give text you get 
{'b':7, 'a':7, 'l':7, 'o':7, 'n':7}

The min required number of characters to form ballon is 
b - 1, a - 1, l - 2, o- 2, n-1

Then, from your frequency count you check if the letters are enough to form the word
l : 7
but we need at least 2 L characters to form a ballon
so 7 // 2 = 3 (integer division)
so l is the limiting factor here. Means we can only form 3 ballons from this text



</p>
