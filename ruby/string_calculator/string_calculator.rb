class StringCalculator

	attr_reader :result

	def initialize()
		@result = 0
	end

	def add(*numbers)
		numbers.inject(:+)
	end

	def subtract(*numbers)
		return numbers.inject(:-)
	end

	def multiply(*numbers)
		return numbers.inject(:*)
	end

end