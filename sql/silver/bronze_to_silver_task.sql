Create Or Replace Task Silver.Bronze_To_Silver_Customer_Task
Warehouse = Transform_WH
Schedule = '1 Minute'
When System$Stream_Has_Data('Bronze.Bronze_Customer_Stream')
As
Merge Into Silver.Silver_Customer
Using Bronze.Bronze_Customer_Stream
On Silver_Customer.Customer_Id = Bronze_Customer_Stream.Customer_Id
And Silver_Customer.Is_Current = True;
