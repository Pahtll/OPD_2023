using System;

class Queue
{
    public List<int> nums = new List<int>();
    /// <summary>
    /// Переопределяем конструктор
    /// </summary>
    /// <param name="args"></param>
    public Queue(params int[] args)
    {
        foreach (int i in args)
        {
            nums.Add(i);
        }
    }
    /// <summary>
    /// Метод добавляет в конец очереди числа.
    /// </summary>
    /// <param name="nums"></param>
    /// <returns></returns>
    public List<int> Append(params int[] nums)
    {
        foreach (int i in nums)
        {
            this.nums.Add(i);
        }
        return this.nums;
    }
    /// <summary>
    /// Копирует текущую очередь в новую.
    /// </summary>
    /// <returns></returns>
    public Queue Copy()
    { 
        return new Queue(this.nums.ToArray());
    }
    /// <summary>
    /// Выбивает и выводит 0й элемент очереди если она не пустая и 0 если пустая.
    /// </summary>
    /// <returns></returns>
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
    /// <summary>
    /// Расширяет очередь другой очередью
    /// </summary>
    /// <param name="ints"></param>
    /// <returns></returns>
    public Queue Extend(Queue ints)
    {
        this.nums.AddRange(ints.nums);
        return new Queue(this.nums.ToArray());
    }
    /*
     * Перегруженный 3 раза под разные аргументы метод Next()
     */
    /// <summary>
    /// Убирает 0й элемент очереди.
    /// </summary>
    /// <returns></returns>
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
    /*
     * Функции для работы операторов сложения, сравнения и переноса.
     */
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
    /// <summary>
    /// Функция для вывода очереди в текстовом формате (Console.WriteLine() вызывает метод ToString()
    /// для своей работы.
    /// </summary>
    /// <returns></returns>
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
        
    }
}
