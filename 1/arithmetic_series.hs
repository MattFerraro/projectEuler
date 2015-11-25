
sumall :: Integer -> Integer -> Integer
sumall upperlimit stepsize = (i + f) * n `quot` 2
    where n = upperlimit `quot` stepsize
          f = n * stepsize
          i = stepsize

main = do
    let sumTo999 = sumall 999
    print (sumTo999 3 + sumTo999 5 - sumTo999 15)
