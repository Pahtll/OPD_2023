using System;
class MyVector
{
    private int x;
    private int y;

    public MyVector()
    {

    }
    public MyVector(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    public static MyVector operator +(MyVector v1, MyVector v2)
    {
        return new MyVector(v1.x + v2.x, v1.y + v2.y);
    }
    public static MyVector operator -(MyVector v1, MyVector v2)
    {
        return new MyVector(v1.x + v2.x, v1.y - v2.y);
    }
    public static MyVector operator *(MyVector v1, int value)
    {
        return new MyVector(v1.x * value, v1.y * value);
    }
    public static MyVector operator *(int value, MyVector v1)
    {
        return new MyVector(v1.x * value, v1.y * value);
    }
    public static bool operator ==(MyVector v1, MyVector v2)
    {
        return v1.x == v2.x && v1.y == v2.y;
    }
    public static bool operator !=(MyVector v1, MyVector v2)
    {
        return v1.x != v2.x || v1.y != v2.y;
    }
    public static double Len(MyVector v)
    {
        return Math.Sqrt(Math.Pow(v.x, 2) + Math.Pow(v.y, 2));
    }
    public override string ToString()
    {
        MyVector v = new MyVector(this.x, this.y);
        string res = Convert.ToString(Len(v));
        return res;
    }
}

class Program
{
    public static void Main(string[] args)
    {
        MyVector v1 = new MyVector(-5, 2);
        MyVector v2 = new MyVector(3, -4);
        MyVector vSum = v1 + v2;
        Console.WriteLine(vSum);
    }
}
