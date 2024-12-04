import sqlite3, os
from structs import caseStruct, userStruct

os.chdir(os.getcwd())

#' = %27
#" = %22
#% = %25

class cases:
    def insert(case : caseStruct):
        conn = sqlite3.connect("db")
        c = conn.cursor()

        case = caseStruct([item.replace("%", "%25").replace("'", "%27").replace('"', "%22") if type(item) == str else item for item in [case.caseNum, case.information.complainant.discord.username, case.information.complainant.discord.id, case.information.complainant.roblox.username, case.information.complainant.roblox.id, case.information.employee.discord.username, case.information.employee.discord.id, case.information.employee.roblox.username, case.information.employee.roblox.id, case.information.what, case.information.evidence, case.information.when, case.information.extra, case.information.investigator.discord.username, case.information.investigator.discord.id, case.information.investigator.roblox.username, case.information.investigator.roblox.id, case.information.employeeSupervisor.discord.username, case.information.employeeSupervisor.discord.id, case.information.employeeSupervisor.roblox.username, case.information.employeeSupervisor.roblox.id, case.processes.contacts.complainant, case.processes.contacts.supervisor, case.processes.contacts.employee, case.processes.contacts.witnesses, case.processes.investigation.actionRecommended, case.processes.investigation.paperwork, case.processes.conclusion.investigatorSupervisorApproval, case.processes.conclusion.disciplineEnforced, case.notification, case.summary, case.closed]])

        c.execute(f"""INSERT INTO cases VALUES({case.caseNum}, "{case.information.complainant.discord.username}", {case.information.complainant.discord.id}, "{case.information.complainant.roblox.username}", {case.information.complainant.roblox.id}, "{case.information.employee.discord.username}", {case.information.employee.discord.id}, "{case.information.employee.roblox.username}", {case.information.employee.roblox.id}, "{case.information.what}", "{case.information.evidence}", "{case.information.when}", "{case.information.extra}", "{case.information.investigator.discord.username}", {case.information.investigator.discord.id}, "{case.information.investigator.roblox.username}", {case.information.investigator.roblox.id}, "{case.information.employeeSupervisor.discord.username}", {case.information.employeeSupervisor.discord.id}, "{case.information.employeeSupervisor.roblox.username}", {case.information.employeeSupervisor.roblox.id}, {case.processes.contacts.complainant}, {case.processes.contacts.supervisor}, {case.processes.contacts.employee}, {case.processes.contacts.witnesses}, "{case.processes.investigation.actionRecommended}", {case.processes.investigation.paperwork}, {case.processes.conclusion.investigatorSupervisorApproval}, {case.processes.conclusion.disciplineEnforced}, "{case.notification}", "{case.summary}", {case.closed})""")

        conn.commit()
    
    def update(caseNum : int, what : str, to):
        conn = sqlite3.connect("db")
        c = conn.cursor()

        if type(to) == str:
            to = to.replace("%", "%25").replace("'", "%27").replace('"', "%22")

        c.execute(f"""UPDATE cases SET "{what}" = {f'"{to}"' if type(to) == str else to} WHERE caseNum = {caseNum}""")

        conn.commit()
    
    def get(caseNum : int) -> caseStruct or None:
        conn = sqlite3.connect("db")
        c = conn.cursor()

        d = c.execute(f"SELECT * FROM cases WHERE caseNum = {caseNum}")
        
        theGet = d.fetchall()
        
        return caseStruct([item.replace("%27", "'").replace("%22", '"').replace("%25", "%") if type(item) == str else item for item in theGet[0]]) if theGet else None
    
    def getRaw(caseNum : int) -> list or None:
        conn = sqlite3.connect("db")
        c = conn.cursor()

        d = c.execute(f"SELECT * FROM cases WHERE caseNum = {caseNum}")
        
        theGet = d.fetchall()
        
        return [item.replace("%27", "'").replace("%22", '"').replace("%25", "%") if type(item) == str else item for item in theGet[0]] if theGet else None

    def remove(caseNum : int):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"DELETE FROM cases WHERE caseNum = {caseNum}")
        
        conn.commit()
    
    def fetch() -> list:
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        d = c.execute("SELECT * FROM cases")
        
        return [caseStruct(case) for case in d.fetchall()]
        
    def check(caseNum : int) -> bool:
        db = cases.fetch()
        caseNums = [el.caseNum for el in db]
        return (caseNum in caseNums)
    
    def next() -> int:
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        d = [el[0] for el in c.execute("SELECT caseNum FROM cases")]
        
        return next(i for i in range(1, len(d) + 2) if i not in d)

    def create():
        conn = sqlite3.connect("db")
        c = conn.cursor()

        c.execute(f"""CREATE TABLE IF NOT EXISTS cases (
            caseNum INTEGER PRIMARY KEY,
            information_complainant_discord_username TEXT,
            information_complainant_discord_id INTEGER,
            information_complainant_roblox_username TEXT,
            information_complainant_roblox_id INTEGER,
            information_employee_discord_username TEXT,
            information_employee_discord_id INTEGER,
            information_employee_roblox_username TEXT,
            information_employee_roblox_id INTEGER,
            information_what TEXT,
            information_evidence TEXT,
            information_when TEXT,
            information_extra TEXT,
            information_investigator_discord_username TEXT,
            information_investigator_discord_id INTEGER,
            information_investigator_roblox_username TEXT,
            information_investigator_roblox_id INTEGER,
            information_employeeSupervisor_discord_username TEXT,
            information_employeeSupervisor_discord_id INTEGER,
            information_employeeSupervisor_roblox_username TEXT,
            information_employeeSupervisor_roblox_id INTEGER,
            processes_contacts_complainant INTEGER,
            processes_contacts_supervisor INTEGER,
            processes_contacts_employee INTEGER,
            processes_contacts_witnesses INTEGER,
            processes_investigation_actionRecommended TEXT,
            processes_investigation_papework INTEGER,
            processes_conclusion_investigatorSupervisorApproval INTEGER,
            processes_conclusion_disciplineEnforced INTEGER,
            notification TEXT,
            summary TEXT,
            closed INTEGER
        )""")
        
        conn.commit()

