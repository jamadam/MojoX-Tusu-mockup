#!/usr/bin/env perl

use strict;
use warnings;
#BEGIN{$| = 1; print "Content-type: text/html\n\n"; open(STDERR, ">&STDOUT"); }
local $SIG{ALRM} = sub { die "timeout\n" }; alarm 5;

use File::Basename 'dirname';
use File::Spec;
use lib join '/', File::Spec->splitdir(dirname(__FILE__)), '..', 'extlib';
use lib join '/', File::Spec->splitdir(dirname(__FILE__)), '..', 'lib';

# Check if Mojo is installed
eval 'use Mojolicious::Commands';
die <<EOF if $@;
It looks like you don't have the Mojolicious Framework installed.
Please visit http://mojolicio.us for detailed installation instructions.

EOF

# Application
$ENV{MOJO_APP} ||= 'Mockup';
#$ENV{MOJO_MODE} ||= 'production';
$ENV{MOJO_MODE} ||= 'development';

# Start commands
Mojolicious::Commands->start;
