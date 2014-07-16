Marquote
========

Marquote is a library for generating Markov chains of text quotes, either on the fly or facilitating an SQL database. 

At the moment, Marquote is at version 0.0.1, meaning that its basic functionality is there, but it still needs to be tested and documented. A parser for the Star Trek transcripts at [chakoteya.net](http://chakoteya.net) is also provided.

Marquote can save additional information about the speaker of a quote, making it possible to generate sentences not only by some sort of source, but also by character. (E.g. Hamlet or Jean-Luc Picard). When initializing the trainer, a maximum lookahead for that particular source can be configured. When generating a string, any lookahead up to that number may be used.

Marquote requires Python 3.

## Links

I got my inspiration from the very clever [King James Programming](http://kingjamesprogramming.tumblr.com/) project aswell as [Charlie Stross' take](http://www.antipope.org/charlie/blog-static/2013/12/lovebiblepl.html) on the project.



<!-- version 2: arbitrary metadata. "English quote, from 1500 to 1800, please" ;) --> 
