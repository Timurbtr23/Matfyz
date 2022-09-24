using System;
using System.Linq;

namespace Programovani_2
{
    public static class MaxInArr
    {
        public static int[] ProcessInputArray(string[] inputArr)
        {
            int[] arr = Array.ConvertAll(inputArr, s => Convert.ToInt32(s));

            int[] numbers = new int[Array.IndexOf(arr, -1)];
            for (int i = 0; i < numbers.Length; i++) numbers[i] = arr[i];

            return numbers;
        }
        
        public static void FindSecondMax(int[] arr)
        {
            int max = arr.Max();
            int maxTimes = 0;
            int second_max = Int32.MinValue;
            
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] == max)
                {
                    maxTimes++;
                    if (maxTimes > 1)
                    {
                        Console.WriteLine(max);
                        return;
                    }
                }

                else if (arr[i] > second_max) second_max = arr[i];
            }
            Console.WriteLine(second_max);
        }
        
        public static void Main1()
        {
            string[] input = Console.ReadLine().Split();
            FindSecondMax(ProcessInputArray(input));
        }
    }
}