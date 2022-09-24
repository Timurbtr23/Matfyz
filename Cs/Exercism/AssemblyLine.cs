using System;

static class AssemblyLine
{
    private const int _rate = 221;
    
    public static double SuccessRate(int speed)
    {
        if (speed == 0) return 0;
        else if (1 <= speed && speed <= 4) return 1.0;
        else if (5 <= speed && speed <= 8) return 0.9;
        else if (speed == 9) return 0.8;
        else if (speed == 10) return 0.77;
        else return 0;
    }
    
    public static double SuccessRate2(int speed) => speed switch
    {
        0 => 0,
        <= 4 => 1.0,
        <= 8 => 0.9,
        <= 9 => 0.8,
        _ => 0.77,
    };
    
    public static double ProductionRatePerHour(int speed)
    {
        return speed * _rate * AssemblyLine.SuccessRate(speed);
    }

    public static int WorkingItemsPerMinute(int speed)
    {
        return (int)(AssemblyLine.ProductionRatePerHour(speed) / 60);
    }
}