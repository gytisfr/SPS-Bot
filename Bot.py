import discord, requests, json, datetime, dbint
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
from structs import caseStruct, userStruct

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())
client.remove_command('help')
tree = client.tree

roblosec = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_FE10009E7F17D8984E847356073A33682452721100295AA2F6670A8F09F16BCEFDB65A9A461B2537524C17930D8EF297E0E44A4311CFF81DF1255E49A126D4EB6CD0BFDCF58C17E955B1F024B1DF45E2FA7E650D7E7F5256AAC869271D968FE218084A358B1C4C7228F9532120E298351A7C558742606EF365CA434864394BDA997A86A07E51982312D63332316E8B0B4D8241946807D67532B95BDB74AA26DDEFA09AC7307FCAB2530680FC7328A44D796D440994372F9537788DDDDAA28418977C068104F5CA90ADE9ABE6B504E4EFBBCCF95E972CEEECA039C462F88A0CC957A239CEEC4972A4ED7CD563F807C396DD6FBB431C16AEB16EE7BCA470918E6B1B41E9DA45B24DDA5E60218493B9CF732C2ECD2FECAF70A3B45D155787D383B75582838CAAA2200C53E57F3052EA781DB13EF3B30F2056159CCD2CD0B7C538657E9A65A0C042588F9D57FA7AD7ED354AF665C1F2731EEB86F2490793A3F743A41BC88E6A7E80DCE734554E5B11B13DED16FD29FD179CF4BCA4F2C8A7D5C56A4F689C1E80F8862E8632E82E343E8256D204D50913567161A86388BF8A98EB8734BDF8BF4B153C7C9987C5EF80C6E3B4F892F59948F1D9D1D3CB4A36734B96101DBD22A90A6C5310F65B17AEC7CC05AFF9C4E2E53185AA3087EA065A79684154091145959ACADF7D7682EA1489A90613FCA5654A48D519F08D4DFAE2A6E68D7D463C1BAEA89DB0C3858E3E60B64CA7B8538FE8EDA8AEADCDDA36F54431A5951018A464AC3EA153B6703C4192F507078F78C932CC78CA9AA0910BAB50DCAD92D949227943A6C2B62DDD0D84BACBE0776FC370C23679699D63E23D639ABBA79B573AA397A6D3BCF6DE8867188CF6C331C0CAA8E50315FA962A7BA6A79D71AC6FECD36E33579D0F63DF1D0C48AA260C9C47C6AD5689317072A41D764267B0CFF493FFEE3F18F46C353AB3946EC7F776FBED801F215F0A9FB9264979AA1933404F5F6D779B1E8CEC98210873259674479D5874C2D6E1AFF81924A6C15D98506ABCA8A22D79291DDADF99FFA62897BC2CBC6A5B3AA2128F"
roverKey = "rvr2b097t7qfxrol6u1pnb1rn9lqyljx5s33ngcth2c6jwrbukip9bpj3toiy11fh6uw"

baseURL = "https://sheets.googleapis.com"
spreadsheetID = "1HT-Dla_FiHJTxJoDzyNymoTj3HHIgnNbVPKPTr7yDE8"

tokenDir = "D:\\Ridgeway\\SPS\\Bot\\token.json"

myID = 301014178703998987
gmID = 318207891050070017
guildID = 1213249725050916974
listReportsChannelID = 1215358764094324746
reportsCategoryID = 1215358794285191188
archivesCategoryID = 1238564226382168168
caseLogsChannelID = 1213249725839577139
actionLogsChannelID = 1213249725839577138
ORMRoleID = 1213249725210562624
SPSRoleID = 1213249725155778616
driverRoleID = 1213249725231398954
expeditedRoleID = 1213249725176881208
freightRoleID = 1213249725176881207
groundRoleID = 1213249725176881204
seasonalRoleID = 1213249725176881209
solarRoleID = 1213249725176881206
primeRoleID = 1213249725176881211
expressRoleID = 1213249725176881210
haulRoleID = 1213249725176881205
employeeRoleIDs = [SPSRoleID, driverRoleID, expeditedRoleID, freightRoleID, groundRoleID, seasonalRoleID, solarRoleID, primeRoleID, expressRoleID, haulRoleID]
squads = [" EXPEDITED DELIVERY SQUAD", " FREIGHT DELIVERY SQUAD", "GROUND DELIVERY SQUAD", "SEASONAL DELIVERY SQUAD", " SOLAR DELIVERY SQUAD", " PRIME DELIVERY SQUAD", "EXPRESS DELIVERY SQUAD", " HAUL DELIVERY SQUAD", " HUMAN RESOURCES DEPARTMENT"]
leastToRoleID = dict(zip(squads, employeeRoleIDs[2:]))
SPSGroupID = 12567277
ridgewayGroupID = 6768136

stepNamesReadableToCode = {
    "Contact Complainant": "processes_contacts_complainant",
    "Contact Supervisor": "processes_contacts_supervisor",
    "Contact Employee": "processes_contacts_employee",
    "Contact Witnesses": "processes_contacts_witnesses",
    "Action Recommended": "processes_investigation_actionRecommended",
    "Paperwork": "processes_investigation_papework",
    "Supervisor Approval": "processes_conclusion_investigatorSupervisorApproval",
    "Discipline Enforced": "processes_conclusion_disciplineEnforced",
    "Notification": "notification",
    "Summary": "summary",
    "Closed": "closed"
}

def refresh():
    with open(tokenDir, "r+") as f:
        data = json.load(f)
        key = requests.post("https://www.googleapis.com/oauth2/v4/token", json={"client_id": data["client_id"], "client_secret": data["client_secret"], "refresh_token": data["refresh_token"], "grant_type": "refresh_token", "scopes": ["https://www.googleapis.com/auth/spreadsheets"]}).json()
        data["token"] = key["access_token"]
        data["expiry"] = (datetime.datetime.now() + datetime.timedelta(seconds=key["expires_in"])).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
    return key["access_token"]

with open(tokenDir, "r+") as f:
    data = json.load(f)
    expiry = datetime.datetime.strptime(data["expiry"], "%Y-%m-%dT%H:%M:%S.%fZ")
    if datetime.datetime.now() > expiry:
        refresh()

