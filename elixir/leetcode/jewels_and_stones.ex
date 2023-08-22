# https://leetcode.com/problems/jewels-and-stones/
defmodule JewelsAndStones do
  @spec num_jewels_in_stones(jewels :: String.t, stones :: String.t) :: integer
  def num_jewels_in_stones(jewels, stones) do
    set = jewels |> String.graphemes |> MapSet.new
    stones
        |> String.graphemes
        |> Enum.count(fn(stone) -> MapSet.member?(set, stone) end)
  end
end

tests = [%{jewels: "aA", stones: "aAAbbbb"}, %{jewels: "z", stones: "ZZ"}]
for test <- tests do
  jewels = test[:jewels]
  stones = test[:stones]
  IO.puts(JewelsAndStones.num_jewels_in_stones(jewels, stones))
end
