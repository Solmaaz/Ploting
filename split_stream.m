function split_stream(x) %x is bit-stream
    lx = (length(x));
    half = ceil(lx/2); %for odd number of bit-stream length
    s1 = x(1:half);
    s2 = x(half + 1 : end);
end
t1 = split_stream(e05);
%t2 = split_stream(e05).s2;
%p1 = split_stream(VarName5).s1;
%p2 = split_stream(VarName5).s2;