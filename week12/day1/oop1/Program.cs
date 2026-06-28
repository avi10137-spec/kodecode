using System;
namespace oop;
enum AccountTypes{ Checking,Business,Saving}
class BankAccount
{

    private string _ownerName;
    private double _balance;
    private AccountTypes _accountType;
    private bool _isActive;
    private List<string> _transationHistory;
    public int AccountNumber { get; }
    public string OwnerName
    {
        get => _ownerName;
        set
        {
            if (string.IsNullOrWhiteSpace(value))
                _ownerName = "Unknown";
            else
                _ownerName = value;


        }
        }
    public double Balance
    {
        get => _balance;
        set
        {
            if (value < 0)
                _balance = 0;
            else _balance = value;
        }
    }
    public AccountTypes AccountType
    {
        get => _accountType;
        set
        {
            
            
                _accountType = value;
            
            

        }

    }

    public BankAccount(int accountNumber, string ownerName,double balance,AccountTypes accountType = AccountTypes.Checking)
    {
        AccountNumber = accountNumber;
        OwnerName = ownerName;
        Balance = balance;
        AccountType = accountType;
    }
}
class Tirgul
{
    static void Main()
    {
        BankAccount a = new BankAccount(10,"avi",150);
        Console.WriteLine($" id number {a.AccountNumber} name is {a.OwnerName} balance is {a.Balance} type is {a.AccountType}");

    }
}
