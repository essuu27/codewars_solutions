# Write a function that accepts an integer n and a string s and returns
# string s n times  
sub repeat_str {
    my ($num, $str) = @_;
    my $outstr = $str x $num;
    return ($outstr);
}


