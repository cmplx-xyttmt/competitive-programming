defmodule FizzBuzz do
  @spec fizz_buzz(n :: integer) :: [String.t]
  def fizz_buzz(n) do
    Enum.map(1..n, &fizz_buzz_helper/1)
  end

  def fizz_buzz_helper(n) when rem(n, 15) == 0 do
    "FizzBuzz"
  end

  def fizz_buzz_helper(n) when rem(n, 3) == 0 do
    "Fizz"
  end

  def fizz_buzz_helper(n) when rem(n, 5) == 0 do
    "Buzz"
  end

  def fizz_buzz_helper(n) do
    "#{n}"
  end
end

IO.inspect(FizzBuzz.fizz_buzz(100))
