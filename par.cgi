#!/usr/bin/perl
use strict; 
my @lines; 
my $filename1 = '/var/www/html/dates.txt';
open (my $fh2, '<', $filename1);

chomp(@lines=<$fh2>);
my @lines;
my @slice = @lines[6];
print @slice;
print @lines;
