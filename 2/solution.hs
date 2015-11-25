fib :: (Integral a) => a -> a
fib 0 = 1
fib 1 = 2
fib n = fib (n - 1) + fib (n - 2)



main = do
	let allNums = [0..4]

	print map fib allNums