class blacklists:
    def insert(user : userStruct):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"""INSERT INTO blacklists VALUES("{user.discord.username}", {user.discord.id}, "{user.roblox.username}", {user.roblox.id})""")

        conn.commit()
    
    def update(robloxUserID : int, what : str, to):
        conn = sqlite3.connect("db")
        c = conn.cursor()

        if type(to) == str:
            to = to.replace("%", "%25").replace("'", "%27").replace('"', "%22")

        c.execute(f"""UPDATE blacklists SET "{what}" = {f'"{to}"' if type(to) == str else to} WHERE roblox_id = {robloxUserID}""")

        conn.commit()
    
    def get(robloxUserID : int) -> userStruct or None:
        conn = sqlite3.connect("db")
        c = conn.cursor()

        d = c.execute(f"SELECT * FROM blacklists WHERE roblox_id = {robloxUserID}")
        
        theGet = d.fetchall()
        
        return userStruct([item for item in theGet[0]]) if theGet else None
    
    def getRaw(robloxUserID : int) -> list or None:
        conn = sqlite3.connect("db")
        c = conn.cursor()

        d = c.execute(f"SELECT * FROM blacklists WHERE roblox_id = {robloxUserID}")
        
        theGet = d.fetchall()
        
        return theGet[0] if theGet else None

    def remove(robloxUserID : int):
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"DELETE FROM blacklists WHERE roblox_id = {robloxUserID}")
        
        conn.commit()
    
    def fetch() -> list:
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        d = c.execute("SELECT * FROM blacklists")
        
        return [userStruct(user) for user in d.fetchall()]
        
    def check(robloxUserID : int) -> bool:
        db = blacklists.fetch()
        robloxUserIDs = [el.roblox.id for el in db]
        return (robloxUserID in robloxUserIDs)

    def create():
        conn = sqlite3.connect("db")
        c = conn.cursor()

        c.execute(f"""CREATE TABLE IF NOT EXISTS blacklists (
            discord_username STRING,
            discord_id INTEGER,
            roblox_username STRING,
            roblox_id INTEGER PRIMARY KEY
        )""")
        
        conn.commit()

class ormsupervisor:
    def insert(user : userStruct):
        exists = ormsupervisor.get()

        if exists:
            ormsupervisor.remove()

        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"""INSERT INTO ormsupervisor VALUES("{user.discord.username}", {user.discord.id}, "{user.roblox.username}", {user.roblox.id})""")

        conn.commit()

        return True
    
    def remove():
        conn = sqlite3.connect("db")
        c = conn.cursor()
        
        c.execute(f"DELETE FROM ormsupervisor")
        
        conn.commit()
    
    def get() -> userStruct or None:
        conn = sqlite3.connect("db")
        c = conn.cursor()

        d = c.execute(f"SELECT * FROM ormsupervisor")
        
        theGet = d.fetchall()

        if not theGet:
            return None
        
        return userStruct(theGet[0]) if theGet[0] else None
    
    def create():
        conn = sqlite3.connect("db")
        c = conn.cursor()

        c.execute(f"""CREATE TABLE IF NOT EXISTS ormsupervisor (
            discord_username STRING,
            discord_id INTEGER,
            roblox_username STRING,
            roblox_id INTEGER
        )""")