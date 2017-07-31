#!/usr/bin/perl -wT

#Allows the recieving of HTML Form data
use strict; use warnings;
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use CGI;
my $cgi = CGI->new();



#Defines what the data recieved from the HTML form data will be called
my $name = $cgi->param('name');
my $time = $cgi->param('time');
my $date = $cgi->param('date');

#Defines the header of the HTML return page 
print $cgi->header('text/html');
#Prints out the head information of the return page
print "<head>";
print "<title>Perl</title>";
print "</head>";
print "<body>";


#Opens both calendar.html for modification of the visual calendar
#as well as dates.txt for long term storage of reservation data.
my $filename = '/var/www/html/calendar.html'; 
my $filename1 = '/var/www/html/dates.txt';
open (my $fh, '>', $filename);
open (my $fh1, '>>', $filename1); 

#Writes the data that the user gives to the dates.txt file. 
print $fh1 "NAME: $name"; 
print $fh1 "TIME: $time";
print $fh1 "DATE: $date\n";

#Closes the $fh1 file so there are no conflicts with the below code. 
close $fh1; 

#Opens $fh1 with a different name to avoid conflicts with the above code. 
open (my $fh2, '<', $filename1);

#Defines teh @lines array. 
my @lines;

#Puts everything form the $fh1 file into the @lines array. 
chomp(@lines= <$fh2>);

#First defines the 'i' viaraible used as a counter. 
#Next, defines teh @new array, and parses through it, using 'i' as a counter
#to only write does every third entry in the array (to find the dates the user entered). 
my $i; 
my @new = grep {not ++$i % 3 } @lines; 
print @new; 
my @split = split("", @new[0]);
print "String $split[1..7]"; 

##############################################
#Printing the table to the calendar.html page.
my $tablea = "<table cellspacing='0' cellpadding='0' align=center width='100' border='1'>";
my $rowa = "<tr>";
my $cola = "<td valign=top><font size='2' face='Tahoma'><p>1 $name<br></font></td>";
my $colb = "<td valign=top><font size='2' face='Tahoma'>2<br></font></td>";
my $colc = "<td valign=top><font size='2' face='Tahoma'>3<br></font></td>";
my $cold = "<td valign=top><font size='2' face='Tahoma'>4<br></font></td>";
my $cole = "<td valign=top><font size='2' face='Tahoma'>5<br></font></td>";
my $rowb = "</tr>";
my $tableb = "</table>";

print $fh $tablea;
print $fh $rowa; 
print $fh $cola;
print $fh $colb;
print $fh $colc;
print $fh $cold;
print $fh $cole; 
print $fh $rowb;  
print $fh $tableb; 
################################################


########################################################
###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###
###                     PURGATORY 	             ###
###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###
########################################################
#▒▒▒░░░░░░░░░░▄▐░░░░ |Turn back now or be forever 
#▒░░░░░░▄▄▄░░▄██▄░░░ |trapped in purgatory with
#░░░░░░▐▀█▀▌░░░░▀█▄░ |this long unused code!!!
#░░░░░░▐█▄█▌░░░░░░▀█▄|_________________________
#░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀/
#░░░░░▄▄▄██▀▀▀▀░░░░░
#░░░░█▀▄▄▄█░▀▀░░░░░░
#░░░░▌░▄▄▄▐▌▀▀▀░░░░░
#░▄░▐░░░▄▄░█░▀▀░░░░░
#░▀█▌░░░▄░▀█▀░▀░░░░░
#░░░░░░░░▄▄▐▌▄▄░░░░░
#░░░░░░░░▀███▀█░▄░░░
#░░░░░░░▐▌▀▄▀▄▀▐▄░░░
#░░░░░░░▐▀░░░░░░▐▌░░
#░░░░░░░█░░░░░░░░█░░
#░░░░░░▐▌░░░░░░░░░█░ 

#=for comment
#my $table1 = "<table border='5'  bordercolor='blue' cellspacing='0' cellpadding='0' align=center>"; 
#my $col1 = "<tr>";
#my $row1 = "<td>$name</td>";
#my $row2 = "<td>$last</td>";
#my $row3 = "<td>$age</td>";
#my $col2 = "</tr>"; 
#my $table2 = "</table>";
#print $fh $table1; 
#print $fh $col1;
#print $fh $row1;
#print $fh $row2;
#print $fh $row3;
#print $fh $col2;
#print $fh $table2; 
#=for comment

#my $string = "Hello, how are you?";
#my @chars = split("", $string);
#print "First characters: $chars[0]\n"; 

#<tr>
#<td valign=top><font size='2' face='Tahoma'>6<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>7<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>8<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>9<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>10<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>11<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>12<br></font></td>
#</tr>


#<tr>
#<td valign=top><font size='2' face='Tahoma'>13<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>14<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>15<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>16<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>17<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>18<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>19<br></font></td>
#</tr>

#<tr>
#<td valign=top><font size='2' face='Tahoma'>20<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>21<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>22<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>23<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>24<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>25<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>26<br></font></td>
#</tr>

#<tr>
#<td valign=top><font size='2' face='Tahoma'>27<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>28<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>29<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>30<br></font></td>
#<td valign=top><font size='2' face='Tahoma'>31<br></font></td>

#</tr>


#=cut 




print '</body>';
close $fh;
close $fh1; 
