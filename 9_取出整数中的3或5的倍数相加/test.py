# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# first thought:
# def solution(number):
#     target  =[]
#     indexs = 1
#     while (3*indexs<number):
#         print (3*indexs)
#         target.append(3*indexs)
#         if 5*indexs<number:
#             target.append(5*indexs)
#         indexs = indexs +1
#     #   
#     print (target)
#     print (set(target))
   
def solution(number):
    a = [ int(i*3) for i in range(1,int(number/3)+1) if int(i*3)<number]
    b =[ int(i*5) for i in range(1,int(number/5)+1) if int(i*5)<number]
    return sum(set(a+b))

if __name__ == "__main__":
    print (solution(21))

#best solution:
#def solution(number):
    # return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)