class Colours:
    brand = 0x8A7761
    green = 0x40F99B
    red = 0xEC3832

class ApplyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Join", style=discord.ButtonStyle.green, emoji="🙋‍♂️", custom_id="application_button")
    async def submitApplication(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.response.send_message(embed=discord.Embed(title="Loading...", colour=Colours.brand, description="Please standby while we process your request").set_thumbnail(url="https://cdn3.emoji.gg/emojis/5490-blurpleload.gif"), ephemeral=True)
        applicant = requests.get(f"https://registry.rover.link/api/guilds/{guildID}/discord-to-roblox/{interaction.user.id}", headers={"Authorization": f"Bearer {roverKey}"}).json()
        if "errorCode" in applicant:
            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like you're verified through rover").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            return
        
        blacklistCheck = dbint.blacklists.check(applicant["robloxId"])
        if blacklistCheck:
            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it looks like you're blacklisted from SPS :grimacing:").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            return

        groups = requests.get(f"https://groups.roblox.com/v1/users/{applicant['robloxId']}/groups/roles").json()["data"]
        residency = [group["role"]["name"] for group in groups if group["group"]["id"] == ridgewayGroupID]
        if not residency:
            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like you're a resident of the State of Ridgeway").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            return
        
        employment = [group["role"]["name"] for group in groups if group["group"]["id"] == SPSGroupID]
        if employment:
            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it looks like you're already employed with us").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            return
        
        acceptance = requests.post(f"https://groups.roblox.com/v1/groups/{SPSGroupID}/join-requests/users/{applicant['robloxId']}", cookies={".ROBLOSECURITY": roblosec})
        acceptance = requests.post(f"https://groups.roblox.com/v1/groups/{SPSGroupID}/join-requests/users/{applicant['robloxId']}", cookies={".ROBLOSECURITY": roblosec}, headers={"x-csrf-token": acceptance.headers["x-csrf-token"]})
        if acceptance.status_code != 200:
            if acceptance.json()["errors"][0]["message"] in ["The user is invalid or does not exist.", "You are already in the maximum number of groups."]:
                await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description=f"Uh-oh, it looks like we ran into the following issue:```\n{acceptance.json()['errors'][0]['message']}\n```").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            elif acceptance.json()["errors"][0]["message"] == "The group join request is invalid.":
                await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description=f"Uh-oh, it looks like you aren't pending to the [SPS Group](https://www.roblox.com/groups/12567277/USA-StudsPerSecond#!/about), go do that and click the apply button again to get accepted").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            else:
                await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description=f"Uh-oh, it looks like we ran into a ⚠ Critical Error ⚠:```\n{acceptance.json()['errors'][0]['message']}\n```If the issue persists, contact the developer (<@{myID}>) with the following error code:\n`SPS:{acceptance.status_code}:{acceptance.json()['errors'][0]['code']}`").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            return

        with open(tokenDir, "r+") as f:
            data = json.load(f)
            expiry = datetime.datetime.strptime(data["expiry"], "%Y-%m-%dT%H:%M:%S.%fZ")
            if datetime.datetime.now() > expiry:
                apiKey = None
            else:
                apiKey = data["token"]
        if not apiKey:
            apiKey = refresh()
        values = requests.get(f"{baseURL}/v4/spreadsheets/{spreadsheetID}/values/'Employee Database'!B1:B", params={"majorDimension": "ROWS", "valueRenderOption": "FORMATTED_VALUE", "dateTimeRenderOption": "FORMATTED_STRING"}, headers={"Authorization": f"Bearer {apiKey}"}).json()
        if "values" not in values:
            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description=f"Uh-oh, it looks like we ran into a ⚠ Critical Error ⚠:```\nGoogle OAuth2 Token Expired\n```If the issue persists, contact the developer (<@{myID}>) with the following error code:\n`SPS:AUTHEXP`").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            return
        
        values = values["values"]
        values = [value[0] if value else "" for value in values]
        if applicant["cachedUsername"] in values:
            row = values.index(applicant["cachedUsername"])
            requests.put(f"{baseURL}/v4/spreadsheets/{spreadsheetID}/values/'Employee Database'!B{row}:I{row}", json={
                "range": f"'Employee Database'!B{row}:I{row}",
                "majorDimension": "ROWS",
                "values": [
                    [f'''=HYPERLINK("https://www.roblox.com/users/{applicant['robloxId']}/profile", "{applicant['cachedUsername']}")''', "Delivery Driver", "Delivery Driver", datetime.datetime.now().strftime("%m/%d/%Y"), "", "", "", "Active"]
                ]
            }, params={"valueInputOption": "RAW"}, headers={"Authorization": f"Bearer {apiKey}"})
        else:
            valuesNoBlanks = [value for value in values if value]
            deps = {}
            for dep in squads:
                deps[dep] = {
                    "start": values.index(dep),
                    "startNoBlank": valuesNoBlanks.index(dep)
                }
            for dep in deps:
                if dep != " HUMAN RESOURCES DEPARTMENT":
                    deps[dep]["members"] = len(valuesNoBlanks[deps[dep]["startNoBlank"]+2:deps[list(deps.keys())[list(deps.keys()).index(dep)+1]]["startNoBlank"]])
            least = sorted({dep: deps[dep]["members"] for dep in deps if dep != " HUMAN RESOURCES DEPARTMENT"}.items(), key=lambda value: value[1])[0][0]
            SPSRole = client.get_role(SPSRoleID)
            driverRole = client.get_role(driverRoleID)
            depRole = client.get_role(leastToRoleID[least])
            await interaction.user.add_roles(SPSRole, driverRole, depRole)
            dep = values[deps[least]["start"]:deps[list(deps.keys())[list(deps.keys()).index(least)+1]]["start"]]
            depReadable = {" EXPEDITED DELIVERY SQUAD": "Expedited", " FREIGHT DELIVERY SQUAD": "Freight", "GROUND DELIVERY SQUAD": "Ground", "SEASONAL DELIVERY SQUAD": "Seasonal", " SOLAR DELIVERY SQUAD": "Solar", " PRIME DELIVERY SQUAD": "Prime", "EXPRESS DELIVERY SQUAD": "Express", " HAUL DELIVERY SQUAD": "Haul"}[least]
            if "" in dep[8:]:
                row = deps[least]["start"] + dep.index("") + 1
                requests.put(f"{baseURL}/v4/spreadsheets/{spreadsheetID}/values/'Employee Database'!B{row}:I{row}", json={
                    "range": f"'Employee Database'!B{row}:I{row}",
                    "majorDimension": "ROWS",
                    "values": [
                        [f'''=HYPERLINK("https://www.roblox.com/users/{applicant['robloxId']}/profile", "{applicant['cachedUsername']}")''', "Delivery Driver", "Delivery Driver", datetime.datetime.now().strftime("%m/%d/%Y"), "", "", "", "Active"]
                    ]
                }, params={"valueInputOption": "RAW"}, headers={"Authorization": f"Bearer {apiKey}"})
            else:
                row = deps[least]["start"] + len(dep)
                requests.post(f"{baseURL}/v4/spreadsheets/{spreadsheetID}:batchUpdate", json={
                    "requests": [
                        {
                            "insertDimension": {
                                "range": {
                                    "sheetId": 384275521,
                                    "dimension": "ROWS",
                                    "startIndex": row,
                                    "endIndex": row+1
                                },
                                "inheritFromBefore": True
                            }
                        }
                    ],
                    "includeSpreadsheetInResponse": False,
                    "responseRanges": [
                        "'Employee Database'!B1:B"
                    ],
                    "responseIncludeGridData": False
                }, headers={"Authorization": f"Bearer {apiKey}"})
                requests.post(f"{baseURL}/v4/spreadsheets/{spreadsheetID}:batchUpdate", json={
                    "requests": [
                        {
                            "updateBorders": {
                                "bottom": {
                                    "style": "SOLID",
                                    "colorStyle": {
                                        "rgbColor": {
                                            "red": 73,
                                            "green": 73,
                                            "blue": 73,
                                            "alpha": 0
                                        }
                                    }
                                },
                                "range": {
                                    "sheetId": 384275521,
                                    "startRowIndex": row-1,
                                    "endRowIndex": row,
                                    "startColumnIndex": 1,
                                    "endColumnIndex": 9
                                }
                            }
                        }
                    ],
                    "includeSpreadsheetInResponse": False,
                    "responseRanges": [
                        "'Employee Database'!B1:B"
                    ],
                    "responseIncludeGridData": False
                }, headers={"Authorization": f"Bearer {apiKey}"})
                row += 1
                requests.post(f"{baseURL}/v4/spreadsheets/{spreadsheetID}:batchUpdate", json={
                    "requests": [
                        {
                            "updateCells": {
                                "rows": [
                                    {
                                        "values": [
                                            {
                                                "userEnteredValue": {
                                                    "formulaValue": f'''=HYPERLINK("https://www.roblox.com/users/{applicant['robloxId']}/profile", "{applicant['cachedUsername']}")'''
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "MIDDLE",
                                                    "wrapStrategy": "WRAP",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "hyperlinkDisplayType": "LINKED",
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                }
                                            },
                                            {
                                                "userEnteredValue": {
                                                    "stringValue": "Delivery Driver"
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "MIDDLE",
                                                    "wrapStrategy": "OVERFLOW_CELL",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                },
                                                "dataValidation": {
                                                    "condition": {
                                                        "type": "ONE_OF_LIST",
                                                        "values": [
                                                            {
                                                                "userEnteredValue": "General Manager"
                                                            },
                                                            {
                                                                "userEnteredValue": "Assistant General Manager"
                                                            },
                                                            {
                                                                "userEnteredValue": "Manager"
                                                            },
                                                            {
                                                                "userEnteredValue": "Assistant Manager"
                                                            },
                                                            {
                                                                "userEnteredValue": "Supervisor"
                                                            },
                                                            {
                                                                "userEnteredValue": "Acting Supervisor"
                                                            },
                                                            {
                                                                "userEnteredValue": "Senior Delivery Driver"
                                                            },
                                                            {
                                                                "userEnteredValue": "Delivery Driver"
                                                            }
                                                        ]
                                                    },
                                                    "showCustomUi": True
                                                }
                                            },
                                            {
                                                "userEnteredValue": {
                                                    "stringValue": "Delivery Driver"
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "MIDDLE",
                                                    "wrapStrategy": "OVERFLOW_CELL",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                }
                                            },
                                            {
                                                "userEnteredValue": {
                                                    "stringValue": datetime.datetime.now().strftime("%m/%d/%Y")
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "MIDDLE",
                                                    "wrapStrategy": "OVERFLOW_CELL",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                }
                                            },
                                            {
                                                "userEnteredValue": {
                                                    "stringValue": ""
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "MIDDLE",
                                                    "wrapStrategy": "OVERFLOW_CELL",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                }
                                            },
                                            {
                                                "userEnteredValue": {
                                                    "stringValue": ""
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "MIDDLE",
                                                    "wrapStrategy": "OVERFLOW_CELL",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                },
                                                "dataValidation": {
                                                    "condition": {
                                                        "type": "ONE_OF_LIST",
                                                        "values": [
                                                            {
                                                                "userEnteredValue": "-"
                                                            },
                                                            {
                                                                "userEnteredValue": "Warning I"
                                                            },
                                                            {
                                                                "userEnteredValue": "Warning II"
                                                            },
                                                            {
                                                                "userEnteredValue": "Warning III"
                                                            },
                                                            {
                                                                "userEnteredValue": "Suspended"
                                                            }
                                                        ]
                                                    },
                                                    "showCustomUi": True
                                                }
                                            },
                                            {
                                                "userEnteredValue": {
                                                    "stringValue": ""
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "MIDDLE",
                                                    "wrapStrategy": "OVERFLOW_CELL",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                }
                                            },
                                            {
                                                "userEnteredValue": {
                                                    "stringValue": "Active"
                                                },
                                                "userEnteredFormat": {
                                                    "numberFormat": {
                                                        "type": "TEXT"
                                                    },
                                                    "borders": {
                                                        "top": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "bottom": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "left": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 73,
                                                                    "green": 73,
                                                                    "blue": 73,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        },
                                                        "right": {
                                                            "style": "SOLID",
                                                            "colorStyle": {
                                                                "rgbColor": {
                                                                    "red": 0,
                                                                    "green": 0,
                                                                    "blue": 0,
                                                                    "alpha": 0
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "horizontalAlignment": "CENTER",
                                                    "verticalAlignment": "BOTTOM",
                                                    "wrapStrategy": "OVERFLOW_CELL",
                                                    "textDirection": "LEFT_TO_RIGHT",
                                                    "textFormat": {
                                                        "foregroundColorStyle": {
                                                            "rgbColor": {
                                                                "red": 171,
                                                                "green": 171,
                                                                "blue": 171,
                                                                "alpha": 0
                                                            }
                                                        },
                                                        "fontFamily": "Roboto",
                                                        "fontSize": 10,
                                                        "bold": False,
                                                        "italic": False,
                                                        "strikethrough": False,
                                                        "underline": False
                                                    },
                                                    "textRotation": {
                                                        "angle": 0
                                                    }
                                                },
                                                "dataValidation": {
                                                    "condition": {
                                                        "type": "ONE_OF_LIST",
                                                        "values": [
                                                            {
                                                                "userEnteredValue": "Active"
                                                            },
                                                            {
                                                                "userEnteredValue": "Leave of Absence"
                                                            },
                                                            {
                                                                "userEnteredValue": "Exempt"
                                                            }
                                                        ]
                                                    },
                                                    "showCustomUi": True
                                                }
                                            }
                                        ]
                                    }
                                ],
                                "fields": "*",
                                "range": {
                                    "sheetId": 384275521,
                                    "startRowIndex": row-1,
                                    "endRowIndex": row,
                                    "startColumnIndex": 1,
                                    "endColumnIndex": 9
                                }
                            }
                        }
                    ],
                    "includeSpreadsheetInResponse": False,
                    "responseRanges": [
                        "'Employee Database'!B1:B"
                    ],
                    "responseIncludeGridData": False
                }, headers={"Authorization": f"Bearer {apiKey}"})

        applicationAgreementViewInstance = ApplicationAgreementView()
        msg = await interaction.user.send(embed=discord.Embed(colour=Colours.brand, description=f"""### StudsPerSecond Application\nHello, {applicant["cachedUsername"]}.\n\nCongratulations! Your application for StudsPerSecond has been accepted.\n\nYou have been placed into the {depReadable} Delivery Squad.\n\nPlease review our company [handbook](https://drive.google.com/file/d/1fHxU-dp-xSv0-I29sBPuLJgbbUrQz6Wd/view?usp=sharing) for vital regulations. Violating any handbook items may result in investigation and disciplinary action.\n\nView the [company roster](https://docs.google.com/spreadsheets/d/1UMcqUpoDjy2AMPXteJBuZpoCBiKO6h8O96o9bua9a08) to see all current employees and their positions.\n\nBy clicking "Submit" you acknowledge reading and understanding the company handbook and contents.\n\nFor any questions, reach out to our administration.\n\n### Employee Onboarding\nBefore you can begin delivering those packages, we need some information from you. We will need your timezone and your service number.\n\nHow do I find my service number?\n\nYour service number is located on the vehicle spawn GUI. You can join team and open that GUI To find this service number. It will be listed below the vehicle name "SPS Ratero," and above the fuel icon.\n\nOnce you're ready to submit this information, please click "Submit" below. Upon receiving a message after submitting confirming this information you may begin delivering.""").set_image(url="https://i.ibb.co/zQL4hkF/Service-Number.png"), view=applicationAgreementViewInstance)
        await interaction.edit_original_response(content=msg.jump_url, embed=None)

class ApplicationAgreementView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Submit", style=discord.ButtonStyle.grey, custom_id="application_agreement")
    async def agreement(self, interaction : discord.Interaction, button : discord.ui.Button):

        class InformationModal(discord.ui.Modal, title="SPS Employee Information Submission"):
            def __init__(self):
                super().__init__(timeout=None)
            
            timezone = discord.ui.TextInput(label="Timezone", style=discord.TextStyle.short, placeholder="EST", min_length=2, max_length=7)
            serviceNumber = discord.ui.TextInput(label="Service Number", style=discord.TextStyle.short, placeholder="1234")

            async def on_submit(self, interaction : discord.Interaction):
                self.stop()
                await interaction.response.send_message(embed=discord.Embed(title="Loading...", colour=Colours.brand, description="Please standby while we process your request").set_thumbnail(url="https://cdn3.emoji.gg/emojis/5490-blurpleload.gif"), ephemeral=True)
                with open(tokenDir, "r+") as f:
                    data = json.load(f)
                    expiry = datetime.datetime.strptime(data["expiry"], "%Y-%m-%dT%H:%M:%S.%fZ")
                    if datetime.datetime.now() > expiry:
                        apiKey = None
                    else:
                        apiKey = data["token"]
                if not apiKey:
                    apiKey = refresh()
                values = requests.get(f"{baseURL}/v4/spreadsheets/{spreadsheetID}/values/'Employee Database'!B1:B", params={"majorDimension": "ROWS", "valueRenderOption": "FORMATTED_VALUE", "dateTimeRenderOption": "FORMATTED_STRING"}, headers={"Authorization": f"Bearer {apiKey}"}).json()
                if "values" not in values:
                    await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description=f"Uh-oh, it looks like we ran into a ⚠ Critical Error ⚠:```\nGoogle OAuth2 Token Expired\n```If the issue persists, contact the developer (<@{myID}>) with the following error code:\n`SPS:AUTHEXP`").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
                    return
                
                values = values["values"]
                values = [value[0] if value else "" for value in values]
                if applicant["cachedUsername"] not in values:
                    await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description=f"Uh-oh, it looks like you either left or were exiled, apply again").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
                    return
                
                row = values.index(applicant["cachedUsername"]) + 1
                requests.put(f"{baseURL}/v4/spreadsheets/{spreadsheetID}/values/'Employee Database'!F{row}:H{row}", json={
                    "range": f"'Employee Database'!F{row}:H{row}",
                    "majorDimension": "ROWS",
                    "values": [
                        [self.timezone.value, "", self.serviceNumber.value]
                    ]
                }, params={"valueInputOption": "RAW"}, headers={"Authorization": f"Bearer {apiKey}"})
                
                await interaction.edit_original_response(embed=discord.Embed(title="Welcome to the Team!", colour=Colours.brand, description="Your information has been processed! \n\nYou're free to begin delivering packages."))
                applicationAgreementViewDisabledInstance = ApplicationAgreementViewDisabled()
                await interaction.message.edit(view=applicationAgreementViewDisabledInstance)

        applicant = requests.get(f"https://registry.rover.link/api/guilds/{guildID}/discord-to-roblox/{interaction.user.id}", headers={"Authorization": f"Bearer {roverKey}"}).json()
        if "errorCode" in applicant:
            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like you're verified through rover").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
            return
        
        informationModalInstance = InformationModal()
        await interaction.response.send_modal(informationModalInstance)

class ApplicationAgreementViewDisabled(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Submit", style=discord.ButtonStyle.grey, disabled=True, custom_id="application_agreement_disabled")
    async def agreement(self, interaction : discord.Interaction, button : discord.ui.Button):
        pass

class ReportView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Report", style=discord.ButtonStyle.red, emoji="📝", custom_id="report_button")
    async def submitReport(self, interaction : discord.Interaction, button : discord.ui.Button):
        complainant = requests.get(f"https://registry.rover.link/api/guilds/{guildID}/discord-to-roblox/{interaction.user.id}", headers={"Authorization": f"Bearer {roverKey}"}).json()
        if "errorCode" in complainant:
            await interaction.response.send_message(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like you're verified through rover").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"), ephemeral=True)
            return

        class ReportModal(discord.ui.Modal, title="SPS Driver Report Form"):
            def __init__(self):
                super().__init__(timeout=None)
            
            username = discord.ui.TextInput(label="Username", style=discord.TextStyle.short, placeholder="OnlyTwentyCharacters", min_length=3, max_length=20)
            events = discord.ui.TextInput(label="Events", style=discord.TextStyle.paragraph, placeholder="Occurence details")
            evidence = discord.ui.TextInput(label="Evidence", style=discord.TextStyle.paragraph, placeholder="Proof of incident")
            date = discord.ui.TextInput(label="Date", style=discord.TextStyle.paragraph, placeholder="When this took place")
            extra = discord.ui.TextInput(label="Extra", style=discord.TextStyle.paragraph, placeholder="Additional information", required=False)

            async def on_submit(self, interaction : discord.Interaction):
                self.stop()
                await interaction.response.send_message(embed=discord.Embed(title="Loading...", colour=Colours.brand, description="Please standby while we process your request").set_thumbnail(url="https://cdn3.emoji.gg/emojis/5490-blurpleload.gif"), ephemeral=True)
                driver = requests.post("https://users.roblox.com/v1/usernames/users", json={"usernames": [self.username.value]}).json()
                if not driver["data"]:
                    await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like the user you reported exists").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
                    return
                driverGroups = requests.get(f"https://groups.roblox.com/v1/users/{driver['data'][0]['id']}/groups/roles").json()
                if SPSGroupID not in [group["group"]["id"] for group in driverGroups["data"]]:
                    await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like the user you reported is employed by SPS").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
                    return
                driverDiscord = requests.get(f"https://registry.rover.link/api/guilds/{guildID}/roblox-to-discord/{driver['data'][0]['id']}", headers={"Authorization": f"Bearer {roverKey}"}).json()
                caseNum = dbint.cases.next()
                dbint.cases.insert(caseStruct([caseNum, interaction.user.name, interaction.user.id, complainant["cachedUsername"], complainant["robloxId"], None if "errorCode" in driverDiscord else driverDiscord["discordUsers"][0]["user"]["username"], None if "errorCode" in driverDiscord else driverDiscord["discordUsers"][0]["user"]["id"], driver["data"][0]["name"], driver["data"][0]["id"], self.events.value, self.evidence.value, self.date.value, self.extra.value, None, 0, None, 0, None, 0, None, 0, 0, 0, 0, 0, "", 0, 0, 0, "", "", 0]))
                listReportsChannel = client.get_channel(listReportsChannelID)
                await listReportsChannel.send(embed=discord.Embed(title=f"Case #{caseNum}", colour=Colours.brand, description="Click below to claim").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"), view=ReportListView())
                await interaction.edit_original_response(embed=discord.Embed(title="Report Received", colour=Colours.green, description="Thank you for you report, we will try get to it as soon as possible.").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
        
        reportModalInstance = ReportModal()
        await interaction.response.send_modal(reportModalInstance)

class ReportListView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Claim", style=discord.ButtonStyle.green, emoji="✋", custom_id="claim_button")
    async def claim(self, interaction : discord.Interaction, button : discord.ui.Button):
        await interaction.response.send_message(embed=discord.Embed(title="Loading...", colour=Colours.brand, description="Please standby while we process your request").set_thumbnail(url="https://cdn3.emoji.gg/emojis/5490-blurpleload.gif"), ephemeral=True)
        investigator = requests.get(f"https://registry.rover.link/api/guilds/{guildID}/discord-to-roblox/{interaction.user.id}", headers={"Authorization": f"Bearer {roverKey}"}).json()
        if "errorCode" in investigator:
            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like you're verified through rover").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"), ephemeral=True)
            return
        
        caseNum = int([embed.title for embed in interaction.message.embeds][0].lstrip("Case #"))
        reportsCategory = client.get_channel(reportsCategoryID)
        ORMRole = interaction.guild.get_role(ORMRoleID)
        reportChannel = await reportsCategory.create_text_channel(f"case-{caseNum}", overwrites={
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, read_messages=True, send_messages=True)
        })
        await reportChannel.move(beginning=True)
        dbint.cases.update(caseNum, "information_investigator_discord_username", interaction.user.name)
        dbint.cases.update(caseNum, "information_investigator_discord_id", interaction.user.id)
        dbint.cases.update(caseNum, "information_investigator_roblox_username", investigator["cachedUsername"])
        dbint.cases.update(caseNum, "information_investigator_roblox_id", investigator["robloxId"])
        case = dbint.cases.get(caseNum)
        await reportChannel.send(interaction.user.mention, embed=discord.Embed(title=f"Case #{caseNum}", colour=Colours.brand)
        .add_field(name="Complainant", value=f"<@{case.information.complainant.discord.id}> / [{case.information.complainant.roblox.username}](https://www.roblox.com/users/{case.information.complainant.roblox.id}/profile)")
        .add_field(name="Employee", value=f"{f'<@{case.information.employee.discord.id}> / ' if case.information.employee.discord.id else ''}[{case.information.employee.roblox.username}](https://www.roblox.com/users/{case.information.employee.roblox.id}/profile)")
        .add_field(name="What", value=case.information.what, inline=False)
        .add_field(name="Evidence", value=case.information.evidence, inline=False)
        .add_field(name="When", value=case.information.when, inline=False)
        .add_field(name="Extra", value=case.information.extra, inline=False)
        .set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
        await interaction.message.edit(embed=discord.Embed(title=f"Case #{caseNum}", colour=Colours.brand, description=f"Claimed by {interaction.user.mention} / [{investigator['cachedUsername']}](https://www.roblox.com/users/{investigator['robloxId']}/profile)").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"), view=ReportListClaimedView())
        for step in list(stepNamesReadableToCode.keys()):
            await reportChannel.send(embed=discord.Embed(title=step if step != "Notification" else None, colour=Colours.red, description=None if step != "Notification" else f"### {step}"), view=ChecklistNotStartedView())
        await interaction.edit_original_response(content=reportChannel.mention, embed=None)

class ReportListClaimedView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Claim", style=discord.ButtonStyle.green, emoji="✋", disabled=True, custom_id="claim_button_disabled")
    async def claim(self, interaction : discord.Interaction, button : discord.ui.Button):
        pass

class ChecklistNotStartedView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Begin", style=discord.ButtonStyle.blurple, emoji="🔧", custom_id="not_start_to_begin")
    async def Begin(self, interaction : discord.Interaction, button : discord.ui.Button):
        embed = [embed for embed in interaction.message.embeds][0]
        embed.colour = Colours.brand
        await interaction.message.edit(embed=embed, view=ChecklistBegunView())
        await interaction.response.send_message("Step Marked as `Begun`", ephemeral=True)

class ChecklistBegunView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Complete", style=discord.ButtonStyle.green, emoji="✅", custom_id="complete")
    async def complete(self, interaction : discord.Interaction, button : discord.ui.Button):
        embed = [embed for embed in interaction.message.embeds][0]
        responded = False

        if embed.title == "Supervisor Approval":
            supervisor = dbint.ormsupervisor.get()
            if interaction.user.id != supervisor.discord.id:
                await interaction.response.send_message(f"Please get your **supervisor** (<@{supervisor.discord.id}> / [{supervisor.roblox.username}](https://www.roblox.com/users/{supervisor.roblox.id}/profile)) to mark this step as `Complete`", ephemeral=True)
                return

        if embed.title == "Closed":
            case = dbint.cases.get(int(interaction.channel.name.lstrip("case-")))
            reqs = [case.processes.investigation.actionRecommended, case.processes.conclusion.investigatorSupervisorApproval, case.notification, case.summary]
            if not all(reqs):
                reqToReadable = ["Action Recommended", "Supervisor Approval", "Notification", "Summary"]
                notDone = []
                for req in range(len(reqs)):
                    if not reqs[req]:
                        notDone.append(reqToReadable[req])
                await interaction.response.send_message(f"Uh-oh, it look like you're missing the following **required** step(s):```\n" + "\n".join(notDone) + "\n```", ephemeral=True)
                return
            class ClosedConfirmView(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)
                
                @discord.ui.button(label="Yes", style=discord.ButtonStyle.green, emoji="✅")
                async def yes(self, interaction2 : discord.Interaction, button : discord.ui.Button):
                    self.stop()
                    case = dbint.cases.get(int(interaction2.channel.name.lstrip("case-")))
                    await interaction2.response.send_message("Case Closed", ephemeral=True)
                    archivesCategory = client.get_channel(archivesCategoryID)
                    if len(archivesCategory.channels) == 50:
                        await archivesCategory.channels[-1].delete(reason="Clearance (50+)")
                    await interaction2.channel.edit(category=archivesCategory, overwrites={
                        interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False)
                    })
                    caseLogsChannel = client.get_channel(caseLogsChannelID)
                    actionLogsChannel = client.get_channel(actionLogsChannelID)
                    action = case.processes.investigation.actionRecommended
                    if action != "N/A":
                        with open(tokenDir, "r+") as f:
                            data = json.load(f)
                            expiry = datetime.datetime.strptime(data["expiry"], "%Y-%m-%dT%H:%M:%S.%fZ")
                            if datetime.datetime.now() > expiry:
                                apiKey = None
                            else:
                                apiKey = data["token"]
                        if not apiKey:
                            apiKey = refresh()
                        values = requests.get(f"{baseURL}/v4/spreadsheets/{spreadsheetID}/values/'Employee Database'!B1:B", params={"majorDimension": "ROWS", "valueRenderOption": "FORMATTED_VALUE", "dateTimeRenderOption": "FORMATTED_STRING"}, headers={"Authorization": f"Bearer {apiKey}"}).json()
                        if "values" not in values:
                            await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description=f"Uh-oh, it looks like we ran into a ⚠ Critical Error ⚠:```\nGoogle OAuth2 Token Expired\n```If the issue persists, contact the developer (<@{myID}>) with the following error code:\n`SPS:AUTHEXP`").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
                            return
                        
                        values = values["values"]
                        if action == "Record":
                            pass
                        elif action == "Suspended":
                            pass
                        elif action in ["Terminated", "Blacklisted"]:
                            removal = requests.delete(f"https://groups.roblox.com/v1/groups/{SPSGroupID}/users/{applicant['robloxId']}", cookies={".ROBLOSECURITY": roblosec})
                            removal = requests.delete(f"https://groups.roblox.com/v1/groups/{SPSGroupID}/users/{applicant['robloxId']}", cookies={".ROBLOSECURITY": roblosec}, headers={"x-csrf-token": removal.headers["x-csrf-token"]})
                            roles = []
                            for roleID in employeeRoleIDs:
                                roles.append(client.get_role(roleID))
                            
                            if action == "Terminated":
                                #
                                pass
                            if action == "Blacklisted":
                                dbint.blacklists.insert(userStruct([case.information.employee.discord.username, case.information.employee.discord.id, case.information.employee.roblox.username, case.information.employee.roblox.id]))
                        await actionLogsChannel.send(embed=discord.Embed(title="Department Action", colour={"Verbal": 0xebc634, "Record": 0xeb9934, "Suspended": 0x3b3b3b, "Terminated": 0xeb3434, "Blacklisted": 0x1a1a1a}[action], description=f"**{case.information.employee.roblox.username}** has been **{ {'Verbal': 'given a verbal warning', 'Record': 'given a recorded warning', 'Suspended': 'suspended', 'Terminated': 'terminated', 'Blacklisted': 'blacklisted'}[action]}** as a result of ORM Case #{case.caseNum}").set_footer(text=case.information.investigator.roblox.username, icon_url="https://i.ibb.co/r2rJJQ4/Logo.png"))
                    await caseLogsChannel.send(embed=discord.Embed(title=f"Office of Risk Management Case #{case.caseNum} Release", colour=Colours.brand, description=f"**Verdict:**\n{'CONSISTENT' if action == 'N/A' else 'INCONSISTENT'}\n\n**Driver in Question:**\n{case.information.employee.roblox.username}\n\n**Investigation Findings:**\n{case.summary}\n\n**Punishment:**\n{ {'Verbal': 'Verbal Warning', 'Record': 'Recorded Warning', 'Suspended': 'Suspension', 'Terminated': 'Termination', 'Blacklisted': 'Blacklisted'}[action]}\n\n*You can view the case report of the investigation in the link below for more details and information about the investigation and case.*\n\n[LINK]({case.notification})").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))

                @discord.ui.button(label="No", style=discord.ButtonStyle.red, emoji="❎")
                async def no(self, interaction2 : discord.Interaction, button : discord.ui.Button):
                    self.stop()
                    await interaction2.response.send_message("Disregarding", ephemeral=True)
                    return
            
            class ClosedFinishedView(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)
                
                @discord.ui.button(label="Yes", style=discord.ButtonStyle.green, emoji="✅", disabled=True)
                async def yes(self, interaction2 : discord.Interaction, button : discord.ui.Button):
                    pass
                
                @discord.ui.button(label="No", style=discord.ButtonStyle.red, emoji="❎", disabled=True)
                async def no(self, interaction2 : discord.Interaction, button : discord.ui.Button):
                    pass
            
            checklistBegunViewInstance = ClosedConfirmView()
            await interaction.response.send_message("Are you sure?", view=checklistBegunViewInstance)
            but = await checklistBegunViewInstance.wait()
            closedFinishedViewInstance = ClosedFinishedView()
            await interaction.edit_original_response(view=closedFinishedViewInstance)
            responded = True

        if embed.title == "Action Recommended":
            class ActionView(discord.ui.View):
                def __init__(self):
                    super().__init__(timeout=None)
                
                @discord.ui.select(options=[discord.SelectOption(label="No Punishment", value="N/A", emoji="👍"), discord.SelectOption(label="Verbal Warning", value="Verbal", emoji="📏"), discord.SelectOption(label="Record Warning", value="Record", emoji="👮‍♂️"), discord.SelectOption(label="Suspension", value="Suspended", emoji="🐶"), discord.SelectOption(label="Termination", value="Terminated", emoji="🔥"), discord.SelectOption(label="Blacklist", value="Blacklisted", emoji="🔨")])
                async def on_submit(self, interaction2 : discord.Interaction, dropdown : discord.ui.Select):
                    self.stop()
                    if dropdown.values:
                        dbint.cases.update(int(interaction2.channel.name.lstrip("case-")), "processes_investigation_actionRecommended", dropdown.values[0])
                        await interaction2.response.send_message("Step Marked as `Complete`", ephemeral=True)
                    else:
                        await interaction2.response.send_message("Uh-oh, it looks like you haven't picked a punishment", ephemeral=True)
            
            actionViewInstance = ActionView()
            await interaction.response.send_message(view=actionViewInstance, ephemeral=True)
            await actionViewInstance.wait()
            responded = True

        if embed.title == "Summary":
            class SummaryModal(discord.ui.Modal, title="Report Title"):
                def __init__(self):
                    super().__init__(timeout=None)
                
                summary = discord.ui.TextInput(label="Summary", style=discord.TextStyle.long, placeholder="tl;dr")

                async def on_submit(self, interaction2 : discord.Interaction):
                    self.stop()
                    dbint.cases.update(int(interaction2.channel.name.lstrip("case-")), "summary", self.summary.value)
                    await interaction2.response.send_message("Step Marked as `Complete`", ephemeral=True)
            
            summaryModalInstance = SummaryModal()
            await interaction.response.send_modal(summaryModalInstance)
            await summaryModalInstance.wait()
            responded = True

        if embed.description: #Notification
            class NotificationModal(discord.ui.Modal, title="Report Title"):
                def __init__(self):
                    super().__init__(timeout=None)
                
                link = discord.ui.TextInput(label="Document Link", style=discord.TextStyle.short, placeholder="https://docs.google.com/document/d/uniqueID/edit")

                async def on_submit(self, interaction2 : discord.Interaction):
                    self.stop()
                    embed = [embed for embed in interaction2.message.embeds][0]
                    dbint.cases.update(int(interaction2.channel.name.lstrip("case-")), "notification", self.link.value)
                    embed.description = f"### [Notification]({self.link.value})"
                    await interaction2.response.send_message("Step Marked as `Complete`", ephemeral=True)
            
            notificationModalInstance = NotificationModal()
            await interaction.response.send_modal(notificationModalInstance)
            await notificationModalInstance.wait()
            responded = True
        elif embed.title not in ["Action Recommended", "Summary"]:
            dbint.cases.update(int(interaction.channel.name.lstrip("case-")), stepNamesReadableToCode[embed.title], 1)
        
        embed.colour = Colours.green
        await interaction.message.edit(embed=embed, view=ChecklistFinishedView())

        if not responded:
            await interaction.response.send_message(content="Step Marked as `Complete`", ephemeral=True)
    
    @discord.ui.button(label="Not Begun", style=discord.ButtonStyle.red, emoji="❎", custom_id="not_started")
    async def notBegun(self, interaction : discord.Interaction, button : discord.ui.Button):
        embed = [embed for embed in interaction.message.embeds][0]
        embed.colour = Colours.red
        await interaction.message.edit(embed=embed, view=ChecklistNotStartedView())
        await interaction.response.send_message("Step Marked as `Not Begun`", ephemeral=True)

class ChecklistFinishedView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Work on Again", style=discord.ButtonStyle.blurple, emoji="🔧", custom_id="complete_to_begin")
    async def notBegun(self, interaction : discord.Interaction, button : discord.ui.Button):
        embed = [embed for embed in interaction.message.embeds][0]

        if embed.description:
            dbint.cases.update(int(interaction.channel.name.lstrip("case-")), "notification", 0)
        else:
            dbint.cases.update(int(interaction.channel.name.lstrip("case-")), stepNamesReadableToCode[embed.title], 0)

        embed.colour = Colours.brand
        await interaction.message.edit(embed=embed, view=ChecklistBegunView())
        await interaction.response.send_message("Step Marked as `Begun`", ephemeral=True)

async def connectViews():
    applyViewInstance = ApplyView()
    aplicationAgreementViewInstance = ApplicationAgreementView()
    reportViewInstance = ReportView()
    reportListViewInstance = ReportListView()
    reportListClaimedViewInstance = ReportListClaimedView()
    checklistNotStartedViewInstance = ChecklistNotStartedView()
    checklistBegunViewInstance = ChecklistBegunView()
    checklistFinishedViewInstance = ChecklistFinishedView()
    views = [applyViewInstance, aplicationAgreementViewInstance, reportViewInstance, reportListViewInstance, reportListClaimedViewInstance, checklistNotStartedViewInstance, checklistBegunViewInstance, checklistFinishedViewInstance]
    for view in views:
        client.add_view(view)

@client.event
async def on_ready():
    await connectViews()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="StudsPerSecond"))
    print(f"SPS Automation now online with {round(client.latency * 1000)}ms ping.")

@tree.command(name="terminate", description="Terminate a driver from StudsPerSecond")
async def terminate(interaction : discord.Interaction, user : discord.Member):
    await interaction.response.send_mesage("ok")

@tree.command(name="setormsupervisor", description="Set the Office of Risk Management Supervisor")
async def setormsupervisor(interaction : discord.Interaction, user : discord.Member):
    await interaction.response.send_message(embed=discord.Embed(title="Loading...", colour=Colours.brand, description="Please standby while we process your request").set_thumbnail(url="https://cdn3.emoji.gg/emojis/5490-blurpleload.gif"), ephemeral=True)
    if interaction.user.id not in [myID, gmID]:
        await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like you have access to this").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
        return
    supervisor = requests.get(f"https://registry.rover.link/api/guilds/{guildID}/discord-to-roblox/{user.id}", headers={"Authorization": f"Bearer {roverKey}"}).json()
    if "errorCode" in supervisor:
        await interaction.edit_original_response(embed=discord.Embed(title="Error", colour=Colours.red, description="Uh-oh, it doesn't look like that user is verified through rover").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))
        return
    dbint.ormsupervisor.insert(userStruct([user.name, user.id, supervisor["cachedUsername"], supervisor["robloxId"]]))
    await interaction.edit_original_response(embed=discord.Embed(title="ORM Supervisor Set", colour=Colours.green, description=f"{user.mention} / `{supervisor['cachedUsername']}` has been set as the Office of Risk Management Supervisor").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"))

@client.command()
@commands.check(lambda ctx : ctx.author.id == myID)
async def apply(ctx):
    applyViewInstance = ApplyView()
    await ctx.channel.send(embed=discord.Embed(title="Apply", colour=Colours.brand, description="Looking for an exciting opportunity to be part of a dynamic delivery team? Apply now to join SPS and start your journey with us! As an SPS team member, you'll experience the thrill of delivering packages and ensuring customer satisfaction. Click the button below to apply, qualified applicants will be automatically accepted. Don't miss out on this chance to be part of something amazing!").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"), view=applyViewInstance)

@client.command()
@commands.check(lambda ctx : ctx.author.id == myID)
async def report(ctx):
    reportViewInstance = ReportView()
    await ctx.channel.send(embed=discord.Embed(title="Submit Report", colour=Colours.brand, description="This is the misconduct report form managed by the Office of Risk Management and StudsPerSecond leadership. If you witness misconduct and would like it investigated and enforced by the Office of Risk Management and StudsPerSecond Leadership, fill out this report form to launch an investigation into the accused delivery driver(s).\n\nYou can remain anonymous, but if you do sign your name it will be kept confidential and you will only be contacted by Office of Risk Management personnel or StudsPerSecond Leadership for follow-up questions regarding the investigation.").set_thumbnail(url="https://i.ibb.co/r2rJJQ4/Logo.png"), view=reportViewInstance)

@client.command()
@commands.check(lambda ctx : ctx.author.id == myID)
async def connect(ctx):
    await tree.sync()

client.run('MTIxMzE1NTUwMjMzNTQ2MzQ5NA.GEfpcf.E3kuaDG_zer--pK14InvRCv829i0WHrg2-QmnU')
#https://discord.com/oauth2/authorize?client_id=1213155502335463494&permissions=8&scope=bot
#https://trello.com/b/XFyJ8eVV/sps-orm-copy

#SPSAutomation
#$eCuResTP@ss$sw0RD