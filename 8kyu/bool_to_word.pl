# Complete the method that takes a boolean value and return a "Yes" string for true, or
#  a "No" string for false.

sub bool_to_word {
    my ($bool) = @_;
    if ($bool) {
        return('Yes');
    }
    else
    {
        return('No');
    }
}

1; 