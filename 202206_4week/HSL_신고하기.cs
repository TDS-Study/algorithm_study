using System;
using System.Collections.Generic;
using System.Linq;


public class Solution
{
    public int[] solution(string[] id_list, string[] report, int k)
    {
        int[] answer = new int[] { }; //결과값
        report = report.Distinct().ToArray(); //중복제거
        List<Item> reportList = new List<Item>();
        List<string> targetList = new List<string>();//k번 이상 신고 당한 사람


        foreach (string item in report)
        {
            string from1 = item.Substring(0, item.IndexOf(" "));
            string target1 = item.Substring(item.IndexOf(" "), item.Length - item.IndexOf(" "));

            reportList.Add(new Item(from:from1, target:target1));
        }

        foreach (string target in id_list)
        {
            int count = reportList.Where<Item>(x => x.target == target).Count();
            if (count >= k)
            {   
                targetList.Add(target);
            }
        }

        int idx = 0;
        foreach (string id in id_list)
        {
            int cnt = reportList.Where(x => x.from == id && targetList.Contains(x.target)).Count();                    
            answer.SetValue(cnt, idx);
            idx++;
        }
        
        return answer;
    }    
}

public class Item
{
    public Item(string from, string target)
    {
        this.from = from;
        this.target = target;
    }

    public string from;
    public string target;
}
