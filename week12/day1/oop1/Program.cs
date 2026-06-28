using System;
namespace oop;
enum AccountTypes{ Checking,Business,Saving}
class BankAccount
{

    private string _ownerName;
    private double _balance;
    private string _accountType;
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
    public string AccountType
    {
        get => _accountType;
        set
        {
            if (Enum.TryParse(value, out AccountTypes PresedValue))
                _accountType = value;
            else _accountType = "Cheking";

        }

    }
    public bool IsActive
    {
        get => _isActive;
        set
        {
            _isActive = value;

        }

    }
    public BankAccount(int accountNumber, string ownerName, double balance, string accountType, List<string> transationHistory, bool isactive = true)
    {
        AccountNumber = accountNumber;
        OwnerName = ownerName;
        Balance = balance;
        AccountType = accountType;
        IsActive = isactive;
        _transationHistory = transationHistory ?? new List<string>();
    }
    public BankAccount(int accountNumber, string ownerName) : this(accountNumber, ownerName, 0.0, "Checking", new List<string>())
    {

    }
    public override string ToString()
    {
        return $" Account # {AccountNumber} Owner {OwnerName} balance {Balance.ToString("F2")} $ type {AccountType} status is {IsActive}";
    }
    public void Deposit(double amount)
    {
        if (this.IsActive == true)
        {
            if (amount < 0)
            {
                Console.WriteLine("invalid amount");
            }
            else this._balance += amount;
            this._transationHistory.Add($"deposit {amount}");
        }
        else Console.WriteLine("account not active");
    }
    public bool withdraw(double amount)
    {
        if (this.IsActive == true)
        {


            if (amount > 0 && this.Balance > amount)

            {
                this.Balance -= amount;
                this._transationHistory.Add($" withdraw {amount}");
                return true;
            }
            else Console.WriteLine("balance not enagh to withdrdraw ");
            return false;
        }
        else Console.WriteLine("account not active");
        return false;
    }
    public void ApplyIterset()
    {
        if (this.AccountType == "Saving")
        {
            this.Balance *= 1.02;

        }
    }
    public void PrintTransactionHistory()
    {
        foreach (string item in this._transationHistory)
        {
            Console.WriteLine(item);
        }
    }
    public void activate()
    {
        this.IsActive = true;
    }
    public void Deactivate()
    {
        this.IsActive = false;
    }
    public static bool Transfer(BankAccount from, BankAccount to, double amount)
    {
        if (from.IsActive == true && to.IsActive == true)
        {
            if (from.withdraw(amount))
            {

                to.Deposit(amount);
            }
            return true;
        }
        else Console.WriteLine("you conot to make transfer");
        return false;
    }
    class Tirgul
    {
        class main {
            static void Main()
            {
                List<BankAccount> allAccounts = new List<BankAccount>() ;

                //BankAccount a = new BankAccount(10, "avi", 150, "Check", [], false);
                //BankAccount b = new BankAccount(20, "aron");
                //Console.WriteLine($" id number {a.AccountNumber} name is {a.OwnerName} balance is {a.Balance} type is {a.AccountType} status is {a.IsActive}");
                //Console.WriteLine($" id number {b.AccountNumber} name is {b.OwnerName} balance is {b.Balance} type is {b.AccountType} ");
                //Console.WriteLine(a.ToString());
                //a.Deposit(120);
                //Console.WriteLine(a.ToString());
                //a.Deposit(50);
                //a.withdraw(25);
                //a.withdraw(40);
                //Console.WriteLine(a.ToString());
                //a.PrintTransactionHistory();
                //a.activate();
                //Console.WriteLine(a.ToString());
                //Transfer(a, b, 40);
                //Console.WriteLine(a.ToString());
                //Console.WriteLine(b.ToString());
                //a.PrintTransactionHistory();
                //b.PrintTransactionHistory();
                allAccounts.Add(new BankAccount(10, "avi", 120.0, "Saving", [],true));
                allAccounts.Add(new BankAccount(20 ,"", 47.0, "Checking", [], true));
                allAccounts.Add(new BankAccount(30, "nati", -1, "Checking", [], true));
                allAccounts.Add(new BankAccount(40, "yosi", 140.0, "Sa", [], true));
                allAccounts.Add(new BankAccount(50, "noach", 85.0, "Saving", [], true));
                foreach(BankAccount item in allAccounts)
                {
                    Console.WriteLine(item.ToString());
                }

            }
        }
    }
}
