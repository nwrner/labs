#!/usr/bin/perl -wT
use strict; 
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use CGI;
#use File::Slurp; 
#use Path::Tiny; 
my $cgi = CGI->new();

print $cgi->header('text/html');

my $name = $cgi->param('name');
my $time = $cgi->param('time');
my $date = $cgi->param('date');
my $file = "dates.txt";
#print "Hello"; 


open (my $fh, '>>', $file);
print $fh "$name\n";
print $fh "$time\n";
print $fh "$date\n";


my $content; 
open (my $fh, '<', $file);
{
	local $/;
	$content=<$fh>;
}

close($fh); 
my @chars=split("", $content);
#print "length($name)\n";
print "@chars[length($name)+1..length($name)+4]\n";
open $fh3, "$file"; 
$first_line = <$fh3>; 
close $fh3;
#How to read only the first line of a file

#print $variable; 
#my @chars = split("", $variable);
#my $arraylen = length @chars; 

#my $filename = '/var/www/html/dates.txt'; 
#open (my $fh, '>>', $filename);

#print $fh $name;
#print $fh $time;
#print $fh $date;

#if ($arraylen eq 2) {
#	print "No collisions detected\n"; 
#}else {
#	if (@chars[12..15] == @chars[40..44]) {
#		print "COLLISION DETECTED\n";
#	}else{
#		print "No collisions detected\n"; 
#	}
#}


#print "<!DOCTYPE=html>";

#print "<head>";
#print "<link rel='stylesheet' type='text/css' href='calendar.css'>";
#print "</head>";

#print "<body>";
#print "<table border='1'  bordercolor='#FFFF00' cellspacing='0' cellpadding='0' align=center>";
#print "	<tr>";
#print 		"<td><table cellspacing='0' cellpadding='0' align=center width='100' border='1'>";
#print "	<tr>";
#print 		"<td  align=center bgcolor='#ffff00'><font size='2' face='Tahoma'> <a href='html_calendar.php?prm=8&chm=-1' rel='nofollow'><</a></font> </td>"; 
#print "		<td colspan=5 align=center bgcolor='#ffff00'><font size='2' face='Tahoma'>Aug 2017 </font> </td>";
#print "		<td  align=center bgcolor='#ffff00'><font size='2' face='Tahoma'> <a href='html_calendar.php?prm=8&chm=1' rel='nofollow'>></a>  </font></td>";
#print "	</tr>";
#print "	<tr>";
#print "		<td><font size='2' face='Tahoma'><b>Sun</b></font></td>";
#print "		<td><font size='2' face='Tahoma'><b>Mon</b></font></td>";
#print "		<td><font size='2' face='Tahoma'><b>Tue</b></font></td>";
#print "		<td><font size='2' face='Tahoma'><b>Wed</b></font></td>";
#print "		<td><font size='2' face='Tahoma'><b>Thu</b></font></td>";
#print "		<td><font size='2' face='Tahoma'><b>Fri</b></font></td>";
#print "		<td><font size='2' face='Tahoma'><b>Sat</b></font></td>";
#print "	</tr>";

#print "</table>"; 
=cut
