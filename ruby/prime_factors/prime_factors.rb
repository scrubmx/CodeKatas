class PrimeCalculator

	attr_accessor :result

	def initialize()
		self.result = []
	end

	def calculate(number)

		if self.is_prime number
			return self.result << number
		end

		for x in 2..number
			if number % x == 0
				self.result << x
				return self.calculate(number/x)
			end
		end
	end

	def is_prime(number)

		return false unless number > 1

		count_divisors = 0

		for x in 2..number
			if number % x == 0
				count_divisors = count_divisors + 1
			end
		end

		count_divisors == 1
	end
end