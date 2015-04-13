<?php

namespace Kata;

class FizzBuzz
{
    /**
     * @param  int  $number
     * @return string
     */
    public function convert($number)
    {
        $result = '';

        if ( $this->isNotDivisibleBy(3, $number) AND $this->isNotDivisibleBy(5, $number)) {
            return (string)$number;
        }

        if ($this->isDivisibleBy(3, $number)) {
            $result .= 'fizz';
        }
        if ($this->isDivisibleBy(5, $number)) {
            $result .= 'buzz';
        }

        return $result;
    }

    /**
     * @param  int  $dividend
     * @param  int  $number
     * @return boolean
     */
    public function isDivisibleBy($dividend, $number)
    {
        return $number % $dividend === 0;
    }

    /**
     * @param  int  $dividend
     * @param  int  $number
     * @return boolean
     */
    public function isNotDivisibleBy($dividend, $number)
    {
        return ! $this->isDivisibleBy($dividend, $number);
    }

    /**
     * @return string
     */
    public function display()
    {
        foreach (range(1, 100) as $number) {
            echo $this->convert($number) . PHP_EOL;
        }
    }
}
