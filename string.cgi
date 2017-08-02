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
my $datetime = $cgi->param('datetime');
#my $date = $cgi->param('date');
my $file = "dates.txt";
#print "Hello"; 


open (my $fh, '>>', $file);
print $fh "$name\n";
print $fh "$datetime\n";
#print $fh "$date\n";
#print "$name\n";
#print "$time\n";
#print "$date\n";

close($fh);


open (FH, '<', $file);
my @master; 
while (<FH>) {
	push (@master, $_);
}

my @evens; 
#print @master[2];
#print @master[5];
#print @master[8];

my $counter=0; 
my $str; 
my $listcount= scalar @master;

while ($counter < $listcount) {
	$counter+=1; 
	if ($counter%2==0) {
		#print "$counter\n"; 
		#print "@master[$counter]<br>\n";
		push (@evens, @master[$counter]); 
		#print "============<br>\n";
	}
}

@evens = split(//,$str);
$str= "@evens";
