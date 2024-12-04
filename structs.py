class userDetailsStruct:
    def __init__(self, data):
        self.username = data[0]
        self.id = data[1]

class userStruct:
    def __init__(self, data):
        self.discord = userDetailsStruct((data[0], data[1]))
        self.roblox = userDetailsStruct((data[2], data[3]))

class caseInformationStruct:
    def __init__(self, data):
        self.complainant = userStruct((data[0], data[1], data[2], data[3]))
        self.employee = userStruct((data[4], data[5], data[6], data[7]))
        self.what = data[8]
        self.evidence = data[9]
        self.when = data[10]
        self.extra = data[11]
        self.investigator = userStruct((data[12], data[13], data[14], data[15]))
        self.employeeSupervisor = userStruct((data[16], data[17], data[18], data[19]))

class caseProcessesContactsStruct:
    def __init__(self, data):
        self.complainant = data[0]
        self.supervisor = data[1]
        self.employee = data[2]
        self.witnesses = data[3]

class caseProcessesInvestigationStruct:
    def __init__(self, data):
        self.actionRecommended = data[0]
        self.paperwork = data[1]

class caseProcessesConclusionStruct:
    def __init__(self, data):
        self.investigatorSupervisorApproval = data[0]
        self.disciplineEnforced = data[1]

class caseProcessesStruct:
    def __init__(self, data):
        self.contacts = caseProcessesContactsStruct((data[0], data[1], data[2], data[3]))
        self.investigation = caseProcessesInvestigationStruct((data[4], data[5]))
        self.conclusion = caseProcessesConclusionStruct((data[6], data[7]))

class caseStruct:
    def __init__(self, data):
        self.caseNum = data[0]
        self.information = caseInformationStruct(data[1:21])
        self.processes = caseProcessesStruct(data[21:29])
        self.notification = data[29]
        self.summary = data[30]
        self.closed = data[31]



"""
caseNum
>information
    >complainant
        >discord
            username
            id
        >roblox
            username
            id
    >employee
        >discord
            username
            id
        >roblox
            username
            id
    what
    evidence
    when
    extra
    >investigator
        >discord
            username
            id
        >roblox
            username
            id
    >employeeSupervisor
        >discord
            username
            id
        >roblox
            username
            id
>processes
    >contacts
        complainant
        supervisor
        employee
        witnesses
    >investigation
        actionRecommended
        paperwork
    >conclusion
        investigatorSupervisorApproval
        disciplineEnforced
notification
summary
closed



caseNum INTEGER PRIMARY KEY,                                    Guaranteed
information_complainant_discord_username TEXT,                  Guaranteed
information_complainant_discord_id INTEGER,                     Guaranteed
information_complainant_roblox_username TEXT,                   Guaranteed
information_complainant_roblox_id INTEGER,                      Guaranteed
information_employee_discord_username TEXT,                     Sometimes
information_employee_discord_id INTEGER,                        Sometimes
information_employee_roblox_username TEXT,                      Guaranteed
information_employee_roblox_id INTEGER,                         Guaranteed
information_what TEXT,                                          Guaranteed
information_evidence TEXT,                                      Guaranteed
information_when TEXT,                                          Guaranteed
information_extra TEXT,                                         Guaranteed
information_investigator_discord_username TEXT,                 On Claim
information_investigator_discord_id INTEGER,                    On Claim
information_investigator_roblox_username TEXT,                  On Claim
information_investigator_roblox_id INTEGER,                     On Claim
information_employeeSupervisor_discord_username TEXT,           On Claim
information_employeeSupervisor_discord_id INTEGER,              On Claim
information_employeeSupervisor_roblox_username TEXT,            On Claim
information_employeeSupervisor_roblox_id INTEGER,               On Claim
processes_contacts_complainant INTEGER,                         Progressive
processes_contacts_supervisor INTEGER,                          Progressive
processes_contacts_employee INTEGER,                            Progressive
processes_contacts_witnesses INTEGER,                           Progressive
processes_investigation_actionRecommended TEXT,                 Progressive
processes_investigation_papework INTEGER,                       Progressive
processes_conclusion_investigatorSupervisorApproval INTEGER,    Progressive
processes_conclusion_disciplineEnforced INTEGER,                Progressive
notification TEXT,                                              Progressive
summary TEXT,                                                   Progressive
closed INTEGER                                                  Progressive
"""