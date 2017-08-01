#!/usr/bin/perl

open my $fh1, '<', 'dates.txt';
chomp(my @lines = <$fh1>);
close $handle;
#my $bullshit=$lines[1]; 
#my $horseshit=$lines[4];
my @august;
my @september;
my @october; 
my @november; 
my @dates; 
 
$counter=2;
$arraylen=scalar @lines; 
$arraylen=$arraylen/3;
#print "@lines[1..3]\n";
#print $arraylen;
#print @lines;


#print "@lines\n";

if ($arraylen==1) {
	print "Appointment accepted.\n";
}

if (@lines[1]!=@lines[4]) {
	print "Appointment accepted\n";
}

