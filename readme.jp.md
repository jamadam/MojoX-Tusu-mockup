MojoX-Tusu-mockup 0.34 beta
---------------

## DESCRIPTION

This is a web site mockup which was generated with [MojoX::Tusu].

    $ mojo generate tusu_app Mockup

You can construct MojoX::Tusu application by addin files into public_html
directory in hierarchical structure and run the application with following
command.

    $ ./script/mockup daemon
    Server available at http://127.0.0.1:3000.

On production server, you can run the app with following command.

    $ hypnotoad ./script/mockup

Or, you can deploy the app with CGI. The CGI script is already in your
public_html. Make sure the CGI script's permission is executable.

[MojoX::Tusu]:https://github.com/jamadam/MojoX-Tusu

Copyright (c) 2011 [jamadam]
[jamadam]: http://blog2.jamadam.com/

Dual licensed under the MIT and GPL licenses:

- [http://www.opensource.org/licenses/mit-license.php]
- [http://www.gnu.org/licenses/gpl.html]
[http://www.opensource.org/licenses/mit-license.php]: http://www.opensource.org/licenses/mit-license.php
[http://www.gnu.org/licenses/gpl.html]:http://www.gnu.org/licenses/gpl.html
