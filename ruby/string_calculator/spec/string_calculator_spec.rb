# Run test with: `rspec spec -c`

require 'spec_helper'

describe StringCalculator do

	before :each do
		@calculator = StringCalculator.new
	end

	describe '#new' do
		it "returns new StringCalculator object" do
			expect(@calculator).to be_an_instance_of(StringCalculator)
		end
	end

	describe '#calculate' do
		it "returns zero as a default value" do
			expect(@calculator.result).to eq(0)
		end

		it "returns the sum of two numbers or more" do
			expect(@calculator.add(1, 2)).to eq(3)
			expect(@calculator.add(1, 2, 3)).to eq(6)
		end

		it "it can subtract two numbers or more" do
			expect(@calculator.subtract(2, 1)).to eq(1)
			expect(@calculator.subtract(10, 5, 1)).to eq(4)
		end

		it "it can multiply two numbers or more" do
			expect(@calculator.multiply(2, 4)).to eq(8)
			expect(@calculator.multiply(3, 10)).to eq(30)
		end

		it "it can divide two numbers or more" do
			expect(@calculator.divide(4, 2)).to eq(2)
		end
	end

end