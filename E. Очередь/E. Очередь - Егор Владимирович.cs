using System;

class Queue
{
    public List<int> nums = new List<int>();
    public Queue(params int[] args)
    {
        foreach (int i in args)
        {
            nums.Add(i);
        }
    }
    public List<int> Append(params int[] nums)
    {
        foreach (int i in nums)
        {
            this.nums.Add(i);
        }
        return this.nums;
    }
    public Queue Copy()
    { 
        return new Queue(this.nums.ToArray());
    }
    public int Pop()
    {
        if (this.nums.Count == 0)
        {
            return 0;
        }
        int res = nums[0];
        this.nums.RemoveAt(0);
        return res;
    }
    public Queue Extend(Queue ints)
    {
        this.nums.AddRange(ints.nums);
        return new Queue(this.nums.ToArray());
    }
    public Queue Next()
    {
        nums.RemoveAt(0);
        return new Queue(nums.ToArray());
    }
    public Queue Next(int n)
    {
        nums.RemoveAt(n);
        return new Queue(nums.ToArray());
    }
    public Queue Next(Queue q)
    {
        q.nums.RemoveAt(0);
        return new Queue(q.nums.ToArray());
    }
    public static Queue operator +(Queue left, Queue right)
    {
        return new Queue(left.Extend(right).nums.ToArray());
    }
    public static bool operator ==(Queue left, Queue right)
    {
        return left.nums == right.nums;
    }
    public static bool operator !=(Queue left, Queue right)
    {
        return !(left.nums == right.nums);
    }
    public static Queue operator >>(Queue queue, int n)
    {
        if (n > queue.nums.Count())
        {
            for (int i = 0; i < queue.nums.Count(); i++)
            {
                queue.Next(i);
            }
            return queue;
        }
        else
        {
            for (int i = 0; i < n; i++)
            {
                queue.Next(i);
            }
            return queue;
        }
    }
    public override string ToString()
    {
        string res = "[";
        if (this.nums.Count() == 0)
        {
            res += "]";
            return res;
        }
        for (int i = 0; i < this.nums.Count(); i++)
        {
            if (i == this.nums.Count() - 1)
            {
                res += this.nums[i];
                res += "]";
                break;
            }
            res += this.nums[i];
            res += " -> ";
        }
        return res;
    }

}

class Program
{
    public static void Main(string[] args)
    {
        Queue q1 = new Queue(1, 2, 3);
        Console.WriteLine(q1);
        q1.Append(4, 5);
        Console.WriteLine(q1);
        Queue qx = q1.Copy();
        Console.WriteLine(qx.Pop());
        Console.WriteLine(qx);
        Queue q2 = q1.Copy();
        Console.WriteLine(q2);
        Console.WriteLine($"{q1 == q2} {qx == q1}");
        Queue q3 = q2.Next();
        Console.WriteLine($"{q1}\n{q2}\n{q3}\n");
        Console.WriteLine(q1 + q3);
        q3.Extend(new Queue(1, 2));
        Console.WriteLine(q3);
    }
}
