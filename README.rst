=============
cpyfunctional
=============
:Author: Christoforus Surjoputro <cs_sanmar@yahoo.com>
:Date: $Date: 2018-12-31 $
:Version: $Version: 0.0.1 $
:License: MIT License

.. role:: python(code)
   :language: python

.. image:: https://travis-ci.org/3mp3ri0r/cpyfunctional.svg?branch=master
    :target: https://travis-ci.org/3mp3ri0r/cpyfunctional

.. image:: https://codecov.io/gh/3mp3ri0r/cpyfunctional/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/3mp3ri0r/cpyfunctional

.. contents:: Table of content

Introduction
============

`cpyfunctional`_ is python package to help you code python in functional programming paradigm. `Series of article`_ by
Eric Elliot will tell you why you should code using functional programming.

Python version
--------------

This module work on 3.4+. Fully tested on python 3.5.2.

How to install
==============

.. code-block:: bash

    pip install cpyfunctional

How to use
==========

1. Import cpyfunctional to your project: :python:`import cpyfunctional`.
2. Choose action you want in :python:`cpyfunctional` package.

compose
-------

`compose`_ is a function to execute any callable one by one chaining from last callable to first. This function accept
any callable and execute it from last callable to the first and pass every result to next callable until the last.

.. code-block:: python

    def inc(number: int) -> int:
        return number + 1

    def square(number: int) -> int:
        return number ** 2

    cpyfunctional.compose(inc, square)(3) # 10
    cpyfunctional.compose(square, inc)(3) # 16

As you can see, it execute callable from last to first. You can also use lambda instead of creating function.

.. code-block:: python

    cpyfunctional.compose(lambda number: number + 1, lambda number: number ** 2)(3) # 10

pipe
----

This function has same functionality to `compose`_ but execute callable from first to last.

.. code-block:: python

    def inc(number: int) -> int:
        return number + 1

    def square(number: int) -> int:
        return number ** 2

    cpyfunctional.pipe(inc, square)(3) # 16
    cpyfunctional.pipe(square, inc)(3) # 10

func_curry
----------

`func_curry`_ is a function to add parameter to callable that called by `compose`_ or `pipe`_. This function accept a
callable that accept parameter and push previous value to related callable and execute it.

.. code-block:: python

    def inc(number: int) -> int:
        return number + 1

    def multiple(multiplier: int, prev_number: int) -> int:
        return prev_number * multiplier

    cpyfunctional.compose(inc, func_curry(multiple)(6))(3) # 19

This example show that now callable are able to accept any parameter not only from previous result.

How to contribute
=================

Just create an `issue`_ when you encounter any problem or contact me personally.

.. _`cpyfunctional`: https://gitlab.com/3mp3ri0r/cpyfunctional
.. _`Series of article`: https://medium.com/javascript-scene/composing-software-an-introduction-27b72500d6ea
.. _`issue`: https://gitlab.com/3mp3ri0r/cpyfunctional/issues

Note
====

I'm not an expert in functional programming, so any input about FP like any function and/or naming and/or incorrect
implementation will be very helpful.
