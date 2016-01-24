# Marquote Design

This file serves as reminder and overview for myself. It gives an overview over the structure and design of the marquote module.

## Purpose

The marquote library should make it easy to build Markov Chains from text files. The library offers the option to store the parsed files in a database so that the parsing has to be done only once per file. 

Additionally, parsed sentences may be tagged with a name, and Chains can then be generated using only parsed vocabulary tagged with a specific name. This permits the parsing of plays or screenplays and the generation of sentences for one specific character (e.g. Captain Picard or Hamlet).

Since there is no single or common format for those text files, a parser has to be provided for the Chain Generator. The Marquote library comes with some parsers for common formats, others can be easily substituted. Furthermore the Chain Generator needs a backend, either to keep the parsed data in memory or to connect to a database of some sort. The Marquote library is distributed with an in-memory backend and an SQL-Backend.

## Usage and Interface

### Installing

In time, Marquote will find its way to PyPI, until then, a stable version can be found on [Github](https://github.com/rixx/marquote) on the `master` branch.

### Getting started

First, include a backend and generate the controlling chain object:

    from marquote import ChainGenerator
    from marquote.Backend import Inmem

    generator = ChainGenerator(Inmem())

or:

    from marquote import ChainGenerator
    from marquote.Backend import SQLBackend

    generator = ChainGenerator(SQL(connection_string))

### Parsing things

Parsers should have a `parse` function taking the path to a file and the file's title as argument.

    from marquote.Parser import StarTrekParser

    generator.parser = StarTrekParser()
    generator.parse("/path/to/file", "Encounter at Farpoint")

### Generating sentences

Give a source, a tag or nothing at all for random sentences. You may also provide a lookahead if you don't like the default value of 3.

    generator.generate(source="Encounter at Farpoint", tag="Picard")
    generator.generate(source="Star Trek", lookahead=2)
    generator.generate()

The `generate` function returns a string and ends with a `.`. This might change or become configurable in later versions.

## Modules

### Chain

The `chain` module provides the `ChainGenerator` class that acts as controller for backends and parsers. The `ChainGenerator` constructor requires a backend to be given as parameter.

A `ChainGenerator` object provides a `parse()` and a `generate()` functions. The `parse` function throws a `NotAvailableError` if the `parser` attribute is `None`.

### Backend

The `backend` module provides several available backends, primarily `SQLBackend` and `InmemBackend`.


### Parser

The `parser` module provides a few parsers for common file formats. The provided parsers take a `test` argument (boolean). If the `test` argument is set to `True`, nothing will be written to the backend, instead everything that would have been written is printed to `STDOUT`.
