# Word games 2
<p>In this problem set you will write a program that will play the 6.00 word game all by itself. It is an
extension to Problem Set 5, in which you wrote a word game that a human could play.</p>

<h3>Problem #1: How long?</h3>
<p>You have a friend who consistently beats you when playing the word game because she takes forever
to play. You decide to change the rules of the game to fix her wagon. Points are awarded as before,
except the points awarded for a word are divided by the amount of time taken to find the word. Points
for a word should be displayed to two decimal places.</p>

<h3>Problem #2: Time Limit</h3>
<p>You still find it boring to watch your friend think for long periods of time while playing the 6.00 word
game. You decide to add a "chess clock" to the game. This limits the total amount of time, in seconds,
that a player can spend to play a hand.</p>

<h3>Problem #3: Computer Player</h3>
<p>You've spent so much time working on 6.00 that, unfortunately, you don't actually have any friends
left to play the word game with you. So, nerd that you have become, you decide to implement support
for computer players.</p>

<h3>Problem #4: Even Faster Computer Player</h3>
<p>Now implement a faster computer player called pick_best_word_faster(hand, rearrange_dict). It
should be based on the following approach described below. (This is a good example of what
pseudocode should look like).</p>  
First, do this pre-processing before the game begins:  
<p><code> Let d = {} <br />
<p>For every word w in the word list:  
<p>Let d[(string containing the letters of w in sorted order)] = w</code></p>
<p>After the above pre-processing step, you have a dict where, for any set of letters, you can determine if 
there is some acceptable word that is a rearrangement of those letters. You should put the
pre-processing code into a separate function called get_word_rearrangements, analagous to
get_words_to_points.<br/>
As in Problem 3, decide where this function should be called based on how many times it needs to run.
Store the returned value in a global variable rearrange_dict.</p>
<p>Now, given a hand, here's how to use that dict to find a word that can be made from that hand:<br/>
To find some word that can be made out of the letters in HAND:
 <p><code>For each subset S of the letters of HAND:
 <p>Let w = (string containing the letters of S in sorted order)
<p>If w in d: return d[w]</code>
<p>N.B.: These are actually sub-multisets, not subsets. In a formal definition, sets cannot contain
repeated elements, while multisets, like groups of letters within a hand, can. </p>

<h3>Problem #5: Algorithm Analysis</h3>
Characterize the time complexity of your implementation (in terms of the size of word_list a
