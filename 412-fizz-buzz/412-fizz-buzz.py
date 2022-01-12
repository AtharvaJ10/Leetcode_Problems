class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list_of_output = []
        
        for i in range(1, n+1):
            
            if i % 3 == 0 and i % 5 == 0:
                # i is multiple of both 3 and 5
                list_of_output.append('FizzBuzz')
            
            elif i % 3 == 0:
                # i is multiple of 3 only
                list_of_output.append('Fizz')
            
            elif i % 5 == 0:
                # i is mupltiple of 5 only
                list_of_output.append('Buzz')
            
            else:
                # i is neither multiple of 3 nor multiple of 5.
                list_of_output.append( str(i) )
                
        
        return list_of_output