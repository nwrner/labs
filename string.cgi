#!/usr/bin/perl -wT

use strict; 
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use CGI;
my $cgi = CGI->new();

print $cgi->header('text/html');

my $datetime = $cgi->param('datetime');
my $name = $cgi->param('name');
my $file = "dates.txt";


open (my $fh, '>>', $file);
#print "DATE BEFORE CHANGE: $datetime\n<br>";
my $badwords ="/:"; 
$datetime =~ s/[$badwords]//g;
$datetime =~ tr/ //ds; 
#print "DATE AFTER CHANGE: $datetime\n<br>"; 
print $fh "$name\n";
print $fh "$datetime\n";

close($fh);


open (FH, '<', $file);
my @master; 

while (<FH>) {
	push (@master, $_);
}


#print "MASTER LIST (Everything in the dates file): <br> @master <br>"; 
my @evens; 

my $counter=1; 
my $str; 
my $listcount= scalar @master;

while ($counter < $listcount) {
	push (@evens, @master[$counter]);
	$counter+=2; 
	#if ($counter%2==0) {
	#	push (@evens, @master[$counter]); 
	#}
}

#print "EVENS LIST (Every second item in the master list): <br> @evens <br>";
#print "The third item?: <br> @evens[0]<br>"; 

my $calendarloc="/var/www/html/calendar.html"; 
open (my $f, '>', $calendarloc);

my $str = "@evens"; 
my $str1 = "@master";
my $pos1 = 0;
my $pos2 = 11; 
print "String $str<br>\n";
#print "Fragment: $char<br>\n";
my $evenscount = scalar @evens; 
my $breaker =0;
print $f "<table border='1'  bordercolor='#FFFF00' cellspacing='0' cellpadding='0' align=center>";
print $f "<tr>";
while ($breaker!=$listcount) {	
	my $char = substr $str, $pos1, $pos2;  
	print "$breaker: Requester: @master[$breaker]<br>\n"; 	
	print $f "<td valign=top><font size='2' face='Tahoma'>Name:@master[$breaker]";
	print $f "Index:$char<br>";
	$breaker+=1;
	print "$breaker Date: @master[$breaker]<br>\n";
	print $f "Date: @master[$breaker]<br></font></td>"; 	
	#print $f "<br>$char";
	$breaker+=1;
	$pos1+=13;
	#print $f @evens;
	#print $f "<br";
	#print $f "==========================="; 
}

print $f "</tr>"; 
print $f "</table>"; 
#print $f @evens; 
#print $f "<br>@master";
#$pos1 = 0;
#$pos2 = 11;
#my $char = substr $str, $pos1, $pos2;

#print $f "<tr>";
#print "CHARACTERS: $char"; 

=pod
while ($breaker!=$listcount) {	
	print "$breaker: Date: @master[$breaker]<br>\n"; 
	$breaker+=1;
}

print $f "</tr>"; 
#print @evens;
=cut
=pod
print $f "<tr>";
print $f "<td> </td>";
print $f "<td> </td>";
print $f "<td valign=top><font size='2' face='Tahoma'>2<br></font></td>";
print $f "<td valign=top><font size='2' face='Tahoma'>3<br></font></td>";
print $f "<td valign=top><font size='2' face='Tahoma'>4<br></font></td>";
print $f "<td valign=top><font size='2' face='Tahoma'>5<br></font></td>";
print $f "</tr>";
print $f "</table>"; 
#while ($counter2<$evenscount) {
#	my $char = substr $str, $pos1, $pos2;
#	print "Dates Requested: $counter2: $char<br>\n";
#	print "Requester: @evens[$counter2-2]<br>\n";
#	$pos1=$pos1+13;
#	$counter2+=1;  
##}
=cut
