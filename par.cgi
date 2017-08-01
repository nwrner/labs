#!/usr/bin/perl

open my $fh1, '<', 'dates.txt';
chomp(my @lines = <$fh1>);
close $handle;
my @dates; 
$counter=2;
$arraylen=scalar @lines; 

#print "@lines\n";
while ($counter < @lines) {
	push (@dates, "@lines[$counter]");
	$counter+=3; 
}


my $s1 = @dates[0]; 
my $s2 = @dates[1]; 

print strncmpi 
#print "@lines[0]\n";  
