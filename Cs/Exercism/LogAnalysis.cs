using System;
using System.Text.RegularExpressions;


namespace Exercism
{
    public static class LogAnalysis 
    {
        // define the 'SubstringAfter()' extension method on the `string` type
        public static string SubstringAfter(this string str, string obj)
        {
            return str.Split(obj).Last();
        }

        // define the 'SubstringBetween()' extension method on the `string` type
        public static string SubstringBetween(this string str, string start, string end)
        {
            return str[(str.IndexOf(start)+start.Length)..str.IndexOf(end)];
        }
    
        // define the 'Message()' extension method on the `string` type
        public static string Message(this string str)
        {
            return str.SubstringAfter(": ");
        }

        // define the 'LogLevel()' extension method on the `string` type
        public static string LogLevel(this string str)
        {
            return str.SubstringBetween("[", "]");
        }
        
        public static void Main()
        {
            string log = "[INFO]: File Deleted.";
            Console.WriteLine(log.SubstringAfter(": "));

            
        }
    }
}