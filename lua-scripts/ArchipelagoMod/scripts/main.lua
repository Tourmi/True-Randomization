require("archipelago")
require("utils")
require("bloodstainedUtils")
require("UEHelpers")

ModPrint("Loading mod")

---@type Archipelago
local ap = nil

---@param commandParts table
function ProcessCommand(commandParts)
    if #commandParts < 2 or #commandParts > 3 then
        MessagePlayer("Command was invalid, should be '/connect host:ip slotname password'")
        ModPrint(table.concat(commandParts, ", "))
        return
    end

    local host = commandParts[1]
    local slotname = commandParts[2]
    local password = ""
    if #commandParts == 3 then
        password = commandParts[3]
    end
    if ap ~= nil then
        ap:Stop()
        ap = nil
    end

    ap = Archipelago:new()
    ExecuteAsync(function()
        ap:Start(host, slotname, password)
    end)
end

RegisterConsoleCommandGlobalHandler("/connect", function(cmd, commandParts, ar)
    ProcessCommand(commandParts)
    return true
end)

ModPrint("Finished loading mod")
