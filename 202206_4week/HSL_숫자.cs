using System;
using System.Collections.Generic;

public class Solution {
    List<Number> numList = new List<Number>() {
    new Number(0, "zero"),
    new Number(1, "one"),
    new Number(2, "two"),
    new Number(3, "three"),
    new Number(4, "four"),
    new Number(5, "five"),
    new Number(6, "six"),
    new Number(7, "seven"),
    new Number(8, "eight"),            
    new Number(9, "nine") };        


    public int solution(string s)
    {
        foreach(Number num in numList)
        {
            s = s.Replace(num.numString, num.num.ToString());
        }

        int answer = Convert.ToInt32(s);
        Console.WriteLine(answer);
        return answer;
    }
}

public class Number
{
    public Number(int v1, string v2)
    {
        this.num = v1;
        this.numString = v2;
    }

    public int num;
    public string numString;                
}
