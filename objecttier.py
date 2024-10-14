'''
Name: Hiba Mirza
NetID: hmirz4
Course: CS 341 Programming Language Concepts (36202) 2024 Fall
'''
#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
       self._Lobbyist_ID = Lobbyist_ID
       self._First_Name = First_Name
       self._Last_Name = Last_Name
       self._Phone = Phone

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID
    @property
    def First_Name(self):
        return self._First_Name
    @property
    def Last_Name(self):
        return self._Last_Name
    @property
    def Phone(self):
        return self._Phone

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
       self._Lobbyist_ID = Lobbyist_ID
       self._Salutation = Salutation
       self._First_Name = First_Name
       self._Middle_Initial = Middle_Initial
       self._Last_Name = Last_Name
       self._Suffix = Suffix
       self._Address_1 = Address_1
       self._Address_2 = Address_2
       self._City = City
       self._State_Initial = State_Initial
       self._Zip_Code = Zip_Code
       self._Country = Country
       self._Email = Email
       self._Phone = Phone
       self._Fax = Fax
       self._Years_Registered = Years_Registered
       self._Employers = Employers
       self._Total_Compensation = Total_Compensation
       
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID
    @property
    def Salutation(self):
        return self._Salutation
    @property
    def First_Name(self):
        return self._First_Name
    @property
    def Middle_Initial(self):
        return self._Middle_Initial
    @property
    def Last_Name(self):
        return self._Last_Name
    @property
    def Suffix(self):
        return self._Suffix
    @property
    def Address_1(self):
        return self._Address_1
    @property
    def Address_2(self):
        return self._Address_2
    @property
    def City(self):
        return self._City
    @property
    def State_Initial(self):
        return self._State_Initial
    @property
    def Zip_Code(self):
        return self._Zip_Code
    @property
    def Country(self):
        return self._Country
    @property
    def Email(self):
        return self._Email
    @property
    def Phone(self):
        return self._Phone
    @property
    def Fax(self):
        return self._Fax
    @property
    def Years_Registered(self):
        return self._Years_Registered
    @property
    def Employers(self):
        return self._Employers
    @property
    def Total_Compensation(self):
        return self._Total_Compensation
    
##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
       self._Lobbyist_ID = Lobbyist_ID
       self._First_Name = First_Name
       self._Last_Name = Last_Name
       self._Phone = Phone
       self._Total_Compensation = Total_Compensation
       self._Clients = Clients
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID
    @property
    def First_Name(self):
        return self._First_Name
    @property
    def Last_Name(self):
        return self._Last_Name
    @property
    def Phone(self):
        return self._Phone
    @property
    def Total_Compensation(self):
        return self._Total_Compensation
    @property
    def Clients(self):
        return self._Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
    sql = "SELECT COUNT(*) FROM LobbyistInfo;"
    result = datatier.select_one_row(dbConn, sql)
    return result[0] if result is not None else -1

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
    sql = "SELECT COUNT(*) FROM EmployerInfo;"
    result = datatier.select_one_row(dbConn, sql)
    return result[0] if result is not None else -1

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
    sql = "SELECT COUNT(*) FROM ClientInfo;"
    result = datatier.select_one_row(dbConn, sql)
    return result[0] if result is not None else -1


##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
    sql = """
    SELECT Lobbyist_ID, First_Name, Last_Name, Phone
    FROM LobbyistInfo
    WHERE First_Name LIKE ? OR Last_Name LIKE ?
    ORDER BY Lobbyist_ID ASC;
    """
    rows = datatier.select_n_rows(dbConn, sql, [pattern, pattern])
    return [Lobbyist(row[0], row[1], row[2], row[3]) for row in rows] if rows else []


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    lobbyist_info = datatier.select_one_row(dbConn, "SELECT * FROM LobbyistInfo WHERE Lobbyist_ID = ?;", [lobbyist_id])
    if not lobbyist_info:
        return None

    years = [str(row[0]) for row in datatier.select_n_rows(dbConn, "SELECT DISTINCT Year FROM LobbyistYears WHERE Lobbyist_ID = ? ORDER BY Year ASC;", [lobbyist_id]) or []]
    
    employers = [row[0] for row in datatier.select_n_rows(dbConn, """
    SELECT DISTINCT EmployerInfo.Employer_Name
    FROM EmployerInfo
    JOIN LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
    WHERE LobbyistAndEmployer.Lobbyist_ID = ?
    ORDER BY EmployerInfo.Employer_Name ASC;
    """, [lobbyist_id]) or []]

    total_compensation = datatier.select_one_row(dbConn, "SELECT SUM(Compensation_Amount) FROM Compensation WHERE Lobbyist_ID = ?;", [lobbyist_id])
    total_compensation = total_compensation[0] if total_compensation and total_compensation[0] is not None else 0

    return LobbyistDetails(
        Lobbyist_ID=lobbyist_info[0], Salutation=lobbyist_info[1], First_Name=lobbyist_info[2],
        Middle_Initial=lobbyist_info[3], Last_Name=lobbyist_info[4], Suffix=lobbyist_info[5],
        Address_1=lobbyist_info[6], Address_2=lobbyist_info[7], City=lobbyist_info[8],
        State_Initial=lobbyist_info[9], Zip_Code=lobbyist_info[10], Country=lobbyist_info[11],
        Email=lobbyist_info[12], Phone=lobbyist_info[13], Fax=lobbyist_info[14],
        Years_Registered=years, Employers=employers, Total_Compensation=float(total_compensation)
    )



##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    if N <= 0:
        return []

    top_lobbyists = datatier.select_n_rows(dbConn, """
    SELECT LobbyistInfo.Lobbyist_ID, LobbyistInfo.First_Name, LobbyistInfo.Last_Name, LobbyistInfo.Phone, 
           SUM(Compensation.Compensation_Amount) AS TotalCompensation
    FROM LobbyistInfo
    JOIN Compensation ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
    WHERE strftime('%Y', Compensation.Period_Start) = ?
    GROUP BY LobbyistInfo.Lobbyist_ID
    ORDER BY TotalCompensation DESC
    LIMIT ?;
    """, [str(year), N])

    result = []
    for lobbyist in top_lobbyists:
        clients = [row[1] for row in datatier.select_n_rows(dbConn, """
        SELECT DISTINCT ClientInfo.Client_ID, ClientInfo.Client_Name AS Clients
        FROM Compensation
        JOIN ClientInfo ON Compensation.Client_ID = ClientInfo.Client_ID
        WHERE Compensation.Lobbyist_ID = ? AND strftime('%Y', Compensation.Period_Start) = ?
        ORDER BY ClientInfo.Client_Name;
        """, [lobbyist[0], str(year)]) or []]

        result.append(LobbyistClients(
            Lobbyist_ID=lobbyist[0], 
            First_Name=lobbyist[1], 
            Last_Name=lobbyist[2], 
            Phone=lobbyist[3],
            Total_Compensation=lobbyist[4] or 0,
            Clients=clients
        ))

    return result



##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    if not datatier.select_one_row(dbConn, "SELECT COUNT(*) FROM LobbyistInfo WHERE Lobbyist_ID = ?", [lobbyist_id])[0]:
        return 0
    return 1 if datatier.perform_action(dbConn, "INSERT INTO LobbyistYears (Lobbyist_ID, Year) VALUES (?, ?)", [lobbyist_id, year]) is not None else 0



##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    return datatier.perform_action(dbConn, "UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?;", [salutation, lobbyist_id]) or 0 