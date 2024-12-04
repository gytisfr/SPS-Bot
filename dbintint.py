import sqlite3, dbint, os
from structs import caseStruct, userStruct

os.chdir(os.getcwd())

print(os.getcwd())

def getcmd(what : str, valid : list):
    valid = [item.lower() for item in valid]
    valid.append("?") if "?" not in valid else valid
    valid.append("exit") if "exit" not in valid else valid
    cmd = input(f"{what}> ").lower()
    while cmd not in valid:
        print("Invalid input")
        cmd = input(f"{what}> ").lower()
    return cmd

def getint(what : str):
    cmd = ""
    while type(cmd) != int:
        cmd = input(f"{what}> ").lower()
        try:
            cmd = int(cmd)
        except:
            pass
    return cmd

while True:
    cmd = getcmd("Table", ["cases", "blacklists", "ormsupervisor"])
    if cmd == "?":
        print("    cases         - Manage cases database\n    blackists     - Manage blacklisted individuals\n    ormsupervisor - Manage the current ORM Supervisor\n    ?             - Help\n    exit          - Exit database manager")
    elif cmd == "cases":
        while cmd != "exit":
            cmd = getcmd("What", ["insertbasic", "insert", "update", "remove", "get", "fetch", "check", "next", "create"])
            if cmd == "?":
                print("    insertbasic - Insert a basic case\n    insert      - Insert a custom case (not implemented yet)\n    update      - Update a case\n    remove      - Remove a case\n    get         - Get a case by its number\n    fetch       - Get all existing case numbers\n    check       - Check if a case exists by number\n    next        - Get the next available case number\n    create      - Re-create the case table if clearing the db (dev only, don't touch)\n    ?           - Help\n    exit        - Move down a level")
            elif cmd == "insertbasic":
                dbint.cases.insert(caseStruct([1, """g"y't#isfr""", 301014178703998987, """Gytis5089""", 103956751, """xtazyd""", 364568584317304837, """9syn9""", 53735787, """he was reckless driving on team (criminal scum)""", """my evidence""", """yesterday at 69:12""", """no extra information""", """flimzee""", 1069415674356715560, """Flimzee""", 313598727, """mickey4854""", 599011127543988235, """Impediage""", 692140965, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
            elif cmd == "insert":
                pass
            elif cmd == "update":
                cmd1 = getint("Case Num")
                cmd2 = input("What> ").lower()
                cmd25 = getcmd("Is To Int", ["y", "n"])
                if cmd25 == "y":
                    cmd3 = getint("To")
                else:
                    cmd3 = input("To> ").lower()
                dbint.cases.update(cmd1, cmd2, cmd3)
            elif cmd == "remove":
                cmd = getint("Case Num")
                dbint.cases.remove(cmd)
            elif cmd == "get":
                cmd = getcmd("Type", ["1", "2", "3", "4"])
                if cmd == "?":
                    print("    1    - Just values\n    2    - Just values, with types\n    3    - All objects\n    4    - All objects, with types\n    ?    - Help\n    exit - Move down a level")
                caseNum = getint("Case Num")
                case = dbint.cases.get(caseNum)
                if case:
                    if cmd == "1":
                        print(case.caseNum)
                        print(case.information.complainant.discord.username)
                        print(case.information.complainant.discord.id)
                        print(case.information.complainant.roblox.username)
                        print(case.information.complainant.roblox.id)
                        print(case.information.employee.discord.username)
                        print(case.information.employee.discord.id)
                        print(case.information.employee.roblox.username)
                        print(case.information.employee.roblox.id)
                        print(case.information.what)
                        print(case.information.evidence)
                        print(case.information.when)
                        print(case.information.extra)
                        print(case.information.investigator.discord.username)
                        print(case.information.investigator.discord.id)
                        print(case.information.investigator.roblox.username)
                        print(case.information.investigator.roblox.id)
                        print(case.information.employeeSupervisor.discord.username)
                        print(case.information.employeeSupervisor.discord.id)
                        print(case.information.employeeSupervisor.roblox.username)
                        print(case.information.employeeSupervisor.roblox.id)
                        print(case.processes.contacts.complainant)
                        print(case.processes.contacts.supervisor)
                        print(case.processes.contacts.employee)
                        print(case.processes.contacts.witnesses)
                        print(case.processes.investigation.actionRecommended)
                        print(case.processes.investigation.paperwork)
                        print(case.processes.conclusion.investigatorSupervisorApproval)
                        print(case.processes.conclusion.disciplineEnforced)
                        print(case.notification)
                        print(case.summary)
                        print(case.closed)
                    if cmd == "2":
                        print(f"{'int' if type(case.caseNum) == int else 'str' if type(case.caseNum) == str else type(case.caseNum)} {case.caseNum}")
                        print(f"{'int' if type(case.information.complainant.discord.username) == int else 'str' if type(case.information.complainant.discord.username) == str else type(case.information.complainant.discord.username)} {case.information.complainant.discord.username}")
                        print(f"{'int' if type(case.information.complainant.discord.id) == int else 'str' if type(case.information.complainant.discord.id) == str else type(case.information.complainant.discord.id)} {case.information.complainant.discord.id}")
                        print(f"{'int' if type(case.information.complainant.roblox.username) == int else 'str' if type(case.information.complainant.roblox.username) == str else type(case.information.complainant.roblox.username)} {case.information.complainant.roblox.username}")
                        print(f"{'int' if type(case.information.complainant.roblox.id) == int else 'str' if type(case.information.complainant.roblox.id) == str else type(case.information.complainant.roblox.id)} {case.information.complainant.roblox.id}")
                        print(f"{'int' if type(case.information.employee.discord.username) == int else 'str' if type(case.information.employee.discord.username) == str else type(case.information.employee.discord.username)} {case.information.employee.discord.username}")
                        print(f"{'int' if type(case.information.employee.discord.id) == int else 'str' if type(case.information.employee.discord.id) == str else type(case.information.employee.discord.id)} {case.information.employee.discord.id}")
                        print(f"{'int' if type(case.information.employee.roblox.username) == int else 'str' if type(case.information.employee.roblox.username) == str else type(case.information.employee.roblox.username)} {case.information.employee.roblox.username}")
                        print(f"{'int' if type(case.information.employee.roblox.id) == int else 'str' if type(case.information.employee.roblox.id) == str else type(case.information.employee.roblox.id)} {case.information.employee.roblox.id}")
                        print(f"{'int' if type(case.information.what) == int else 'str' if type(case.information.what) == str else type(case.information.what)} {case.information.what}")
                        print(f"{'int' if type(case.information.evidence) == int else 'str' if type(case.information.evidence) == str else type(case.information.evidence)} {case.information.evidence}")
                        print(f"{'int' if type(case.information.when) == int else 'str' if type(case.information.when) == str else type(case.information.when)} {case.information.when}")
                        print(f"{'int' if type(case.information.extra) == int else 'str' if type(case.information.extra) == str else type(case.information.extra)} {case.information.extra}")
                        print(f"{'int' if type(case.information.investigator.discord.username) == int else 'str' if type(case.information.investigator.discord.username) == str else type(case.information.investigator.discord.username)} {case.information.investigator.discord.username}")
                        print(f"{'int' if type(case.information.investigator.discord.id) == int else 'str' if type(case.information.investigator.discord.id) == str else type(case.information.investigator.discord.id)} {case.information.investigator.discord.id}")
                        print(f"{'int' if type(case.information.investigator.roblox.username) == int else 'str' if type(case.information.investigator.roblox.username) == str else type(case.information.investigator.roblox.username)} {case.information.investigator.roblox.username}")
                        print(f"{'int' if type(case.information.investigator.roblox.id) == int else 'str' if type(case.information.investigator.roblox.id) == str else type(case.information.investigator.roblox.id)} {case.information.investigator.roblox.id}")
                        print(f"{'int' if type(case.information.employeeSupervisor.discord.username) == int else 'str' if type(case.information.employeeSupervisor.discord.username) == str else type(case.information.employeeSupervisor.discord.username)} {case.information.employeeSupervisor.discord.username}")
                        print(f"{'int' if type(case.information.employeeSupervisor.discord.id) == int else 'str' if type(case.information.employeeSupervisor.discord.id) == str else type(case.information.employeeSupervisor.discord.id)} {case.information.employeeSupervisor.discord.id}")
                        print(f"{'int' if type(case.information.employeeSupervisor.roblox.username) == int else 'str' if type(case.information.employeeSupervisor.roblox.username) == str else type(case.information.employeeSupervisor.roblox.username)} {case.information.employeeSupervisor.roblox.username}")
                        print(f"{'int' if type(case.information.employeeSupervisor.roblox.id) == int else 'str' if type(case.information.employeeSupervisor.roblox.id) == str else type(case.information.employeeSupervisor.roblox.id)} {case.information.employeeSupervisor.roblox.id}")
                        print(f"{'int' if type(case.processes.contacts.complainant) == int else 'str' if type(case.processes.contacts.complainant) == str else type(case.processes.contacts.complainant)} {case.processes.contacts.complainant}")
                        print(f"{'int' if type(case.processes.contacts.supervisor) == int else 'str' if type(case.processes.contacts.supervisor) == str else type(case.processes.contacts.supervisor)} {case.processes.contacts.supervisor}")
                        print(f"{'int' if type(case.processes.contacts.employee) == int else 'str' if type(case.processes.contacts.employee) == str else type(case.processes.contacts.employee)} {case.processes.contacts.employee}")
                        print(f"{'int' if type(case.processes.contacts.witnesses) == int else 'str' if type(case.processes.contacts.witnesses) == str else type(case.processes.contacts.witnesses)} {case.processes.contacts.witnesses}")
                        print(f"{'int' if type(case.processes.investigation.actionRecommended) == int else 'str' if type(case.processes.investigation.actionRecommended) == str else type(case.processes.investigation.actionRecommended)} {case.processes.investigation.actionRecommended}")
                        print(f"{'int' if type(case.processes.investigation.paperwork) == int else 'str' if type(case.processes.investigation.paperwork) == str else type(case.processes.investigation.paperwork)} {case.processes.investigation.paperwork}")
                        print(f"{'int' if type(case.processes.conclusion.investigatorSupervisorApproval) == int else 'str' if type(case.processes.conclusion.investigatorSupervisorApproval) == str else type(case.processes.conclusion.investigatorSupervisorApproval)} {case.processes.conclusion.investigatorSupervisorApproval}")
                        print(f"{'int' if type(case.processes.conclusion.disciplineEnforced) == int else 'str' if type(case.processes.conclusion.disciplineEnforced) == str else type(case.processes.conclusion.disciplineEnforced)} {case.processes.conclusion.disciplineEnforced}")
                        print(f"{'int' if type(case.notification) == int else 'str' if type(case.notification) == str else type(case.notification)} {case.notification}")
                        print(f"{'int' if type(case.closed) == int else 'str' if type(case.closed) == str else type(case.closed)} {case.closed}")
                    elif cmd == "3":
                        print(case.caseNum)
                        print(case.information)
                        print(case.information.complainant)
                        print(case.information.complainant.discord)
                        print(case.information.complainant.discord.username)
                        print(case.information.complainant.discord.id)
                        print(case.information.complainant.roblox)
                        print(case.information.complainant.roblox.username)
                        print(case.information.complainant.roblox.id)
                        print(case.information.employee)
                        print(case.information.employee.discord)
                        print(case.information.employee.discord.username)
                        print(case.information.employee.discord.id)
                        print(case.information.employee.roblox)
                        print(case.information.employee.roblox.username)
                        print(case.information.employee.roblox.id)
                        print(case.information.what)
                        print(case.information.evidence)
                        print(case.information.when)
                        print(case.information.extra)
                        print(case.information.investigator)
                        print(case.information.investigator.discord)
                        print(case.information.investigator.discord.username)
                        print(case.information.investigator.discord.id)
                        print(case.information.investigator.roblox)
                        print(case.information.investigator.roblox.username)
                        print(case.information.investigator.roblox.id)
                        print(case.information.employeeSupervisor)
                        print(case.information.employeeSupervisor.discord)
                        print(case.information.employeeSupervisor.discord.username)
                        print(case.information.employeeSupervisor.discord.id)
                        print(case.information.employeeSupervisor.roblox)
                        print(case.information.employeeSupervisor.roblox.username)
                        print(case.information.employeeSupervisor.roblox.id)
                        print(case.processes)
                        print(case.processes.contacts)
                        print(case.processes.contacts.complainant)
                        print(case.processes.contacts.supervisor)
                        print(case.processes.contacts.employee)
                        print(case.processes.contacts.witnesses)
                        print(case.processes.investigation)
                        print(case.processes.investigation.actionRecommended)
                        print(case.processes.investigation.paperwork)
                        print(case.processes.conclusion)
                        print(case.processes.conclusion.investigatorSupervisorApproval)
                        print(case.processes.conclusion.disciplineEnforced)
                        print(case.notification)
                        print(case.summary)
                        print(case.closed)
                    elif cmd == "4":
                        print(f"{'int' if type(case.caseNum) == int else 'str' if type(case.caseNum) == str else '   '} {case.caseNum}")
                        print(f"{'int' if type(case.information) == int else 'str' if type(case.information) == str else '   '} {case.information}")
                        print(f"{'int' if type(case.information.complainant) == int else 'str' if type(case.information.complainant) == str else '   '} {case.information.complainant}")
                        print(f"{'int' if type(case.information.complainant.discord) == int else 'str' if type(case.information.complainant.discord) == str else '   '} {case.information.complainant.discord}")
                        print(f"{'int' if type(case.information.complainant.discord.username) == int else 'str' if type(case.information.complainant.discord.username) == str else '   '} {case.information.complainant.discord.username}")
                        print(f"{'int' if type(case.information.complainant.discord.id) == int else 'str' if type(case.information.complainant.discord.id) == str else '   '} {case.information.complainant.discord.id}")
                        print(f"{'int' if type(case.information.complainant.roblox) == int else 'str' if type(case.information.complainant.roblox) == str else '   '} {case.information.complainant.roblox}")
                        print(f"{'int' if type(case.information.complainant.roblox.username) == int else 'str' if type(case.information.complainant.roblox.username) == str else '   '} {case.information.complainant.roblox.username}")
                        print(f"{'int' if type(case.information.complainant.roblox.id) == int else 'str' if type(case.information.complainant.roblox.id) == str else '   '} {case.information.complainant.roblox.id}")
                        print(f"{'int' if type(case.information.employee) == int else 'str' if type(case.information.employee) == str else '   '} {case.information.employee}")
                        print(f"{'int' if type(case.information.employee.discord) == int else 'str' if type(case.information.employee.discord) == str else '   '} {case.information.employee.discord}")
                        print(f"{'int' if type(case.information.employee.discord.username) == int else 'str' if type(case.information.employee.discord.username) == str else '   '} {case.information.employee.discord.username}")
                        print(f"{'int' if type(case.information.employee.discord.id) == int else 'str' if type(case.information.employee.discord.id) == str else '   '} {case.information.employee.discord.id}")
                        print(f"{'int' if type(case.information.employee.roblox) == int else 'str' if type(case.information.employee.roblox) == str else '   '} {case.information.employee.roblox}")
                        print(f"{'int' if type(case.information.employee.roblox.username) == int else 'str' if type(case.information.employee.roblox.username) == str else '   '} {case.information.employee.roblox.username}")
                        print(f"{'int' if type(case.information.employee.roblox.id) == int else 'str' if type(case.information.employee.roblox.id) == str else '   '} {case.information.employee.roblox.id}")
                        print(f"{'int' if type(case.information.what) == int else 'str' if type(case.information.what) == str else '   '} {case.information.what}")
                        print(f"{'int' if type(case.information.evidence) == int else 'str' if type(case.information.evidence) == str else '   '} {case.information.evidence}")
                        print(f"{'int' if type(case.information.when) == int else 'str' if type(case.information.when) == str else '   '} {case.information.when}")
                        print(f"{'int' if type(case.information.extra) == int else 'str' if type(case.information.extra) == str else '   '} {case.information.extra}")
                        print(f"{'int' if type(case.information.investigator) == int else 'str' if type(case.information.investigator) == str else '   '} {case.information.investigator}")
                        print(f"{'int' if type(case.information.investigator.discord) == int else 'str' if type(case.information.investigator.discord) == str else '   '} {case.information.investigator.discord}")
                        print(f"{'int' if type(case.information.investigator.discord.username) == int else 'str' if type(case.information.investigator.discord.username) == str else '   '} {case.information.investigator.discord.username}")
                        print(f"{'int' if type(case.information.investigator.discord.id) == int else 'str' if type(case.information.investigator.discord.id) == str else '   '} {case.information.investigator.discord.id}")
                        print(f"{'int' if type(case.information.investigator.roblox) == int else 'str' if type(case.information.investigator.roblox) == str else '   '} {case.information.investigator.roblox}")
                        print(f"{'int' if type(case.information.investigator.roblox.username) == int else 'str' if type(case.information.investigator.roblox.username) == str else '   '} {case.information.investigator.roblox.username}")
                        print(f"{'int' if type(case.information.investigator.roblox.id) == int else 'str' if type(case.information.investigator.roblox.id) == str else '   '} {case.information.investigator.roblox.id}")
                        print(f"{'int' if type(case.information.employeeSupervisor) == int else 'str' if type(case.information.employeeSupervisor) == str else '   '} {case.information.employeeSupervisor}")
                        print(f"{'int' if type(case.information.employeeSupervisor.discord) == int else 'str' if type(case.information.employeeSupervisor.discord) == str else '   '} {case.information.employeeSupervisor.discord}")
                        print(f"{'int' if type(case.information.employeeSupervisor.discord.username) == int else 'str' if type(case.information.employeeSupervisor.discord.username) == str else '   '} {case.information.employeeSupervisor.discord.username}")
                        print(f"{'int' if type(case.information.employeeSupervisor.discord.id) == int else 'str' if type(case.information.employeeSupervisor.discord.id) == str else '   '} {case.information.employeeSupervisor.discord.id}")
                        print(f"{'int' if type(case.information.employeeSupervisor.roblox) == int else 'str' if type(case.information.employeeSupervisor.roblox) == str else '   '} {case.information.employeeSupervisor.roblox}")
                        print(f"{'int' if type(case.information.employeeSupervisor.roblox.username) == int else 'str' if type(case.information.employeeSupervisor.roblox.username) == str else '   '} {case.information.employeeSupervisor.roblox.username}")
                        print(f"{'int' if type(case.information.employeeSupervisor.roblox.id) == int else 'str' if type(case.information.employeeSupervisor.roblox.id) == str else '   '} {case.information.employeeSupervisor.roblox.id}")
                        print(f"{'int' if type(case.processes) == int else 'str' if type(case.processes) == str else '   '} {case.processes}")
                        print(f"{'int' if type(case.processes.contacts) == int else 'str' if type(case.processes.contacts) == str else '   '} {case.processes.contacts}")
                        print(f"{'int' if type(case.processes.contacts.complainant) == int else 'str' if type(case.processes.contacts.complainant) == str else '   '} {case.processes.contacts.complainant}")
                        print(f"{'int' if type(case.processes.contacts.supervisor) == int else 'str' if type(case.processes.contacts.supervisor) == str else '   '} {case.processes.contacts.supervisor}")
                        print(f"{'int' if type(case.processes.contacts.employee) == int else 'str' if type(case.processes.contacts.employee) == str else '   '} {case.processes.contacts.employee}")
                        print(f"{'int' if type(case.processes.contacts.witnesses) == int else 'str' if type(case.processes.contacts.witnesses) == str else '   '} {case.processes.contacts.witnesses}")
                        print(f"{'int' if type(case.processes.investigation) == int else 'str' if type(case.processes.investigation) == str else '   '} {case.processes.investigation}")
                        print(f"{'int' if type(case.processes.investigation.actionRecommended) == int else 'str' if type(case.processes.investigation.actionRecommended) == str else '   '} {case.processes.investigation.actionRecommended}")
                        print(f"{'int' if type(case.processes.investigation.paperwork) == int else 'str' if type(case.processes.investigation.paperwork) == str else '   '} {case.processes.investigation.paperwork}")
                        print(f"{'int' if type(case.processes.conclusion) == int else 'str' if type(case.processes.conclusion) == str else '   '} {case.processes.conclusion}")
                        print(f"{'int' if type(case.processes.conclusion.investigatorSupervisorApproval) == int else 'str' if type(case.processes.conclusion.investigatorSupervisorApproval) == str else '   '} {case.processes.conclusion.investigatorSupervisorApproval}")
                        print(f"{'int' if type(case.processes.conclusion.disciplineEnforced) == int else 'str' if type(case.processes.conclusion.disciplineEnforced) == str else '   '} {case.processes.conclusion.disciplineEnforced}")
                        print(f"{'int' if type(case.notification) == int else 'str' if type(case.notification) == str else '   '} {case.notification}")
                        print(f"{'int' if type(case.closed) == int else 'str' if type(case.closed) == str else '   '} {case.closed}")
                else:
                    print(case)
            elif cmd == "fetch":
                print([case.caseNum for case in dbint.cases.fetch()])
            elif cmd == "check":
                cmd = getint("Case Num")
                print(dbint.cases.check(cmd))
            elif cmd == "next":
                print(dbint.cases.next())
            elif cmd == "create":
                dbint.cases.create()
    elif cmd == "blacklists":
        while cmd != "exit":
            cmd = getcmd("Blacklists", ["insertbasic", "insert", "update", "remove", "get", "fetch", "check", "create"])
            if cmd == "?":
                print("    insertbasic - Insert a basic blacklist\n    insert      - Insert a custom blacklist\n    update      - Update a blacklist\n    remove      - Remove a blacklist\n    get         - Get a blacklist by the User's Roblox ID\n    fetch       - Get all existing blacklisted User Roblox ID's\n    check       - Check if a blacklist exists by the User's Roblox ID\n    create      - Re-create the blacklists table if clearing the db (dev only, don't touch)\n    ?           - Help\n    exit        - Move down a level")
            elif cmd == "insertbasic":
                dbint.blacklists.insert(userStruct(["gytisfr", 301014178703998987, "Gytis5089", 103956751]))
            elif cmd == "insert":
                cmd1 = input("User Discord Name> ").lower()
                cmd2 = getint("User Discord ID")
                cmd3 = input("User Roblox Name> ").lower()
                cmd4 = getint("User Roblox ID")
                dbint.blacklists.insert(userStruct([cmd1, cmd2, cmd3, cmd4]))
            elif cmd == "update":
                cmd1 = getint("User Roblox ID")
                cmd2 = input("What> ").lower()
                cmd25 = getcmd("Is To Int", ["y", "n"])
                if cmd25 == "y":
                    cmd3 = getint("To")
                else:
                    cmd3 = input("To> ").lower()
                user = dbint.blacklists.update(cmd1, cmd2, cmd3)
            elif cmd == "remove":
                cmd = getint("User Roblox ID")
                user = dbint.blacklists.remove(cmd)
            elif cmd == "get":
                cmd = getint("User Roblox ID")
                user = dbint.blacklists.get(cmd)
                print(user)
            elif cmd == "fetch":
                user = dbint.blacklists.fetch()
                print(user)
            elif cmd == "check":
                cmd = getint("User Roblox ID")
                user = dbint.blacklists.check(cmd)
                print(user)
            elif cmd == "create":
                dbint.blacklists.create()
    elif cmd == "ormsupervisor":
        while cmd != "exit":
            cmd = getcmd("ORM Supervisor", ["insert", "update", "remove", "get", "create"])
            if cmd == "insert":
                pass
            elif cmd == "update":
                pass
            elif cmd == "remove":
                pass
            elif cmd == "get":
                print(dbint.ormsupervisor.get())
            elif cmd == "create":
                dbint.ormsupervisor.create()