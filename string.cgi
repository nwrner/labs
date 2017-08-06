#!/usr/bin/perl -wT

use strict; 
use CGI::Carp qw (fatalsToBrowser);
use File::Basename;
use CGI;

my $cgi = CGI->new();

print $cgi->header('text/html');

##### PRINTS THE USERS INPUT TO THE DATES.TXT FILE #####x
my $datetime = $cgi->param('datetime');			#	
my $name = $cgi->param('name');				#
my $file = "dates.txt";					#
							#
							#
open (my $fh, '>>', $file);				#
my $badwords ="/:"; 					#
$datetime =~ s/[$badwords]//g;				#
$datetime =~ tr/ //ds; 					#
print $fh "$name\n";					#
print $fh "$datetime\n";				#
							#
close($fh);						#
########################################################x

##### PUTS EVERYTHING FROM THE DATES.TXT FILE###########x 
##### INTO THE @master ARRAY ############################ 
open (FH, '<', $file);					#
my @master; 						#
							#
while (<FH>) {						#
	push (@master, $_);				#
}							#
							#
########################################################x

#### TAKES EVERY SECOND ITEM IN THE DATA.TXT ###########x
#### FILE AND PUTS IT IN THE @evens ARRAY ###############
my @evens; 						#
my $counter=1; 						#
my $str; 						#
my $listcount= scalar @master;				#
							#
while ($counter < $listcount) {				#
	push (@evens, @master[$counter]);		#
	$counter+=2; 					#
	#if ($counter%2==0) {				#
	#	push (@evens, @master[$counter]); 	#
	#}						#
}							#
########################################################x

#### DEFINES /var/www/html/calendar.html as ############x
#### $calendarloc and opens it  #########################
my $calendarloc="/var/www/html/calendar.html"; 		#
open (my $f, '>', $calendarloc);			#
########################################################x

my $str = "@evens"; 
my $str1 = "@master";
my $pos1 = 8;
my $pos2 = 3; 
my $datepos1= 0;
my $datepos2=4;
my $colpos1=0;
my $colpos2=8;
my $evenscount = scalar @evens; 
my $breaker =0;
my $jan1init;
my $jan1; 
my $jan2;
my $jan3;
my $jan4;
my @hours;
my @sorted; 
my $hoursfincount=0;
my $breaker2=0;
print $f "<table border='1'  bordercolor='#FFFF00' cellspacing='0' cellpadding='0' align=center>";
print $f "<tr>";
while ($breaker!=$listcount) {	
	my $date = substr $str, $datepos1, $datepos2; 
	my $char = substr $str, $pos1, $pos2;  
	print "$breaker: Requester: @master[$breaker]<br>\n"; 	
	print $f "<td valign=top><font size='2' face='Tahoma'>Name:@master[$breaker]";
	print $f "Index:$char<br>";	
	my $colchar= substr $str, $colpos1, $colpos2; 	
	if ($date=='0901') { 
		#$jan1.="$colchar "; 
		push (@hours, $char); 
		@sorted = sort { $a <=> $b } @hours;
		#$jan1.="@sorted[$hoursfincount]<br>";  
		$jan1.="$char<br>"; 
		$jan1.="@master[$breaker]<br>"; 
	}
	my $hourslist=scalar @evens; 
	$breaker+=1;
	print "$breaker Date: @master[$breaker]<br>\n";
	print $f "Date: @master[$breaker]"; 	
	$breaker+=1; 
	$pos1+=13;
	$colpos1+=13;	
	$datepos1+=13;
}

my $listcount2= scalar @sorted; 


print $f "</tr>"; 
print $f "</table>"; 

print $f "<table border='1'  bordercolor='#FFFF00' cellspacing='0' cellpadding='0' align=center>";
print $f "<tr>";
print $f "<td> </td>";
print $f "<td> </td>";
print $f "<td valign=top><font size='2' face='Tahoma'>$jan1<br></font></td>";
print $f "<td valign=top><font size='2' face='Tahoma'>$jan2<br></font></td>";
print $f "<td valign=top><font size='2' face='Tahoma'>$jan3<br></font></td>";
print $f "<td valign=top><font size='2' face='Tahoma'>$jan4<br></font></td>";
print $f "</tr>";
print $f "</table>"; 
#print $f @hoursfin; 
#
while ($breaker2!=$listcount2) {
        print $f @sorted[$breaker2];
        #$jan2.=$breaker2; 
        $breaker2+=1;
}
        
