def memoize(f):
    mem = dict()
    def helper(n):
        if n in mem:
            return mem[n]
        else:
            mem[n] = f(n)
            return mem[n]

    return helper

@memoize
def fib(n):
    if n==0:
        return 0;
    elif n==1:
        return 1;
    else:
        return fib(n-2)+fib(n-1);

print(fib(100));