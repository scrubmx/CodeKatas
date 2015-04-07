class RomanNumerals

	@@glyphs = {
		1000 => 'M',
		900 => 'CM',
		500 => 'D',
		400 => 'CD',
		100 => 'C',
		90 => 'XC',
		50 => 'L',
		40 => 'XL',
		10 => 'X',
		9 => 'IX',
		5 => 'V',
		4 => 'IV',
		1 => 'I',
	}

	def convert(number)
		result = ''
		@@glyphs.each do |key, glyph|
			while number >= key
				result << glyph
				number -= key
			end
		end

		result
	end

	def display()
		for x in 1..101
			puts self.convert(x)
		end
	end

end
