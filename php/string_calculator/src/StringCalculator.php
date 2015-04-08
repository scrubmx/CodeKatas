<?php

namespace Kata;

class StringCalculator
{
    private $delimiters_regexp = "/,|\\n/";

    /**
     * @param string $string
     */
    public function add($string)
    {
        if ($string == '') return 0;

        $numbers_array = $this->string_to_array($string);

        return $this->array_add($numbers_array);
    }

    /**
     * @param  string $string
     * @return array
     */
    private function string_to_array($string)
    {
        return preg_split("/,|\\n/", $string);
    }

    /**
     * @param  array $numbers
     * @return integer
     */
    public function array_add(array $numbers)
    {
        // throws exception if it finds a negative number
        $this->validate_numbers($numbers);

        // removes numbers grater than 1000
        $this->sanitize_array($numbers);

        return array_sum($numbers);
    }

    /**
     * @param  array $numbers
     * @return array
     */
    protected function sanitize_array(array &$numbers)
    {
        foreach ($numbers as $index => $n) {
            if ( (int)$n >= 1000 ) unset($numbers[ $index ]);
        }
    }

    /**
     * @param  array $numbers
     *
     * @throws \Kata\InvalidArgumentException;
     *
     * @return void
     */
    protected function validate_numbers(array $numbers)
    {
        foreach ($numbers as $number) {
            $this->validate_number($number);
        }
    }

    /**
     * @param  string|integer $number
     *
     * @throws \Kata\InvalidArgumentException;
     *
     * @return void
     */
    protected function validate_number($number)
    {
        if ( (int)$number < 0 ) {
            throw new InvalidArgumentException("Invalid number provided: $number");
        }
    }
}
