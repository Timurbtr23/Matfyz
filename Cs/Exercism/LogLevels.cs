using System;
namespace Exercism;

static class LogLine
{
    // "[<LEVEL>]: <MESSAGE>"

    public static string Message(string logLine)
    {
        // LogLine.Message("[ERROR]: Invalid operation" => "Invalid operation"
        var point = logLine.IndexOf(": ");
        var message = logLine.Substring(point + 2);
        return message.Trim();
    }

    public static string LogLevel(string logLine)
    {
        // "[ERROR]: Invalid operation" => "error"
        return logLine[1..logLine.IndexOf(']')].ToLower();
    }

    public static string Reformat(string logLine)
    {
        // "[INFO]: Operation completed" => "Operation completed (info)"
        return $"{Message(logLine)} ({LogLevel(logLine)})";
    }
}
