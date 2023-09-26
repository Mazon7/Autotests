class CommonMethods:

    # JavaScript code to get the content of the "window.editor" CodeMirror
    def get_editor_value():
        return """
            (function getValueOfCodemirror() {
                const editor = window.editor;
                return editor.doc.getValue();
            })();
        """
    
    # JavaScript code to set the content of the "window.editor" CodeMirror
    def set_editor_value(query):
        return f"""
            (function setValueToCodemirror() {{
                const editor = window.editor;
                editor.doc.setValue("{query}");
            }})();
        """
    
    get_customers = "SELECT * FROM Customers;"

# class FirstTest:

class SecondTest:
    sql_query = "SELECT * FROM Customers WHERE City='London';"

class ThirdTest:
    record_values = ['Darth Vader', 'Dark Lord', 'Level 77', 'Death Star', 7777, 'Galactic Empire']
    sql_query = r"INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)\nVALUES('Darth Vader', 'Eneken Skywalker', 'Level 77', 'Death Star', 7777, 'Galactic Empire');"

class FourTest:
    record_values = ['Eneken Skywalker', 'Jedi Padawan', 'Dune Sea', 'Mos Eisley', 6666, 'Tatooine']
    sql_query = r"UPDATE Customers SET CustomerName='Eneken Skywalker', ContactName='Jedi Padawan', Address='Dune Sea', City='Mos Eisley', PostalCode=6666, Country='Tatooine' WHERE CustomerID = 1;"

class FifthTest:
    orders_view = r"CREATE VIEW OrdersNew AS SELECT OrderID, OrderDate, CustomerName, ShipperName, Employees.FirstName || ' ' || Employees.LastName AS ProcessedBy FROM Orders\nJOIN Customers ON Orders.CustomerID = Customers.CustomerID\nJOIN Employees ON Orders.EmployeeID = Employees.EmployeeID\nJOIN Shippers ON Orders.ShipperID = Shippers.ShipperID;"

    count_orders = r"SELECT ProcessedBy, COUNT(*) AS OrderNumber\nFROM OrdersNew\nGROUP BY ProcessedBy\nORDER BY OrderNumber DESC;"