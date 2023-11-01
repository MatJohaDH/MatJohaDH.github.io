---
layout: post
title: "Application Freewriting"
categories: [Highly specialized application, Textual, Freewriting, GUI]
date: 2023-11-01 11:56:45 +0200
---


# Application Freewriting

At the start of the fall semester 2022 I participated in a day long workshop about
academic writing, arranged by the *Finish on Time* consortium.
The workshop introduced me to **Peter Elbow**, his concept of *Freewriting*,
and the book *Writing Without Teachers*, Elbow 1973 that delves deeper in to
freewriting and different aspects of (academic) writing.
Freewriting is a simple exercise to improve ones writing:
write continuously for ten minutes without backtracking to improve a phrasing,
correct an error or pausing to find the 'right' word. The point is not to write
about any specific subject, or to stick to the same subject during the exercise.

<p style="text-align: center;">
"The only requirement is that you *never* stop"
 <br>  (Elbow 1973, p.3)
</p>

Since then I have intermittently engaged in the exercise, but I have yet to
manage to do the recommender 3+ sessions per week over a longer period.
My best run was during my summer vacation, where I would sit down and freewrite
almost every day for a few weeks. In order to force myself not to backtrack I
wrote a simple Python script that prevented me from seeing the text in
real-time by capturing all the writable characters from keystrokes and
dump them into a textfile. Once the session was over (defaulted to 10 minutes)
the script would open this textfile for a ~5 minute browse and then archive it,
i.e. move it to a subfolder named "archive". I had it set up so that it would
save the file and archive in the directory it was run -- that way I could keep
a freewrite archive for different project.
Setting it up in this way was a **mistake** for two main reasons:
1. It is very difficult and can be counterproductive to try forcing a
freewrite session to stick to a single subject. Sometimes it is like opening up
the floodgates, and trying to control it is futile. Freewriting can be
excellent moments to let the mind wander and explore new paths and rather than
trying to control it -- try to harness it.
2. Saving the texts makes the writing too permanent where they ought to be
ephemeral and explorative. Keeping a record of everything written also leaves
it open to be judged in a way that puts too much pressure on the writing.
That is not to say that all forms of record-keeping are wrong, but it must be
much more lightweight... still exploring logging methods that suit me.

![GUI of Textual-based Freewriting application ](https://github.com/MatJohaDH/MatJohaDH.github.io/blob/gh-pages/assets/images/2023-11-01_TextualFreewrite.png?raw=true)


Fast forward to today when I decided to try and write a very simple application
to that could be run on different Operative Systems -- ideally it should run on
Linux (Debian), Windows10 and MacOS and equally well on all three since these
are the different Operative Systems that I switch between.
So I figured that this would finally be an opportunity to learn how to use
[Textual](https://textual.textualize.io/) which i have
[heard](https://talkpython.fm/episodes/show/336/terminal-magic-with-rich-and-textuals)
and read about but never really had an application for until now.
All I need for the FreeWrite app is to capture keystrokes, a timer
and a way to display the written, so [Textual](https://textual.textualize.io/)
is a bit of an overkill. Still, it is a good enough excuse to start learning
a new framework.

In the past I have played with
[TKinter](https://docs.python.org/3/library/tkinter.html) and
[QT](https://www.qt.io/qt-for-python) for toy projects for
my own use, I ended up not using them since they are much more cumbersome to
set up than a simple CLI with
[Agparse](https://docs.python.org/3/library/argparse.html).
During the past two years i have written some interactive Jupyter Notebooks
using either the [GoogleColab widgets](https://github.com/MatJohaDH/LDA_playground)
or [ipywidgets](https://github.com/DigitalHistory-Lund/elam_stm_prep), but
these are mostly suitable for exploring data or methods, not for writing.
I also  wrote an [application](https://github.com/MatJohaDH/citadel) with
[Anvil](https://anvil.works/) for a
[paper](http://digitalhumanities.org/dhq/vol/17/2/000679/000679.html).
In my work I have found that Anvil is great for creating interfaces for others
where the process is continuity dependent -- such as storing intermittent
results in a database or the like and the Layout editor and documentation are
both great.
Still, all of these frameworks are too cumbersom to set up or run for the
application that I have in mind.

Luckily for me the [tutorial](https://textual.textualize.io/tutorial/) provided
by Textual is for a stopwatch app and [Textual](https://textual.textualize.io/) is by default very
proficient at capturing keystrokes, so it quickly became apparent that my idea
can be implemented without too much work.
One very important thing to note about [Textual](https://textual.textualize.io/) is its rather awesome
[Devtools](https://textual.textualize.io/guide/devtools/)-suite through which
one can observe all the different objects and calls that occur.
Throught this it was easier to figure out what how things worked and thereby
how I could bend it to my will! Unfortunately for me, I did not figure out that
this awesome console existed until I had already figured out most of what I
needed for a very basic version of the app.

Whereas the tutorial application is a list of stopwatches that can be started,
stopped, reset, spawned and removed, my variant only has the single timer,
start and stop buttons and a markdown widget for printing the output.
The stop button is disabled until 10 minutes have passed, and the start button
is disabled once used; the next freewriting session will happen on another day
and the app will not be left running in the meantime. During the 10 minute
interval all printable keystrokes are stored in a variable, *tab* and *enter*
are hardcoded to be translated into "\t" and "\n\n" respectively.
Once 10 minutes have passed, the stop button is enabled and once pressed the
timer stops and the text (or string of incomprehnsive characters) are shown in
the markdown widgets. Since both widgets (timer and text) are placed within a
scrollable container, one can always access all the text. Once the app is closed
the text is gone. In summary the prototype works as intended, at least on this
machine -- testing will  continue on MacOS, Win10 and my other Linux machines.
The GUI is surprisingly pretty for how little time I put into it, and much
prettier than my needs necessitate. I will keep tinkering with it as I use it,
and I already have several ideas of how it could be improved -- but this will
have to do for today.

![GUI of Textual-based Freewriting application ](/assets/images/2023-11-01_TextualFreewrite.png)
