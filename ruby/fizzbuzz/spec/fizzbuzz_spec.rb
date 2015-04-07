require_relative '../fizzbuzz'

describe FizzBuzz do

    before :each do
        @fizzbuzz = FizzBuzz.new
    end

    describe '#new' do
        it "returns new FizzBuzz instance" do
            expect(@fizzbuzz).to be_an_instance_of(FizzBuzz)
        end
    end

 	describe '#convert' do
        it "it returns 1 when given input 1" do
            expect(@fizzbuzz.convert(1)).to eq('1')
        end

        it "it returns 1 when given input 1" do
            expect(@fizzbuzz.convert(1)).to eq('1')
        end
	end

end
