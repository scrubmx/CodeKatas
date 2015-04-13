<?php

// make sure to `[sudo] composer update`
// run tests with vendor/bin/phpspec run

namespace spec\Kata;

use PhpSpec\ObjectBehavior;
use Kata\InvalidArgumentException;

class FizzBuzzSpec extends ObjectBehavior
{
    public function it_is_initializable()
    {
        $this->shouldHaveType('Kata\FizzBuzz');
    }

    function it_returns_1_for_input_1()
    {
        $this->convert(1)->shouldEqual('1');
    }

    function it_returns_2_for_input_2()
    {
        $this->convert(2)->shouldEqual('2');
    }

    function it_returns_fizz_for_input_3()
    {
        $this->convert(3)->shouldEqual('fizz');
    }

    function it_returns_4_for_input_4()
    {
        $this->convert(4)->shouldEqual('4');
    }

    function it_returns_buzz_for_input_5()
    {
        $this->convert(5)->shouldEqual('buzz');
    }

    function it_returns_fizzbuzz_for_input_15()
    {
        $this->convert(15)->shouldEqual('fizzbuzz');
    }
}
