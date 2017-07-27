#!/usr/bin/perl -wT

use strict; use warnings;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use CGI;

#my $upload_dir = "/var/www/html/upload";
my $cgi = CGI->new();
my $name = $cgi->param('firstname');
my $last = $cgi->param('lastname');
my $age = $cgi->param('age');
my $number = 12;
print $cgi->header('text/html');
#print "$number" 
print "<head>";
print "<title>Perl</title>";
#print "<link rel="stylesheet" type="text/css" href="perl.css">"; 
print "</head>";

print "<body>";
#print "<div style="float:left;">";
print "<p>Hello $name $last</p>";
print "</div>";
print "<p>You're $age years old???</p>";
print "</body>";
