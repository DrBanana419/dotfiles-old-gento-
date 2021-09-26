def eff_fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = eff_fib(n-1, d) + eff_fib(n-2, d)
        d[n] = ans
        return ans

basecase = {0:1, 1:1}
print(eff_fib(100, basecase))
