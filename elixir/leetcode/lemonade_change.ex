defmodule LemonadeChange do
  @spec lemonade_change(bills :: [integer]) :: boolean
  def lemonade_change(bills) do
    change = %{5 => 0, 10 => 0}
    {can, _} = Enum.reduce(bills, {true, change}, &update_change/2)
    can
  end

  # bill, current_change
  def update_change(bill, {can_provide, change} = _acc) do
    %{5 => fives, 10 => tens} = change
    case bill do
      5  -> {can_provide, %{change | 5 => fives + 1}}
      10 -> {can_provide and fives > 0, %{change | 5 => max(0, fives - 1), 10 => tens + 1}}
      20 ->
        {provide, fives, tens} = change_20(fives, tens)
        {can_provide and provide, %{change | 5 => fives, 10 => tens}}
    end
  end

  def change_20(fives, tens) when fives > 0 and tens > 0 do
    {true, fives - 1, tens - 1}
  end

  def change_20(fives, tens) when fives >= 3 do
    {true, fives - 3, tens}
  end

  def change_20(fives, tens) do
    {false, fives, tens}
  end
end

tests = [[5,5,5,10,20], [5,5,10,10,20]]

for test <- tests do
  IO.puts(LemonadeChange.lemonade_change(test))
end
