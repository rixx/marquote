Marquote
========

Marquote is a library for generating Markov chains of text quotes, either on the fly or facilitating an SQL database. 

Marquote can save additional information about the speaker of a quote, making it possible to generate sentences not only by some sort of source, but also by character. (E.g. Hamlet or Jean-Luc Picard). When initializing the trainer, a maximum lookahead for that particular source can be configured. When generating a string, any lookahead up to that number may be used.

Marquote requires Python 3.

<!-- version 2: arbitrary metadata. "English quote, from 1500 to 1800, please" ;) --> 
