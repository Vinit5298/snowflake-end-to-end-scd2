Use Schema Silver;

Create Or Replace Table Silver_Customer (
    Customer_Sk Number Autoincrement,
    Customer_Id String,
    Customer_Name String,
    Email_Id String,
    Phone_Number String,
    City String,
    State String,
    Country String,
    Customer_Segment String,
    Credit_Rating String,
    Customer_Status String,
    Source_System String,
    Record_Hash String,
    Effective_Start_Dt Date,
    Effective_End_Dt Date,
    Is_Current Boolean,
    Load_Timestamp Timestamp
);
