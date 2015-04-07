require_relative '../roman_numerals'

describe RomanNumerals do

    before :each do
        @roman_numerals = RomanNumerals.new
    end

    describe '#new' do
        it "returns new RomanNumerals instance" do
            expect(@roman_numerals).to be_an_instance_of(RomanNumerals)
        end
    end

    describe '#convert' do
        it "returns de roman number for input 1" do
            expect(@roman_numerals.convert(1)).to eq('I')
        end

        it "returns de roman number for input 2" do
            expect(@roman_numerals.convert(2)).to eq('II')
        end

        it "returns de roman number for input 3" do
            expect(@roman_numerals.convert(3)).to eq('III')
        end

        it "returns de roman number for input 4" do
            expect(@roman_numerals.convert(4)).to eq('IV')
        end

        it "returns de roman number for input 5" do
            expect(@roman_numerals.convert(5)).to eq('V')
        end

        it "returns de roman number for input 6" do
            expect(@roman_numerals.convert(6)).to eq('VI')
        end

        it "returns de roman number for input 8" do
            expect(@roman_numerals.convert(8)).to eq('VIII')
        end

        it "returns de roman number for input 9" do
            expect(@roman_numerals.convert(9)).to eq('IX')
        end

        it "returns de roman number for input 10" do
            expect(@roman_numerals.convert(10)).to eq('X')
        end

        it "returns de roman number for input 11" do
            expect(@roman_numerals.convert(11)).to eq('XI')
        end

        it "returns de roman number for input 15" do
            expect(@roman_numerals.convert(15)).to eq('XV')
        end

        it "returns de roman number for input 16" do
            expect(@roman_numerals.convert(16)).to eq('XVI')
        end

        it "returns de roman number for input 20" do
            expect(@roman_numerals.convert(20)).to eq('XX')
        end

        it "returns de roman number for input 21" do
            expect(@roman_numerals.convert(21)).to eq('XXI')
        end

        it "returns de roman number for input 40" do
            expect(@roman_numerals.convert(40)).to eq('XL')
        end

        it "returns de roman number for input 50" do
            expect(@roman_numerals.convert(50)).to eq('L')
        end

        it "returns de roman number for input 100" do
            expect(@roman_numerals.convert(100)).to eq('C')
        end

        it "returns de roman number for input 555" do
            expect(@roman_numerals.convert(555)).to eq('DLV')
        end

        it "returns de roman number for input 1999" do
            expect(@roman_numerals.convert(1999)).to eq('MCMXCIX')
        end

        it "returns de roman number for input 4994" do
            expect(@roman_numerals.convert(4994)).to eq('MMMMCMXCIV')
        end
    end

end