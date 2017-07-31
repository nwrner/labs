#!/usr/bin/perl -wT

use strict; use warnings;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use CGI;
use 5.010;

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
print "<p>Hello $name</p>";
print "</div>";
print "<p>You're $age years old???</p>";
if ($age == 69) {
	print "<p>;)</p>";
}
print "<p>Your changes have been saved.</p>";

my $filename = '/var/www/html/calendar.html'; 
open (my $fh, '>>', $filename);
#my $test = print $fh "<p>$name<p>";
#=for comment
my $table1 = "<table border='1'  bordercolor='#FFFF00' cellspacing='0' cellpadding='0' align=center>"; 
my $col1 = "<tr>";
my $row1 = "<td>$name</td>";
my $row2 = "<td>$last</td>";
my $row3 = "<td>$age</td>";
my $col2 = "</tr>"; 
my $table2 = "</table>";
print $fh $table1; 
print $fh $col1;
print $fh $row1;
print $fh $row2;
print $fh $row3;
print $fh $col2;
print $fh $table2; 
=for comment
<td valign=top><font size='2' face='Tahoma'><p id="1change">1<br></font></td>
<td valign=top><font size='2' face='Tahoma'>2<br></font></td>
<td valign=top><font size='2' face='Tahoma'>3<br></font></td>
<td valign=top><font size='2' face='Tahoma'>4<br></font></td>
<td valign=top><font size='2' face='Tahoma'>5<br></font></td>
</tr>


<tr>
<td valign=top><font size='2' face='Tahoma'>6<br></font></td>
<td valign=top><font size='2' face='Tahoma'>7<br></font></td>
<td valign=top><font size='2' face='Tahoma'>8<br></font></td>
<td valign=top><font size='2' face='Tahoma'>9<br></font></td>
<td valign=top><font size='2' face='Tahoma'>10<br></font></td>
<td valign=top><font size='2' face='Tahoma'>11<br></font></td>
<td valign=top><font size='2' face='Tahoma'>12<br></font></td>
</tr>


<tr>
<td valign=top><font size='2' face='Tahoma'>13<br></font></td>
<td valign=top><font size='2' face='Tahoma'>14<br></font></td>
<td valign=top><font size='2' face='Tahoma'>15<br></font></td>
<td valign=top><font size='2' face='Tahoma'>16<br></font></td>
<td valign=top><font size='2' face='Tahoma'>17<br></font></td>
<td valign=top><font size='2' face='Tahoma'>18<br></font></td>
<td valign=top><font size='2' face='Tahoma'>19<br></font></td>
</tr>

<tr>
<td valign=top><font size='2' face='Tahoma'>20<br></font></td>
<td valign=top><font size='2' face='Tahoma'>21<br></font></td>
<td valign=top><font size='2' face='Tahoma'>22<br></font></td>
<td valign=top><font size='2' face='Tahoma'>23<br></font></td>
<td valign=top><font size='2' face='Tahoma'>24<br></font></td>
<td valign=top><font size='2' face='Tahoma'>25<br></font></td>
<td valign=top><font size='2' face='Tahoma'>26<br></font></td>
</tr>

<tr>
<td valign=top><font size='2' face='Tahoma'>27<br></font></td>
<td valign=top><font size='2' face='Tahoma'>28<br></font></td>
<td valign=top><font size='2' face='Tahoma'>29<br></font></td>
<td valign=top><font size='2' face='Tahoma'>30<br></font></td>
<td valign=top><font size='2' face='Tahoma'>31<br></font></td>

</tr>


=cut 




print '</body>';

