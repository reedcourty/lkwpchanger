===========
lkwpchanger
===========

What's this?
------------

Wallpaper changer mostly Gabi's WinXP

How can I install it?
---------------------

What are you talking about? It's just one file, copy it to an appropriate
place. :)

How can I use it?
-----------------
Just type in the console::

    $ python lkwpchanger.py -h
    
You should see the following lines::

    $ LK Wallpaper Changer mostly for Gabi's WinXP
    $ usage: lkwpchanger.py [-h] [--pictures PICTURES] [--time ELAPSED_TIME]
    $                     [--debug] [--version]
    $
    $ optional arguments:
    $   -h, --help            show this help message and exit
    $   --pictures PICTURES, -p PICTURES
    $                         The path of the pictures directory
    $   --time ELAPSED_TIME, -t ELAPSED_TIME
    $                         The elapsed time between two background changes
    $   --debug, -d           Set debug mode on
    $   --version, -v         show program's version number and exit

Here is an example::

    $ python lkwpchanger.py -p F:\Pictures -t 180

So the application choose a picture from your "Pictures" directory on drive F, 
and set it as background every 3 minutes.

Where the hell did this name come from?
---------------------------------------

This information is top secret for the time being. ;)
