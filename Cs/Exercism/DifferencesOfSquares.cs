using System;

using System.Linq;
using System.Collections.Generic;

public static class DifferenceOfSquares
{
    public static int CalculateSquareOfSum(int max)
    {
        int count = 0;
        for(int i=max; i>0; i--) count+=i;
        return Convert.ToInt32(Math.Pow(Convert.ToDouble(count), 2.0));
    }
    public static int SquareOfSum(int n)
    {
        return n * n * (n + 1) * (n + 1) / 4;
    }

    public static int CalculateSumOfSquares(int max)
    {
        int count = 0;
        for(int i=max; i>0; i--) count+=Convert.ToInt32(Math.Pow(Convert.ToDouble(i), 2.0));
        return count;
    }
    public static int SumOfSquares(int n)
    {
        return n * (n + 1) * (2 * n + 1) / 6;
    }

    public static int CalculateDifferenceOfSquares(int max)
    {
        return CalculateSquareOfSum(max) - CalculateSumOfSquares(max);
    }
}

public static class Squares
{
    public static int SquareOfSums(int max) => max
        .NaturalNumbers()
        .Sum()
        .Square();
    public static int SumOfSquares(int max) => max
        .NaturalNumbers()
        .Select(Square)
        .Sum();
    public static int DifferenceOfSquares(int max)
        => SquareOfSums(max) - SumOfSquares(max);
    static IEnumerable<int> NaturalNumbers(this int max)
        => Enumerable.Range(start: 1, count: max);
    static int Square(this int value)
        => value * value;
}