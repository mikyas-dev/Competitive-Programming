class Solution:
	def distinctPrimeFactors(self, nums: List[int]) -> int:

		result = set()

		for i in range (len(nums)) :

			square_root = int(math.sqrt(nums[i]))

			for prime_num in range(2, square_root + 1) :

				if (nums[i] % prime_num == 0) :

					result.add(prime_num)

					while (nums[i] % prime_num == 0) :
						nums[i] = nums[i] // prime_num

			if (nums[i] >= 2) :
				result.add(nums[i])

		return len(result)
		