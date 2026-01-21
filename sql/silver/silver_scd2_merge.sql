Merge Into Silver.Silver_Customer Tgt
Using (
    Select
        Customer_Id,
        Customer_Name,
        Email_Id,
        Phone_Number,
        City,
        State,
        Country,
        Customer_Segment,
        Credit_Rating,
        Customer_Status,
        Source_System,
        Record_Hash
    From Bronze.Bronze_Customer_Stream
) Src
On Tgt.Customer_Id = Src.Customer_Id
And Tgt.Is_Current = True

When Matched
And Tgt.Record_Hash <> Src.Record_Hash
Then Update Set
    Tgt.Is_Current = False,
    Tgt.Effective_End_Dt = Current_Date - 1

When Not Matched
Then Insert (
    Customer_Id,
    Customer_Name,
    Email_Id,
    Phone_Number,
    City,
    State,
    Country,
    Customer_Segment,
    Credit_Rating,
    Customer_Status,
    Source_System,
    Record_Hash,
    Effective_Start_Dt,
    Effective_End_Dt,
    Is_Current,
    Load_Timestamp
)
Values (
    Src.Customer_Id,
    Src.Customer_Name,
    Src.Email_Id,
    Src.Phone_Number,
    Src.City,
    Src.State,
    Src.Country,
    Src.Customer_Segment,
    Src.Credit_Rating,
    Src.Customer_Status,
    Src.Source_System,
    Src.Record_Hash,
    Current_Date,
    '9999-12-31',
    True,
    Current_Timestamp
);
